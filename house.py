#Astro Ohnuma
#9/20/17
#house.py - making a house with ggame shapes

from ggame import *

red = Color(0xFF0000,1)
tan = Color(0xFFB266,1)
blue = Color(0x0080FF,1)
black = Color(0x000000,1)

blackoutline = LineStyle(1,black)

roof = PolygonAsset([(60,120), (240,120), (150,60)], blackoutline, red)
house = RectangleAsset(180,100, blackoutline, tan)
window = RectangleAsset(40,40, blackoutline, blue)
window2 = RectangleAsset(40,40, blackoutline, blue)
door = RectangleAsset(40,60, blackoutline, red)

Sprite(roof)
Sprite(house, (60,120))
Sprite(window, (70,130))
Sprite(window2, (190,130))
Sprite(door, (130,160))
App().run()