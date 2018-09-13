import pygame
import Quebra

#Definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# -- bloco principal
pygame.init()
largura = 600
altura = 400
tela = pygame.display.set_mode([largura, altura])
tela.fill((255, 255, 255))
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris magna enim, faucibus convallis ultricies vitae, rhoncus sit amet erat. Integer egestas tincidunt venenatis. Maecenas facilisis eleifend varius. Sed venenatis orci vel orci finibus consectetur. Proin interdum ex sed arcu mollis, non dignissim nunc pharetra. Nunc fermentum mauris sed nibh facilisis, in feugiat justo malesuada. Proin non nunc lobortis, ultrices nunc sed, dignissim diam."
fonteJogo = pygame.font.SysFont("Arial", 12)
rect = pygame.Rect([10, 10, 300, 600])


rendered_text = Quebra.render_textrect(texto, fonteJogo, rect, (216, 216, 216), (48, 48, 48), 0)

if rendered_text:
    tela.blit(rendered_text, rect.topleft)

    pygame.display.update()

while (True):
    # pega um evento na lista de eventos pendentes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()



