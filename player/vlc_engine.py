import vlc
import os
import random

class VLCPlayer:
    def __init__(self,playlist=[]):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.playlist = playlist or []
        self.current_index = 0
        self.shuffle = False
        self.history = []
        self.repeat_mode = "none"

    def set_playlist(self,playlist):
        self.playlist = playlist
        self.current_index = 0
        self.history = []

    def toggle_repeat(self):
        modes = ["none","track","playlist"]
        idx = modes.index(self.repeat_mode)
        self.repeat_mode = modes[(idx + 1) % len(modes)]
        print("Repeat mode:",self.repeat_mode)

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle
        print("Shuffle is now", "On" if self.shuffle else "Off")

    def play(self, file_path=None):
        """Play a specific file or the current one in the playlist."""
        if file_path:
            path = file_path
        elif self.playlist:
            path = self.playlist[self.current_index]
        else:
            raise ValueError("No file or playlist set.")

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        media = self.instance.media_new(path)
        self.player.set_media(media)
        self.player.play()
    
    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
    
    def next(self):
        self.stopped = False
        if not self.playlist:
            return
        
        if self.repeat_mode == "track":
            self.play()
            return
        
        self.history.append(self.current_index)
        if self.shuffle:
            next_index = self.current_index
            while next_index == self.current_index and len(self.playlist) > 1:
                next_index = random.randint(0,len(self.playlist)-1)
            self.current_index = next_index
        else:
            self.current_index += 1
            if self.current_index >= len(self.playlist):
                if self.repeat_mode == "playlist":
                    self.current_index = 0
                else:
                    self.current_index = len(self.playlist) - 1
                    print("End of playlist")
                    self.stop()
                    self.stopped = True
                    return
        self.play()
    
    def previous(self):
        if self.history:
            self.current_index = self.history.pop()
            self.play()
        else:
            if not self.playlist:
                return
            next_index = self.current_index
            while next_index == self.current_index and len(self.playlist) > 1:
                next_index = random.randint(0, len(self.playlist) - 1)
            self.current_index = next_index
            self.play()
    
    def is_playing(self):
        return self.player.is_playing() == 1