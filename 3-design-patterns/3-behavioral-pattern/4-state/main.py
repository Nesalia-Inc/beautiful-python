from __future__ import annotations

from typing import Protocol



class MediaState(Protocol):
    player : MediaPlayer
    
    def play(self) -> None: ...
    def pause(self) -> None: ...
    
    
    
class PlayingState(MediaState):
    def __init__(self, player : MediaPlayer) -> None:
        self.player = player

    def play(self) -> None:
        print("Le média est déjà en lecture")

    def pause(self) -> None:
        self.player.set_state(self.player.paused_state)
        print("Pause du média")


class PausedState(MediaState):
    def __init__(self, player : MediaPlayer) -> None:
        self.player = player

    def play(self) -> None:
        self.player.set_state(self.player.playing_state)
        print("Reprise de la lecture du média")

    def pause(self) -> None:
        print("Le média est déjà en pause")


class MediaPlayer:
    def __init__(self) -> None:
        self.playing_state = PlayingState(self)
        self.paused_state = PausedState(self)
        
        self.state : MediaState = self.paused_state
        
    def set_state(self, state : MediaState) -> None:
        self.state = state
        
    def play(self) -> None:
        self.state.play()
        
    def pause(self) -> None:
        self.state.pause()
        
        
if __name__ == '__main__':
    player = MediaPlayer()
    
    player.pause()
    player.play()
    player.pause()