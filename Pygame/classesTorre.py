import pygame

pygame.init()


torreGuer = "torreGuerreiro.png"
torreArq = "torreArqueiro.png"
torreMag = "torreMago.png"

tGuer = pygame.image.load(torreGuer)
tArq = pygame.image.load(torreArq)
tMag = pygame.image.load(torreMag)

#Nos danos, a torre com vantagem causa 20% de dano da vida total da classe de ataque,
# enquanto contra sua fraqueza causa 5% e o dano m�dio � 10% e o dano em catapultas sempre � 25

#Torre Arqueiro
vidaTA = 125
TAdA = 20
TAdG = 6
TAdM = 8
TAdC = 30

#Torre Guerreiro
vidaTG = 125
TGdA = 10
TGdG = 24
TGdM = 4
TGdC = 30

#Torre Mago
vidaTM = 125
TMdA = 5
TMdG = 12
TMdM = 16
TMdC = 30

#balanceamento, classes de ataque podem atacar torres
    #classe atk Guerreiro
GdanoATorreArq = 35
GdanoATorreGuer = 15
GdanoATorreMag = 25
    #classe atk Arqueiro
AdanoATorreArq = 15
AdanoATorreGuer = 25
AdanoATorreMag = 35
    #classe atk Mago
MdanoATorreArq = 25
MdanoATorreGuer = 35
MdanoATorreMag = 15


torreArq = "guerreiro.png"
toArq = pygame.image.load(torreArq)

class TorreArqueiro:
    def __init__(self):
        self.vida = vidaTA
        self.dano = 0

    def atacarArqueiro(self):
        self.dano = TAdA
        return self.dano

    def atacarGuerreiro(self):
        self.dano = TAdG
        return self.dano

    def atacarMago(self):
        self.dano = TAdM
        return self.dano

    def atacarCatapulta(self):
        self.dano = TAdC
        return self.dano

    def danoT(self,dan):
        self.vida -= dan

    def serAtkBalanceamento(self,tipo):
        if tipo == 1:
            self.vida -= GdanoATorreArq

        elif tipo == 2:
            self.vida -= AdanoATorreArq

        elif tipo == 3:
            self.vida -= MdanoATorreArq


class TorreGuerreiro:
    def __init__(self):
        self.vida = vidaTG
        self.dano = 0

    def atacarArqueiro(self):
        self.dano = TGdA
        return self.dano

    def atacarGuerreiro(self):
        self.dano = TGdG
        return self.dano

    def atacarMago(self):
        self.dano = TGdM
        return self.dano

    def atacarCatapulta(self):
        self.dano = TGdC
        return self.dano

    def danoT(self,dan):
        self.vida -= dan

    def serAtkBalanceamento(self, tipo):
        if tipo == 1:
            self.vida -= GdanoATorreGuer

        elif tipo == 2:
            self.vida -= AdanoATorreGuer

        elif tipo == 3:
            self.vida -= MdanoATorreGuer


class TorreMago:
    def __init__(self):
        self.vida = vidaTM
        self.dano = 0

    def atacarArqueiro(self):
        self.dano = TMdA
        return self.dano

    def atacarGuerreiro(self):
        self.dano = TMdG
        return self.dano

    def atacarMago(self):
        self.dano = TMdM
        return self.dano

    def atacarCatapulta(self):
        self.dano = TMdC
        return self.dano

    def danoT(self,dan):
        self.vida -= dan

    def serAtkBalanceamento(self, tipo):
        if tipo == 1:
            self.vida -= GdanoATorreMag

        elif tipo == 2:
            self.vida -= AdanoATorreMag

        elif tipo == 3:
            self.vida -= MdanoATorreMag


#Retorna o tipo de torre, 1= Torre guerreiro, 2= Torre Arqueiro, 3= Torre Mago
def tipoTorre(tipo):
    if tipo == 1:
        return TorreGuerreiro()

    elif tipo == 2:
        return TorreArqueiro()

    else:
        return TorreMago()

def imagemTorre(tipo):
    if tipo == 1:
        return tGuer

    elif tipo == 2:
        return tArq

    else:
        return tMag
