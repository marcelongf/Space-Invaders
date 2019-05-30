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
dir_inimigos = 1
ultimo_inimigo = 2

ultima_checagem_fps = 1

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
        if ultimo_tiro >= tiro_cd(dificuldade):
            tiro = Sprite('./images/tiro.png')
            tiro.x = nave.x + nave.width/2 - tiro.width/2
            tiro.y = janela.height - nave.height
            tiros.append(tiro)
            ultimo_tiro = 0

def tiros_fora_da_tela():
    for tiro in tiros:
        if tiro.y <= 0:
            tiros.remove(tiro)

def cria_inimigos():
    for i in range(3):
        linha = []
        for j in range(6):
            inimigo = Sprite('inimigo.png')
            inimigo.y = i * inimigo.height
            inimigo.x = j * inimigo.width
            linha.append(inimigo)
        inimigos.append(linha)

def desenha_inimigos():
    for linha in inimigos:
        for inimigo in linha:
            inimigo.draw()

def checa_inimigos():
    c = 0
    for linha in inimigos:
        for inimigo in linha:
            if inimigo != None:
                c += 1
    if c == 0:
        cria_inimigos()

def checa_fps():
    if ultima_checagem_fps >= 1:
        fps = 1/janela.delta_time()

def maior_x():
    maior = 0
    for linha in inimigos:
        for inimigo in linha:
            if inimigo.x > maior:
                maior = inimigo.x
    return maior

def menor_x():
    menor = janela.width
    for linha in inimigos:
        for inimigo in linha:
            if inimigo.x < menor:
                menor = inimigo.x
    return menor

def mata_inimigos():
    for linha in inimigos:
        for inimigo in linha:
            for tiro in tiros:
                if tiro.x < maior_x() and tiro.x > menor_x():
                    if inimigo.collided(tiro):
                        tiros.remove(tiro)
                        inimigo = None

def esbarra():
    for linha in inimigos:
        for inimigo in linha:
            if inimigo.x >= janela.width or inimigo.x <= 0:
                return True
    return False

def movimenta_inimigos():
    if esbarra():
        dir_inimigos *= -1
        for linha in inimigos:
            for inimigo in linha:
                inimigo.y += 30
    for linha in inimigos:
        for inimigo in linha:
            inimigo.x += 10 * dir_inimigos
    
            
                

def jogo(dificuldade):
    global ultimo_tiro, ultimo_inimigo

    movimento_nave()
    checa_tiro()
    checa_inimigos()
    movimenta_inimigos()
    mata_inimigos()

    #desenha todos objetos
    nave.draw()
    for tiro in tiros:
        tiro.y -= 1
        tiro.draw()
    desenha_inimigos()
    
    #atualizações finais
    ultimo_tiro += janela.delta_time()
    ultimo_inimigo += janela.delta_time()
    ultima_checagem_fps += janela.delta_time()
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

