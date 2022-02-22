class Velocity:
    """
    Velocity Class - handles moving object movement
    """
    def __init__(self, dx, dy):
        """
        Sets up initial values for speed(dx) and direction(dy) of the moving object
        """
        self._dx = dx  # Starting speed of 0
        self._dy = dy  # Starting speed of -1 (falling)

    def get_dx(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._dx

    def get_dy(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._dy

    def set_dx(self, dx):
        """Sets the horizontal distance.
        
        """
        self._dx = dx

    def set_dy(self, dy):
        """Sets the vertical distance.
        
        """
        self._dy = dy
        
    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Velocity that is scaled.
        """
        return Velocity(self._dx * factor, self._dy * factor) 

