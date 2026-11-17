import pygame as pg

# Inicialização do Pygame, definição da tela, titulo e relogio
pg.init()
screen = pg.display.set_mode((800, 700))
pg.display.set_caption("Night Sky")
clock = pg.time.Clock()

# Definição dos valores iniciais para os cometas x e y, e a fonte para exibir o texto na tela
comet_x = 0
comet_y = 100
font = pg.font.SysFont("Roboto", 24)
# font = pg.font.Font("None", 19)

# Mensagem de boas-vindas para o usuário 
print("Good night! Welcome to the night sky simulation. watch the comets and stars move across the sky. Press the close button to exit the simulation.")

# Definindo a variável de controle do loop principal do jogo
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Definindo a cor do cometa com base na posição x do cometa, e atualizando a posição dos cometas e verificando se eles saíram da tela
    if comet_x < 200:
        colour = (255, 255, 255)
    elif comet_x < 400:
        colour = (255, 255, 0)
    else:
        colour = (255, 0, 0)

    # Atualizando a posição dos cometas e verificando se eles saíram da tela
    comet_x += 3
    if comet_x > 700:
        comet_x = -60
    # Atualizando a posição do cometa vermelho e verificando se ele saiu da tela
    comet_y += 2.5
    if comet_y > 700:
        comet_y = 40

    # Desenhando o fundo, os cometas e as estrelas na tela, screen, cor, posição, tamanho, comet_x, comet_y, são as coordenadas atualizadas dos cometas, e o texto exibindo a posição do cometa na tela
    screen.fill((20, 24, 48))
    pg.draw.circle(screen, (240, 230, 160), (500, 110), 80)
    pg.draw.circle(screen, colour, (comet_x, 300), 10) 
    pg.draw.circle(screen, (255, 0, 0), (350, comet_y), 10)
    # pg.draw.circle(screen, (0, 0, 100), (comet_x, comet_y), 50)
    # pg.draw.circle(screen, (255, 255, 255), (comet_x + 20, comet_y - 20), 4)
    # pg.draw.circle(screen, (255, 255, 255), (comet_x * 3, comet_y - 350), 4)

    pg.draw.circle(screen, (240, 230, 160), (50, 110), 5)
    pg.draw.circle(screen, (240, 230, 160), (90, 60), 8)
    pg.draw.circle(screen, (240, 230, 160), (350, 90), 3)
    pg.draw.circle(screen, (240, 230, 160), (400, 230), 4)
    pg.draw.circle(screen, (240, 230, 160), (250, 150), 4)

    # POE para o usuário controlar a posição do cometa vermelho usando as teclas de seta do teclado, e atualizando a posição do texto exibindo a posição do cometa na tela, K_LEFT, K_RIGHT, K_UP, K_DOWN são as teclas de seta do teclado, e o texto exibindo a posição do cometa na tela é atualizado com a função render da fonte definida anteriormente

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        comet_x -= 4
    elif keys[pg.K_RIGHT] and comet_x < 580:
        comet_x += 4 

    if keys[pg.K_UP]:
        comet_y -= 4
    elif keys[pg.K_DOWN]:
        comet_y += 4

    # Renderizando o texto na tela com a posição atual do cometa, e exibindo o texto na tela usando a função blit da tela, e atualizando a tela com a função flip da tela, e limitando a taxa de atualização da tela para 60 quadros por segundo com a função tick do relogio
    texto =  font.render(f"Comet Position: ({comet_x}, {comet_y})", True, (255, 205, 155))
    screen.blit(texto, (comet_x - 40, 325))

    # Atualizando a tela e limitando a taxa de atualização da tela para 60 quadros por segundo
    pg.display.flip()
    clock.tick(60)

# Encerrando o Pygame
pg.quit()