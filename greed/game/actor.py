# https://icons8.com/icon/pmO4gu1zMse3/jewel
import pygame, random

# This part is only for test
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)

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




pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Greed")
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

class Rocks(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(rock_images)
		self.image = random.choice(gems_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 :
			self.rect.x = random.randrange(WIDTH - self.rect.width)

			#Change this variable
			self.rect.y = random.randrange(-150, -100)
			self.speedy = random.randrange(1, 3)

class Gems(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(rock_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 :
			self.rect.x = random.randrange(WIDTH - self.rect.width)

			#Change this variable
			self.rect.y = random.randrange(-150, -100)
			self.speedy = random.randrange(1, 8)
rock_images = []
rock_list = ["game/assets/meteorGrey_big4.png",
				"game/assets/meteorGrey_med1.png", "game/assets/meteorGrey_med2.png", "game/assets/meteorGrey_small1.png", "game/assets/meteorGrey_small1.png",
				"game/assets/meteorGrey_small1.png", "game/assets/meteorGrey_small1.png"]

for img in rock_list:
	rock_images.append(pygame.image.load(img).convert())

gems_images = []
gems_list = ["game/assets/gems.png"]

for img in gems_list:
	gems_images.append(pygame.image.load(img).convert())

# Cargar fondo.
background = pygame.image.load("game/assets/background.png").convert()
all_sprites = pygame.sprite.Group()
rock_list = pygame.sprite.Group()
gems_list = pygame.sprite.Group()

for i in range(7):
	rock = Rocks()
	all_sprites.add(rock)
	rock_list.add(rock)
	gem = Gems()
	all_sprites.add(gem)
	gems_list.add(gem)

# Score
score = 0

# Game Loop
running = True
while running:
	# Keep loop running at the right speed
	clock.tick(60)
	# Process input (events)
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
	
	# Update
	all_sprites.update()

	#Draw / Render
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)

	# Marcador
	draw_text(screen, str(score), 25, WIDTH // 2, 10)
	pygame.display.flip()



