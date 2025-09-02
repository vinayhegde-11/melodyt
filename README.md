# Melodyt

Melodyt is a simple command-line music player built with Python and VLC. It scans your specified music directory for audio files (currently only `.mp3` is supported) and lets you play, pause, skip, shuffle, and repeat tracks directly from the terminal.

## Features
- **Automatic Playlist**: Loads all `.mp3` files from your music folder. (Support for more audio formats coming soon)
- **Playback Controls**: Play, pause/resume, next, previous, shuffle, and repeat modes.
- **VLC Backend**: Uses VLC for robust media playback.
- **Simple CLI**: Control playback with single-key commands.

## Usage
1. **Install dependencies**:
	```bash
	pip install -r requirements.txt
	```
2. **Run the player**:
	```bash
	python3 main.py
	```
3. **Controls**:
	- `p`: Pause/Resume
	- `n`: Next track
	- `b`: Previous track
	- `s`: Toggle shuffle
	- `r`: Toggle repeat mode
	- `q`: Quit

## Project Structure
- `main.py`: Entry point, handles CLI and user interaction.
- `player/vlc_engine.py`: VLC-based player logic (play, pause, next, previous, shuffle, repeat).
- `requirements.txt`: Python dependencies (`python-vlc`, `yt-dlp`).
- `downloader/`, `ui/`, `utils/`: Reserved for future features (currently empty).

## Requirements
- Python 3.10+
- VLC media player installed on your system
- Python packages: `python-vlc`, `yt-dlp`

## TODO
- Add a downloader for online music sources
- Support for additional audio file extensions (e.g., `.wav`, `.flac`, `.aac`)
- Develop a graphical UI
- Add utility scripts for playlist management

---
Feel free to contribute or suggest features!