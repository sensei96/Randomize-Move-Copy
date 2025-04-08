import os
import random
import shutil
from datetime import datetime

LOG_FILENAME = "copy_log.txt"

def get_all_wav_files(base_folder):
    wav_files = []
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.lower().endswith(".wav"):
                full_path = os.path.join(root, file)
                wav_files.append(full_path)
    return wav_files

def load_existing_log(log_path):
    used_files = {}
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    _, vname, filepath = parts
                    used_files[vname] = filepath
    return used_files

def append_log(log_path, vname, filepath):
    with open(log_path, "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d")
        f.write(f"{now} | {vname} | {filepath}\n")

def select_and_copy_wavs(base_folder, num_files=14):
    all_wavs = get_all_wav_files(base_folder)
    log_path = os.path.join(base_folder, LOG_FILENAME)
    used_log = load_existing_log(log_path)

    used_paths = set(used_log.values())  # Set file yg sudah pernah dipakai untuk nama tertentu

    available_files = [f for f in all_wavs if f not in used_paths]

    if len(available_files) < num_files:
        print(f"File .wav unik yang tersedia hanya {len(available_files)} dari {num_files} yang diminta.")
        num_files = len(available_files)

    selected_files = random.sample(available_files, num_files)

    for i, src_file in enumerate(selected_files, start=1):
        vname = f"v{i}.wav"
        dst_file = os.path.join(base_folder, vname)

        if os.path.exists(dst_file):
            print(f"{vname} sudah ada di folder, dilewati.")
            continue

        shutil.copy2(src_file, dst_file)
        append_log(log_path, vname, src_file)
        print(f"{vname} disalin dari: {os.path.dirname(src_file)}")

    print(f"{num_files} file .wav unik berhasil disalin ke folder: '{base_folder}'.")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    select_and_copy_wavs(script_dir)
