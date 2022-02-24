class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the players position and resolves any collisions with rocks or gems.
        
        Args:
            cast (Cast): The cast of actors.
        """
        score = cast.get_first_actor("score")
        player = cast.get_first_actor("player")
        artifacts = cast.get_actors("artifacts")
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")
        # player.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for rock in rocks:
            if player.get_position().equals(rock.get_position()):
                player.score_rock()
                score.set_text("Score: " + str(player.get_score()))
                cast.remove_actor("rocks", rock)  
            rock.move_next(max_x, max_y)
        for gem in gems:
            # player_position = str(player.get_position())
            # print(player.)
            # bottom_range  = player_position - 5
            # top_range  = player_position + 5
            # gem_position = gem.get_position()
            if player.get_position().equals(gem.get_position()):
            # if gem_position in range(bottom_range, top_range):
                player.score_gem()
                score.set_text("Score: " + str(player.get_score()))
                cast.remove_actor("gems", gem)  
            gem.move_next(max_x, max_y)
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
