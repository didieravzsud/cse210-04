from screen import *
from player import *
from score import *

class Director: 
    
    def __init__(self):
        self._screen = Screen()
        # self.total_score = 0
        
    def start_game(self):
        self._screen.open_window()
        while self._screen.is_window_open():
            self._get_inputs()
            self._do_updates()
        self._screen.close_window()
        
    def _get_inputs(self):
        pass
    
    def _do_updates(self):
        # for _ in x:
        if player.get_position().equals(rocks.get_position()):
            score.self.total_score = score.subtract_score()
        elif player.get_position().equals(gems.get_position()):
            score.self.total_score = score.add_score()
            
