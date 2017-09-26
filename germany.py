#Astro Ohnuma
#9/22/17
#germany.py - Making the german flag with ggame graphics

from ggame import *

black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)
red = Color(0xFF0000,1)

blackoutline = LineStyle(1,black)
yellowoutline = LineStyle(1,yellow)
redoutline = LineStyle(1,red)

blackrectangle = RectangleAsset(300,50,blackoutline,black)
redrectangle = RectangleAsset(300,50,redoutline,red)
yellowrectangle = RectangleAsset(300,50,yellowoutline,yellow)

Sprite(blackrectangle,(100,100))
Sprite(redrectangle, (100,150))
Sprite(yellowrectangle,(100,200))
App().run()