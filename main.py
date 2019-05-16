from PPlay.window import *
import menu as menu
import modo as modo
from PPlay.sprite import *
from random import randint

janela = Window(600,600)
janela.set_title("Space Invaders")

teclado = Window.get_keyboard()

game_state = 0
dificuldade = 1

nave = Sprite('./images/nave.png')
nave.y = janela.height - nave.height
nave.x = 0

tiros = []
ultimo_tiro = 1

inimigos = []
ultimo_inimigo = 2

def tiro_cd(dificuldade):
    if dificuldade == 1:
        return 0.2
    if dificuldade == 2:
        return 0.3
    if dificuldade == 3:
        return 0.5

def inimigo_cd(dificuldade):
    if dificuldade == 1:
        return 3
    if dificuldade == 2:
        return 2
    if dificuldade == 3:
        return 1.5

def movimento_nave():
    if teclado.key_pressed("LEFT"):
        nave.x -= 0.2
    if teclado.key_pressed("RIGHT"):
        nave.x += 0.2

def checa_tiro():
    global ultimo_tiro

    if teclado.key_pressed("SPACE"):
        if ultimo_tiro >= tiro_cd():
            tiro = Sprite('./images/tiro.png')
            tiro.x = nave.x + nave.width/2 - tiro.width/2
            tiro.y = janela.height - nave.height
            tiros.append(tiro)
            ultimo_tiro = 0

def tiros_fora_da_tela():
    for tiro in tiros:
        if tiro.y <= 0:
            tiros.remove(tiro)


def cria_inimigo():
    global ultimo_inimigo

    if ultimo_inimigo > inimigo_cd(dificuldade):
        for i in range(dificuldade):
            inimigo = Sprite('./images/inimigo.png')
            inimigo.x = randint(0, janela.width - inimigo.width)
            inimigo.y = 0
            inimigos.append(inimigo)
        ultimo_inimigo = 0    

def mata_inimigos():
    for inimigo in inimigos:
        for tiro in tiros:
            if inimigo.collided(tiro):
                tiros.remove(tiro)
                inimigos.remove(inimigo)
            
                

def jogo(dificuldade):
    global ultimo_tiro, ultimo_inimigo

    movimento_nave()
    checa_tiro()
    cria_inimigo()
    mata_inimigos()

    #desenha todos objetos
    nave.draw()
    for tiro in tiros:
        tiro.y -= 1
        tiro.draw()
    for inimigo in inimigos:
        inimigo.y += 0.1
        inimigo.draw()
    
    #atualizações finais
    ultimo_tiro += janela.delta_time()
    ultimo_inimigo += janela.delta_time()
    tiros_fora_da_tela()


while True:
    if game_state == 0:
        game_state = menu.menu(janela)
    if game_state == 2:
        dificuldade = modo.modo(janela)
        game_state = 0
    if game_state == 1:
        janela.set_background_color((0,0,0))
        if teclado.key_pressed("ESC"):
            game_state = 0
    jogo(dificuldade)

    janela.update()

