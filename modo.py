from PPlay.window import *
from PPlay.gameimage import *


def scrolling(bg_bottom, bg_top, roll_speed, janela):

    bg_bottom.y += roll_speed * janela.delta_time()
    bg_top.y += roll_speed * janela.delta_time()
    if bg_top.y >= 0:
        bg_bottom.y = 0
        bg_top.y = -bg_top.height

    janela.set_background_color((0,0,0))
    bg_bottom.draw()
    bg_top.draw()


def modo(janela):
    mouse = Window.get_mouse()
    facil = GameImage("images/facil.png")
    medio = GameImage("images/medio.png")
    dificil = GameImage("images/dificil.png")

    facil.x = janela.width/2 - facil.width/2
    facil.y = janela.height/4 - facil.height/2
    medio.x = facil.x
    medio.y = facil.y + facil.height
    dificil.x = facil.x
    dificil.y = medio.y + medio.height
    estaPressionado = True
    while True:
        if mouse.is_button_pressed(1) == False:
            estaPressionado = False
        if estaPressionado == False:
            facil.draw()
            medio.draw()
            dificil.draw()
            if mouse.is_over_object(facil) and mouse.is_button_pressed(1):
                return 1
            if mouse.is_over_object(medio) and mouse.is_button_pressed(1):
                return 2
            if mouse.is_over_object(dificil) and mouse.is_button_pressed(1):
                return 3
        janela.update()
