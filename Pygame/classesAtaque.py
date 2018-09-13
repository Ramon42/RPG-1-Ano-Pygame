#Arqueiro
vidaA = 100
danoAoCastA = 40

#Guerreiro
vidaG = 120
danoAoCastG = 30

#Mago
vidaM = 80
danoAoCastM = 50

#Catapulta
vidaC = 125
danoATorre = 45
danoAoCastC = 10

#classe que cria uma lista de objetos que são os ataques, armazenando suas vidas e o tipo correspondente
class ArmazenarAtk:
    def __init__(self):
        self.lista = []

    def criarAtk(self,obj):
        self.lista.append(obj)

#pos = nas classes armazena a posição de objetos, 0 = campo neutro, 1 = casa 1, 2 = casa 2 e 3 = casa 3

class Guerreiro:
    def __init__(self):
        self.tipo = 1
        self.vida = vidaG
        self.danoAoCast = danoAoCastG
        self.danoT = 0
        self.pos = 0

    def atacarCasteloG(self):
        return self.danoAoCast

class Arqueiro:
    def __init__(self):
        self.tipo = 2
        self.vida = vidaA
        self.danoAoCast = danoAoCastA
        self.danoT = 0
        self.pos = 0

    def atacarCasteloA(self):
        return self.danoAoCast


class Mago:
    def __init__(self):
        self.tipo = 3
        self.vida = vidaM
        self.danoAoCast = danoAoCastM
        self.danoT = 0
        self.pos = 0

    def atacarCasteloM(self):
        return self.danoAoCast


class Catapulta:
    def __init__(self):
        self.tipo = 4
        self.vida = vidaC
        self.danoAoCast = danoAoCastC
        self.danoT = danoATorre
        self.pos = 0

    def atacarCasteloC(self):
        return self.danoAoCast

    def atacarTorre(self):
        return self.danoT
