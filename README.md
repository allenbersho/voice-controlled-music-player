# Voice-Controlled Local Music Player 🎵🎙️

A Python desktop application that plays local music files using **voice commands**. Built with `Tkinter`, `pygame`, and `speech_recognition`, this app lets you control music playback completely hands-free.

---

## ✅ Features

- 🎙️ Voice-controlled music player
- 🖥️ Simple GUI built using Tkinter
- 🎵 Supports MP3 and WAV files
- ⏯️ Commands like play, pause, resume, stop, next, previous, shuffle
- 🗣️ Displays the spoken command in the GUI

---

## 📁 Folder Structure

```
voice_music_player/
├── voice_gui.py          # Main application script
├── songs/                # Folder for local MP3/WAV files
│   ├── faded.mp3
│   └── believer.mp3
```

---

## 🔧 Requirements

Install the following Python packages:

```bash
pip install pygame speechrecognition
```

> Note: You may also need `pyaudio`. On Windows, install using a `.whl` file if needed.

---

## ▶️ How to Run

1. Add your `.mp3` or `.wav` files inside the `songs/` folder.
2. Run the app using:

```bash
python voice_gui.py
```

3. Click **Start Listening** and give commands like:
   - "Play faded"
   - "Pause"
   - "Resume"
   - "Next"
   - "Stop listening"

4. The app will display the recognized voice command and current song.

---

## 🧠 Future Improvements (optional)

- Volume control
- Playlist display in GUI
- Packaging to `.exe`

---

## 🏁 Built With

- Python 3.x
- Tkinter
- pygame
- speech_recognition