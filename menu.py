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


def menu(janela):

    mouse = Window.get_mouse()

    
    roll_speed = 300
    play = GameImage("images/play.png")
    dificuldades = GameImage("images/dificuldades.png")
    quit = GameImage("images/quit.png")
    ranking = GameImage("images/ranking.png")

    play.x = janela.width/2 - play.width/2
    play.y = janela.height/5 - play.height/2
    dificuldades.x = play.x
    dificuldades.y = play.y + play.height
    ranking.x = play.x
    ranking.y = dificuldades.y + dificuldades.height
    quit.x = play.x
    quit.y = ranking.y + ranking.height

    estaPressionado = True
    while True:
        if mouse.is_button_pressed(1) == False:
            estaPressionado = False
        if estaPressionado == False:
            if mouse.is_over_object(play) and mouse.is_button_pressed(1):
                return 1
            if mouse.is_over_object(dificuldades) and mouse.is_button_pressed(1):
                return 2

            if mouse.is_over_object(quit) and mouse.is_button_pressed(1):
                janela.close()
            play.draw()
            dificuldades.draw()
            ranking.draw()
            quit.draw()
        janela.update()
