import tkinter as tk
import speech_recognition as sr
import pygame
import os
import threading
import random

# === INIT BLOCK ===
music_folder = "songs"
playlist = [file for file in os.listdir(music_folder) if file.endswith(('.mp3', '.wav'))]
playlist.sort()
current_index = 0
current_song = None
recognizer = sr.Recognizer()
is_listening = False

# === PYGAME INIT ===
pygame.mixer.init()

# === MAIN FUNCTION ===
def handle_command(command):
    global current_index, current_song
    command = command.lower()

    if "play" in command:
        for i, file in enumerate(playlist):
            filename = file.lower().replace(".mp3", "").replace(".wav", "")
            if filename in command:
                pygame.mixer.music.load(os.path.join(music_folder, file))
                pygame.mixer.music.play()
                current_index = i
                current_song = file
                update_song_label(file)
                return

    elif "pause" in command:
        pygame.mixer.music.pause()

    elif "resume" in command or "continue" in command:
        pygame.mixer.music.unpause()

    elif "stop" in command:
        pygame.mixer.music.stop()

    elif "next" in command:
        current_index = (current_index + 1) % len(playlist)
        next_song = playlist[current_index]
        pygame.mixer.music.load(os.path.join(music_folder, next_song))
        pygame.mixer.music.play()
        current_song = next_song
        update_song_label(next_song)

    elif "previous" in command:
        current_index = (current_index - 1) % len(playlist)
        prev_song = playlist[current_index]
        pygame.mixer.music.load(os.path.join(music_folder, prev_song))
        pygame.mixer.music.play()
        current_song = prev_song
        update_song_label(prev_song)

    elif "random" in command or "shuffle" in command:
        current_index = random.randint(0, len(playlist) - 1)
        random_song = playlist[current_index]
        pygame.mixer.music.load(os.path.join(music_folder, random_song))
        pygame.mixer.music.play()
        current_song = random_song
        update_song_label(random_song)

# === LISTENING LOOP ===
def listen_loop():
    global is_listening
    is_listening = True
    while is_listening:
        with sr.Microphone() as source:
            status_label.config(text="🎤 Listening...")
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("🗣️ You said:", command)

            if "stop listening" in command.lower():
                stop_listening()
                break

            handle_command(command)

        except:
            status_label.config(text="❌ Could not understand.")

# === START/STOP ===
def start_listening():
    threading.Thread(target=listen_loop).start()

def stop_listening():
    global is_listening
    is_listening = False
    status_label.config(text="🛑 Stopped listening")
    pygame.mixer.music.stop()

# === GUI SETUP ===
window = tk.Tk()
window.title("Voice-Controlled Music Player")
window.geometry("400x250")

title_label = tk.Label(window, text="🎵 Voice Music Player", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

song_label = tk.Label(window, text="No song playing", font=("Helvetica", 12))
song_label.pack(pady=10)

status_label = tk.Label(window, text="Click Start to begin", font=("Helvetica", 10), fg="blue")
status_label.pack(pady=10)

start_button = tk.Button(window, text="Start Listening", command=start_listening, bg="green", fg="white")
start_button.pack(pady=5)

stop_button = tk.Button(window, text="Stop Listening", command=stop_listening, bg="red", fg="white")
stop_button.pack(pady=5)

def update_song_label(song):
    song_label.config(text=f"Now playing: {song}")

# === RUN ===
window.mainloop()
