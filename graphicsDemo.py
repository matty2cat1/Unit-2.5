#Matt Westelman
#2/7/18
#graphicsDemo.py - Intro to game

from ggame import *

red = Color(0xFF0000,1) #this is the color red
black = Color(0x000000,1) #Black

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(200,100,blackOutline,red) #Width, height, outline and fill

Sprite(redRectangle)
App().run()
