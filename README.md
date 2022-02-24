# cse210-04

 Greed Game 

 A game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

 Specifications

 Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
 The player (#) can move left or right along the bottom of the screen.
 If the player touches a gem they earn a point.
 If the player touches a rock they lose a point.
 Gems and rocks are removed when the player touches them.
 The game continues until the player closes the window..

# Extra Functionality

1. We have added additional classes to represent the following object:
	a. Emerald - represented by letter "E" and scores +2
	b. Ruby - represented by letter "R" and scores +5
	c. Diamond - represented by letter "D" and scores +10
	d. TNT - represented by character "!" and scores -10
2. We have added a cave represented by the letter "C". If the user catches the cave, 5 more rocks and 5 more gems are created in the game.  The cave is never removed and can be visited when ever the user desires.
3. We added an end of game congratulations.  When all gems, emeralds, rubies, and diamonds are collected, the user receives a special message.
4. We have added more flexibility to the player.  He can now come up from the bottom a short distance to find gems.

# Files

__main__.py
director.py
actor.py
cast.py
rock.py
gem.py
player.py
point.py
velocity.py
color.py
keyboard_service.py
video_service.py

# Classes

classes: 
	main (JAKE)
	Director (JAKE)
		-play game
		-call score if player touches object
		-creates a loop to refresh screen
		-load screen

	Point (MARK)
		-moves position down along y-axis

	Velocity (MARK)
		-sets random speed of falling object

	VideoService(DIDIER)
		-load screen
		-display score, falling objects and player

	Score  (DIDIER)
		-add a point
		-loss a point

	Player (inherits from Actor) (JOHANNA)
        Keyboard-service (JOHANNA)
		-create player
		-take input from the keyboard		
		-calls leftwards movement when press left arrow key
		-calls rightwards movement when press right arrow key

	Rock  (ALEXANDER)
		-create rock
		-spawn rock in random x-axis location

	Gem  (ALEXANDER)
		-create gem
		-spawn gem in random x-axis location

	Actor (MARK)
		-moves one to the right
		-moves one to the left
		-moves one down the y-axis
		-assign random color
	
	Cast – collect of moving objects (Mark)

# Team

Alexander Calva
Mark Richmond
Johanna Schick
Jake Soulier
Didier Virguez


