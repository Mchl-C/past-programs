import os
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

def play_audio_files():
    # Get the current working directory (where the script and audio files are located)
    folder_path = os.getcwd()
    print(f"Current working directory: {folder_path}")

    # List all files in the directory for debugging
    all_files = os.listdir(folder_path)
    print(f"All files in folder: {all_files}")

    # Get a list of all audio files (case-insensitive check for extensions)
    audio_files = [f for f in all_files if f.lower().endswith(('.mp3', '.wav', '.ogg'))]
    print(f"Detected audio files: {audio_files}")

    if not audio_files:
        print("No audio files found in the folder.")
        return
    
    while True:
        # Play each file in the folder
        for audio_file in audio_files:
            file_path = os.path.join(folder_path, audio_file)
            print(f"Playing {audio_file}")
            
            # Load and play the audio file
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            
            # Wait until the audio file finishes playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)

# Start playing the audio files continuously
play_audio_files()
