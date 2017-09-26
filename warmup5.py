#Astro Ohnuma
#9/26/17
#warmup5.py - making a yellow diamond with our name inside in blue

from ggame import *
yellow = Color(0xFFFF00,1)
black = Color(0x000000,1)
blue = Color(0x0000FF,1)

blackoutline = LineStyle(1,black)
yellowoutline = LineStyle(1,yellow)

yellowdiamond1 = PolygonAsset([(100,100), (150,50), (200,100)], yellowoutline, yellow)
yellowdiamond2 = PolygonAsset([(100,100), (150,150), (200,100)], yellowoutline, yellow)
name = TextAsset('Astro',fill=blue, style='bold 60pt')

Sprite(yellowdiamond1)
Sprite(yellowdiamond2)
Sprite(name, (135, 95))
App().run()