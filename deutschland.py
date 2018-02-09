#Matt Westelman
#2/9/18
#deutschland.py - German Flag

from ggame import *

red = Color(0xFF0000,1) #this is the color red
green = Color(0x00FF00,1)#green
blue = Color(0x0000FF,1) #blue
black = Color(0x000000,1) #Black
maple = Color(0xD2691E,1) #maplewood
aqua = Color(0x00FFFF,1) #Aqua
yellow = Color(0xFFFF00,1) #yellow

blackOutline = LineStyle(1,black)
yellowOutline= LineStyle(1,yellow)
redOutline= LineStyle(1,red)

redRectangle = RectangleAsset(450,100,redOutline,red) #Width, height, outline and fill
orangeRectangle = RectangleAsset(10,20,blackOutline, maple) #DOOR
blueCircle = CircleAsset(50,blackOutline,blue) #Radius, outline, fill
greenEllipse = EllipseAsset(100, 50, blackOutline, green) #Width, height, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
blueTriangle = PolygonAsset([(30,30), (60,52), (0,52)], blackOutline,blue) #endpoints, outline, fill
aquaRectangle = RectangleAsset(10,10,blackOutline,aqua)
blackRectangle = RectangleAsset(450,100,blackOutline,black)
yellowRectangle = RectangleAsset(450,100,yellowOutline,yellow)

text = TextAsset("Deutschland!",fill=green, style='bold 40pt Times') #Green texting like we are on 4chan

Sprite(text, (600,0))
Sprite(blackRectangle, (0,0))
Sprite(yellowRectangle, (0,200))
Sprite(redRectangle,(0,100))
