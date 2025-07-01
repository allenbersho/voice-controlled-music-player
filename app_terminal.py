import speech_recognition as sr
import pygame
import os
import time
import speech_recognition as sr
import random

mic_list = sr.Microphone.list_microphone_names()

# Initialize pygame mixer
pygame.mixer.init()

# Path to songs folder
music_folder = "songs"

recognizer = sr.Recognizer()
mic = sr.Microphone()
playlist = [file for file in os.listdir(music_folder) if file.endswith(('.mp3', '.wav'))]
playlist.sort()

current_index = 0  # Track the current song index

def play(command, current_song):
    global current_index
    command = command.lower()

    if "play" in command:
        # Try to extract song name
        for i, file in enumerate(playlist):
            filename = file.lower().replace(".mp3", "").replace(".wav", "")
            if filename in command:
                pygame.mixer.music.load(os.path.join(music_folder, file))
                pygame.mixer.music.play()
                print(f"▶️ Playing: {file}")
                current_index = i  # ✅ update index
                return file
        print("⚠️ Song not found.")

    elif "pause" in command:
        pygame.mixer.music.pause()
        print("⏸️ Music paused.")

    elif "resume" in command or "continue" in command:
        pygame.mixer.music.unpause()
        print("▶️ Music resumed.")

    elif "stop" in command:
        pygame.mixer.music.stop()
        print("⏹️ Music stopped.")

    elif "next" in command:
        current_index = (current_index + 1) % len(playlist)
        next_song = playlist[current_index]
        pygame.mixer.music.load(os.path.join(music_folder, next_song))
        pygame.mixer.music.play()
        print(f"⏭️ Next: {next_song}")
        return next_song

    elif "previous" in command:
        current_index = (current_index - 1) % len(playlist)
        prev_song = playlist[current_index]
        pygame.mixer.music.load(os.path.join(music_folder, prev_song))
        pygame.mixer.music.play()
        print(f"⏮️ Previous: {prev_song}")
        return prev_song

    elif "random" in command or "shuffle" in command:
        current_index = random.randint(0, len(playlist) - 1)
        random_song = playlist[current_index]
        pygame.mixer.music.load(os.path.join(music_folder, random_song))
        pygame.mixer.music.play()
        print(f"🔀 Shuffling to: {random_song}")
        return random_song

    else:
        print("❓ Command not recognized.")

    return current_song


current_song = None
print("🎤 Voice-controlled music player is now listening... (say 'stop listening' to exit)")

while True:
    with sr.Microphone() as source:
        print("\n🎧 Say a command:")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("🗣️ You said:", command)

        if "stop listening" in command.lower():
            print("👋 Exiting voice control.")
            pygame.mixer.music.stop()
            break

        current_song = play(command, current_song)

    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError:
        print("❌ Could not reach speech service.")