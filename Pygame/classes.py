import pygame
import random
import classesTorre

pygame.init()
pygame.font.init()
largura = 1280
altura = 720
tela = pygame.display.set_mode([largura, altura])

#CORES
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CINZA = (105, 105, 105)
fonte = pygame.font.SysFont('ARIAL', 36)
fontePerg = pygame.font.SysFont('ARIAL', 18)


#Blocos de botão
class Bloco(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura):
        super().__init__()    #chama o construtor da superclasse
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()    # pega coordenadas

    def posicionar(self, x=10, y=10):
        self.rect.x = x
        self.rect.y = y


#Retorna o indicador de turno, primeiro a Letra, depois a cor
def verTurnoLetra(turno):
    if turno == 0:
        return("V")
    elif turno == 1:
        return("A")
def verTurnoCor(turno):
    if turno == 0:
        return(VERMELHO)
    elif turno == 1:
        return(AZUL)

#Retorna a etapa de cada turno
def verEtapaLetra(etapa):
    if etapa == 0:
        return ("PERGUNTA")
    elif etapa == 1:
        return("POSICIONAMENTO")
    elif etapa == 2:
        return("MOVIMENTAÇÃO")


#Classes e funções das perguntas
class Perguntas: #Modelo para representar as perguntas
    def __init__(self):
        self.pe = ""
        self.alternativaA = ""
        self.alternativaB = ""
        self.alternativaC = ""
        self.alternativaD = ""
        self.resposta = ""

class ListaPerguntas: #Modelo para criar a lista 'lista', que armazenará os objetos contendo pergunta, alternativas e respostas
    def __init__(self):
        self.lista = []

    def adicionar(self,quest): #Cria o método 'adicionar', responsável por adicionar os objetos 'Perguntas' à lista
        self.lista.append(quest)

listar = ListaPerguntas()

def embaralhar(lista):
    random.shuffle(lista) #embaralha a lista de objetos

def compararRespostas(respostaEnviada,respostaCerta):
    if respostaEnviada == respostaCerta:
        return 1
    elif respostaEnviada != respostaCerta:
        return 0


