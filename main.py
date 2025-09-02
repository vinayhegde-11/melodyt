import os
from pathlib import Path
from player.vlc_engine import VLCPlayer
import time

if __name__ == "__main__":
    music_folder = Path.home() / "Music"
    songs = list(music_folder.glob("*.mp3"))

    if not songs:
        print(f"No songs found in {music_folder}")
    else:
        playlist = [str(song) for song in songs]
        player = VLCPlayer(playlist)
        print("Playing: ",Path(player.playlist[player.current_index]).name)
        player.play()

        print("\nControls: [p] Pause / Resume  || [q] Quit")
        while True:
            cmd = input(">>>").strip().lower()
            if cmd == "p":
                player.pause()
            elif cmd == "n":
                player.next()
                if not player.stopped:
                    print("Playing: ",Path(player.playlist[player.current_index]).name)
            elif cmd == "b":
                player.previous()
                print("Playing: ",Path(player.playlist[player.current_index]).name)
            elif cmd == "s":
                player.toggle_shuffle()
            elif cmd == "r":
                player.toggle_repeat()
            elif cmd == "q":
                player.stop()
                print("Stopped")
                break
