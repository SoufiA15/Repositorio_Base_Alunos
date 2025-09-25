import pygame 

pygame.init()
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
clock = pygame.time.Clock()

x = 50 
y = 50 
velocidade_x = 5
velocidade_y = 5
largura_ret, altura_ret = 50,50 

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame. QUIT:
            rodando = False
    x += velocidade_x 
    y += velocidade_y 

    if x + largura_ret > LARGURA_TELA or x < 0:
        velocidade_x = -velocidade_x
    if y + largura_ret > ALTURA_TELA or y < 0: 
        velocidade_y = -velocidade_y

    tela.fill((0,0,0))
    pygame.draw.rect(tela, (255,0,0), (x,y,largura_ret, altura_ret))
    pygame.display.update()
    clock.tick(60)

pygame.quit()