#Vida
vidaCast = 200

#Dano que causa à todos os ataques à sua frente
danoAoAtk = 5

#Dano sofrido de cada classe
danoSofridoArq = 40
danoSofridoGuer = 50
danoSofridoMag = 30
danoSofridoCat = 10

class Castelo():
    def __init__(self):
        self.vida = vidaCast
        self.danoCausado = danoAoAtk

    def danoArq(self):
        self.vida -= danoSofridoArq
        return self.vida

    def danoGuer(self):
        self.vida -= danoSofridoGuer
        return self.vida

    def danoMag(self):
        self.vida-= danoSofridoMag
        return self.vida

    def danoCat(self):
        self.vida -= danoSofridoCat
        return self.vida

    def dano(self,dan):
        self.vida -= dan