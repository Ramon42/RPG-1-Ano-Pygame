import pygame

pygame.init()
#CORES
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)


pygame.font.init()
fonte = pygame.font.SysFont('Arial', 15)
texto = fonte.render('Olá mundo!', 1, VERMELHO)
campo = "campo.png"
cobraAndando = "cobraAndando.png"
pikachu = "torre.png"
background = pygame.image.load(campo)
cobra = pygame.image.load(cobraAndando)
pik = pygame.image.load(pikachu)



largura = 1280
altura = 720
tela = pygame.display.set_mode([largura,altura])

x = 0

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tela.blit(background, (0,0))
    tela.blit(pik, (x, 100))
    tela.blit(texto, (100, 100)) #Perguntas
    x += 1
    if x > largura:
        x -= 1000

    pygame.display.update()
