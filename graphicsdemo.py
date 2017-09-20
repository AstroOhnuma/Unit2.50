#Astro Ohnuma
#9/20/17
#graphicsdemo.py - intro to ggame

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackoutline = LineStyle(1,black) #pixels, color

redrectangle = RectangleAsset(200,100,blackoutline,red) #width, height, outline, fill
bluecircle = CircleAsset(50,blackoutline,blue) #radius, outline, fill
greenellipse = EllipseAsset(100,50,blackoutline,green) #horiz_radius, vertical_radius, outline, fill
blackline = LineAsset(50,160,blackoutline)#x_endpoint, y_endpoint, lineStyle
redtriangle = PolygonAsset([(0,0), (120,180), (60,300)], blackoutline, red) #list of endpoints, outline, fill
text = TextAsset('Astro',fill=green,style='bold 40pt Times')

Sprite(redrectangle)
Sprite(bluecircle,(50,50))
Sprite(greenellipse, (200,400))
Sprite(blackline)
Sprite(redtriangle)
Sprite(text,(300,200))
App().run()
