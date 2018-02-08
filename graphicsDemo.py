#Matt Westelman
#2/7/18
#graphicsDemo.py - Intro to game

from ggame import *

red = Color(0xFF0000,1) #this is the color red
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1) #Black

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(200,100,blackOutline,red) #Width, height, outline and fill
blueCircle = CircleAsset(50,blackOutline,blue) #Radius, outline, fill
greenEllipse = EllipseAsset(100, 50, blackOutline, green) #Width, height, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(0,0), (120,180), (60,300)], blackOutline,red) #endpoints, outline, fill
text = TextAsset(">Current Year",fill=green, style='bold 40pt Times') #Green texting like 4Chan

Sprite(redRectangle)
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,400))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(100,100))
App().run()
