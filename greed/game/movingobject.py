class MovingObject:
    """
    MovingObject class - all moving objects on the screen inherit from this class
    """
    def __init__(self, x, y):
        # Set initial Variables
        self.center = Point(x,y)
        self.velocity = Velocity()
        self.alive = True


    def advance(self):
        # Advance the moving object
        
        # x component
        self.center.x += self.velocity.dx
        
        # y component
        self.center.y += self.velocity.dy

