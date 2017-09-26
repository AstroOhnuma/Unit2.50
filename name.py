#Astro Ohnuma
#9/26/17
#name.py - asking for a name and a color code and then putting that name on a background of that color

from ggame import *
name = input('Enter your name: ')
colorcode = input('Enter an RGB color code: ')

color = Color(colorcode,1)
black = Color(0x000000,1)

blackoutline = LineStyle(1,black)

background = RectangleAsset(1400,600,blackoutline,color)
text = TextAsset(name,fill=black,style='bold 60pt Times')

Sprite(background, (0,0))
Sprite(text, (575,200))
App().run()