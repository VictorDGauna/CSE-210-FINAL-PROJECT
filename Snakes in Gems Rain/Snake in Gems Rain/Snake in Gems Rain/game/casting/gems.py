import random
from game.casting.actor import Actor;
from game.shared.color import Color;
from game.shared.point import Point;
from secrets import choice
import constants

class Gems(Actor):

    """
        A Gems. This class inherits from Actor.        
    """

    def __init__(self):


        #Call the parent init
        super().__init__()

        #set the look of the gems or rocks
        char = [42,176]
        text = chr(choice(char))
        super().set_text(text)

        #set the points for gems, adding a point for each gem hit.
        if text == chr(42):
#            Point().set_points(+1)
            color = Color(0,0,255)
            super().set_color(color)
        else:
     #       Point().set_points(-1)
            color = Color(255,0,0)
            super().set_color(color)
        #Set Velocity with parent set_text method
        speed = random.randrange(1,16)
        super().set_velocity(Point(0,speed))
    
       

