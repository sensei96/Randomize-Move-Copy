import os
import random
import shutil

def get_all_videos(base_folder):
    video_files = []
    if not os.path.exists(base_folder):
        print(f"Folder sumber '{base_folder}' tidak ditemukan, membuat folder baru...")
        os.makedirs(base_folder)
    for file in os.listdir(base_folder):
        if file.lower().endswith(".mp4"):
            video_files.append(os.path.join(base_folder, file))
    return video_files

def select_and_move_videos(base_folder, output_folder, num_videos=14):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    video_files = get_all_videos(base_folder)
    
    if len(video_files) < num_videos:
        print(f"Hanya ditemukan {len(video_files)} video, kurang dari {num_videos}.")
        num_videos = len(video_files)
    
    selected_videos = random.sample(video_files, num_videos)
    
    for i, video in enumerate(selected_videos, start=1):
        new_name = os.path.join(output_folder, f"v{i}.mp4")
        
        # Jika file dengan nama yang sama sudah ada, lewati
        if os.path.exists(new_name):
            print(f"File {new_name} sudah ada, dilewati.")
            continue
        
        shutil.move(video, new_name)
    
    print(f"{num_videos} video telah dipindahkan ke {output_folder} tanpa menimpa file yang sudah ada.")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_folder = script_dir  # Gunakan lokasi script sebagai base folder
    output_folder = os.path.join(script_dir, "output")  # Folder 'output' di lokasi script
    select_and_move_videos(base_folder, output_folder)