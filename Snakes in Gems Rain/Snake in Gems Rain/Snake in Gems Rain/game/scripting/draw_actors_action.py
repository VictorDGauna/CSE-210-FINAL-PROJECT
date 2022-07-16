from game.scripting.action import Action
from game.casting.gems import Gems 
from game.shared.point import Point
from game.casting.score import Score
from game.shared.color import Color
import random
import constants

MAX_GEM = 40
FONT_SIZE = 35
max_x = constants.MAX_X
max_y = constants.MAX_Y



class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service, Score):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._score = Score
    def _add_score(self, points):
        """
            Adds points to score
            Args: self - an instance of director,
                points to add
        """
        self._score += int(points)

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        segments = snake.get_segments()
        messages = cast.get_actors("messages")
        gems = cast.get_actors("gems")
        banner = cast.get_first_actor("banners")
        inst = Score()
        head = snake.get_head()
        
        

        cell_size = constants.CELL_SIZE
        p = max_x
        
        if len(gems) < MAX_GEM:
            if random.randrange(0,20) == 3:
                new_gem = Gems()
                new_gem.set_font_size(FONT_SIZE)
                
                column = int(constants.MAX_X / cell_size)
                location = Point(random.randrange(column)*cell_size,0)
                new_gem.set_position(location)
                cast.add_actor("gems",new_gem)   
                
                
        for gem in gems:

            #move the gem
            gem.move_next()
            y = gem.get_position().get_y()
            #Check for collision or reaching the bottom of the screen
            if head.get_position().closing(gem.get_position(), cell_size):
                if gem.get_text() == chr(42):
                    score.add_points(1)
                    cast.remove_actor("gems",gem)
                else:
                    score.add_points(-1)
                    cast.remove_actor("gems",gem)
            #remove the rock when it reaches the bottom of the screen
            elif y > constants.MAX_Y - cell_size:
                cast.remove_actor("gems",gem)
        
        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(gems)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
            
        # Update banner with score
       # banner.set_text(f"Score: {self._get_score()}")