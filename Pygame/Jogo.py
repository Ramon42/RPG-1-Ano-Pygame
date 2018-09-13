# encoding: utf-8
import pygame
import classes
import classesAtaque
import classesTorre
import random
import classeCastelo
import Quebra


#CORES
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (105, 105, 105)
#

pygame.init()
pygame.font.init()

#fontes e textos predefinidos
fonte = pygame.font.SysFont('ARIAL', 36)
fontePerg = pygame.font.SysFont('ARIAL', 18)
fonteVidaTorres = pygame.font.SysFont('comicsansms',12)
textoAtk = fonte.render('ATAQUE', 1, CINZA)
textoDef = fonte.render('DEFESA', 1, CINZA)
#

#Iniciar perguntas e embaralhar
listaPerguntas = classes.ListaPerguntas()

#Lendo arquivo texto e adicionando à lista de perguntas
arq = open("pergunta.txt", 'r')  # Abre o arquivo 'pergunta.txt' para leitura e o armazena na variável 'arq'
ler = arq.readlines()  # Lê todas as linhas do arquivo salvo na variável 'arq' e o transforma em uma lista
o = 0
while o <= len(ler):  # Enquanto a variável de suporte 'o' for menor que o tamanho da lista o while será executado
    perguntas = classes.Perguntas()  # Cada vez que o while é iniciado, é instanciado um novo objeto "Perguntas" para
    # armazenar a pergunta, suas alternativas e sua resposta
    perguntas.pe = ler[o]  # Lê a posição(linha) 'o' do arquivo de texto, onde está a pergunta
    o += 1  # Pula para a próxima posição do arquivo de texto
    perguntas.alternativaA = ler[o]  # Lê a posição 'o' do arquivo de texto, onde está a alternativa A
    o += 1
    perguntas.alternativaB = ler[o]  # Lê a posição 'o' do arquivo de texto, onde está a alternativa B
    o += 1
    perguntas.alternativaC = ler[o]  # Lê a posição 'o' do arquivo de texto, onde está a alternativa C
    o += 1
    perguntas.alternativaD = ler[o]  # Lê a posição 'o' do arquivo de texto, onde está a alternativa D
    o += 1
    perguntas.resposta = ler[o]  # Lê a posição 'o' do arquivo de texto, onde está a resposta para a pergunta
    listaPerguntas.adicionar(perguntas)  # Executa o método "adicionar"
    o += 1
    o += 1

classes.embaralhar(listaPerguntas.lista)

pergunta = ''
alternativaA = ''
alternativaB = ''
alternativaC = ''
alternativaD = ''
respostaCerta = ''
respostaEnviada = ''

armazenarAtksV = classesAtaque.ArmazenarAtk() #instancia classe que contem uma lista de ataques em campo
armazenarAtksA = classesAtaque.ArmazenarAtk()

#Cria os dois objetos castelo
casteloVermelho = classeCastelo.Castelo()
casteloAzul = classeCastelo.Castelo()

#Adicionar imagens
campo = "campo.png"
bArqueiro = "bArq.png"
bGuerreiro = "bGuer.png"
bCatapulta = "bCat.png"
bMago = "bMag.png"
toArq = "bToArq.png"
toGuer = "bToGuer.png"
toMag = "bToMag.png"
stAtk = "statsAtk.png"
stDef = "statsDef.png"
selZonaDef = "selZonaDef.png"
alt = "alternativas.png"
guerreiro ="guerreiroT.png"
arqueiro = "arqueiroT.png"
mago = "magoT.png"
catapulta = "catapultaT.png"
azulVence = "azulGanhou.png"
vermelhoVence = "vermelhoGanhou.png"
#

#Carregar imagens
selecionarZDef = pygame.image.load(selZonaDef)
alternativas = pygame.image.load(alt)
background = pygame.image.load(campo)
botaoArq = pygame.image.load(bArqueiro)
botaoGuer = pygame.image.load(bGuerreiro)
botaoMag = pygame.image.load(bMago)
botaoCat = pygame.image.load(bCatapulta)
botaoToArq = pygame.image.load(toArq)
botaoToGuer = pygame.image.load(toGuer)
botaoToMag = pygame.image.load(toMag)
statsAtk = pygame.image.load(stAtk)
statsDef = pygame.image.load(stDef)
guer = pygame.image.load(guerreiro)
arq = pygame.image.load(arqueiro)
mag = pygame.image.load(mago)
cat = pygame.image.load(catapulta)
azulGanhou = pygame.image.load(azulVence)
vermelhoGanhou = pygame.image.load(vermelhoVence)
#

#Blocos abaixo dos botões para entender o click
listaSprites = pygame.sprite.Group()

#Bloco objeto Guerreiro
blocoGuer = classes.Bloco(PRETO, 107, 51)
blocoGuer.posicionar(18, 450)

#Bloco Arqueiro
blocoArq = classes.Bloco(PRETO, 107, 51)
blocoArq.posicionar(18,510)

#Bloco Mago
blocoMag = classes.Bloco(PRETO, 107, 51)
blocoMag.posicionar(18,570)

#Bloco Catapulta
blocoCat = classes.Bloco(PRETO, 107, 51)
blocoCat.posicionar(18,630)

#Blocos Torres
blocoToGuer = classes.Bloco(PRETO, 107, 51)
blocoToGuer.posicionar(875,450)
blocoToArq = classes.Bloco(PRETO, 107, 51)
blocoToArq.posicionar(875,510)
blocoToMag = classes.Bloco(PRETO, 107, 51)
blocoToMag.posicionar(875,570)

#Blocos Zona de Defesa
blocoZonaDefVermelho1 = classes.Bloco(PRETO, 120, 44)
blocoZonaDefVermelho1.posicionar(141, 272)

blocoZonaDefVermelho2 = classes.Bloco(PRETO, 120, 44)
blocoZonaDefVermelho2.posicionar(266, 272)

blocoZonaDefVermelho3 = classes.Bloco(PRETO, 120, 44)
blocoZonaDefVermelho3.posicionar(391, 272)

blocoZonaDefAzul1 = classes.Bloco(PRETO, 120, 44)
blocoZonaDefAzul1.posicionar(1021, 272)

blocoZonaDefAzul2 = classes.Bloco(PRETO, 120, 44)
blocoZonaDefAzul2.posicionar(896, 272)

blocoZonaDefAzul3 = classes.Bloco(PRETO, 120, 44)
blocoZonaDefAzul3.posicionar(771, 272)

#Blocos alternativas
blocoAlternativaA = classes.Bloco(BRANCO, 37, 37)
blocoAlternativaA.posicionar(510,680)

blocoAlternativaB = classes.Bloco(BRANCO, 37, 37)
blocoAlternativaB.posicionar(583,680)

blocoAlternativaC = classes.Bloco(BRANCO, 37, 37)
blocoAlternativaC.posicionar(656,680)

blocoAlternativaD = classes.Bloco(BRANCO, 37, 37)
blocoAlternativaD.posicionar(729,680)

#Define ataques estarem ou não em campo
    #Vermelho
guerreiroVZ = False
guerreiroV1 = False
guerreiroV2 = False
guerreiroV3 = False
arqueiroVZ = False
arqueiroV1 = False
arqueiroV2 = False
arqueiroV3 = False
magoVZ = False
magoV1 = False
magoV2 = False
magoV3 = False
catapultaVZ = False
catapultaV1 = False
catapultaV2 = False
catapultaV3 = False
    #
    #Azul
guerreiroAZ = False
guerreiroA1 = False
guerreiroA2 = False
guerreiroA3 = False
arqueiroAZ = False
arqueiroA1 = False
arqueiroA2 = False
arqueiroA3 = False
magoAZ = False
magoA1 = False
magoA2 = False
magoA3 = False
catapultaAZ = False
catapultaA1 = False
catapultaA2 = False
catapultaA3 = False
    #

#Define torres estarem ou não em campo
torreV1 = False
torreV2 = False
torreV3 = False
torreA1 = False
torreA2 = False
torreA3 = False
#

tipo = 0 #Serve tanto para ataque e defesa, cada classe possui um número para ser chamada
armazenaTipoTorreV1 = ''
armazenaTipoTorreV2 = ''
armazenaTipoTorreV3 = ''
armazenaTipoTorreA1 = ''
armazenaTipoTorreA2 = ''
armazenaTipoTorreA3 = ''

#Quem começa
comecar = [1, 2]
random.shuffle(comecar)
if comecar[0] == 1:
    turno = 0 #turno = 0 indica que é a vez do jogador vermelho
else:
    turno = 1 #turno = 1 indica que é a vez do jogador azul
#

#Separação de etapas
etapa = 0 #etapa = 0 corresponde à etapa de pergunta, 1 é a etapa de posicionamento e 2 a de movimentação

largura = 1280
altura = 720
tela = pygame.display.set_mode([largura, altura])

#Marcadores vida torres
marcadorVidaTorreA1 = 0
marcadorVidaTorreA2 = 0
marcadorVidaTorreA3 = 0
marcadorVidaTorreV1 = 0
marcadorVidaTorreV2 = 0
marcadorVidaTorreV3 = 0
#

tela.fill(BRANCO)
pygame.draw.line(tela, PRETO, [426, 358],[426, 720], 5)
pygame.draw.line(tela, PRETO, [852, 358],[852, 720], 5)

#retangulos para quebra de linha das perguntas
rectPerg = pygame.Rect([435, 370, 412, 78])
rectAltA = pygame.Rect([435, 480, 412, 45])
rectAltB = pygame.Rect([435, 525, 412, 45])
rectAltC = pygame.Rect([435, 570, 412, 45])
rectAltD = pygame.Rect([435, 615, 412, 45])

while (True):

    #Renderizar perguntas
    perg = Quebra.render_textrect(pergunta, fontePerg, rectPerg, PRETO, BRANCO, 0)
    alA = Quebra.render_textrect(alternativaA, fontePerg, rectAltA, PRETO, BRANCO, 0)
    alB = Quebra.render_textrect(alternativaB, fontePerg, rectAltB, PRETO, BRANCO, 0)
    alC = Quebra.render_textrect(alternativaC, fontePerg, rectAltC, PRETO, BRANCO, 0)
    alD = Quebra.render_textrect(alternativaD, fontePerg, rectAltD, PRETO, BRANCO, 0)

    vidaCastVermelho = fonte.render(str(casteloVermelho.vida), 1, VERMELHO)
    vidaCastAzul = fonte.render(str(casteloAzul.vida), 1, AZUL)

    # Indicadores, turno e etapa
    indicadorTurno = fonte.render(classes.verTurnoLetra(turno), 1, classes.verTurnoCor(turno))
    indicadorEtapa = fontePerg.render(classes.verEtapaLetra(etapa), 1, classes.verTurnoCor(turno))
    #

    tela.blit(background, (0, 0))
    tela.blit(alternativas,(510,680))

    #indicador vida torres
    marcadorA1 = fonteVidaTorres.render(str(marcadorVidaTorreA1), 1, PRETO)
    marcadorA2 = fonteVidaTorres.render(str(marcadorVidaTorreA2), 1, PRETO)
    marcadorA3 = fonteVidaTorres.render(str(marcadorVidaTorreA3), 1, PRETO)
    marcadorV1 = fonteVidaTorres.render(str(marcadorVidaTorreV1), 1, PRETO)
    marcadorV2 = fonteVidaTorres.render(str(marcadorVidaTorreV2), 1, PRETO)
    marcadorV3 = fonteVidaTorres.render(str(marcadorVidaTorreV3), 1, PRETO)
    #

    #Indicadores, turno e etapa
    tela.blit(indicadorTurno,(630, 258))
    tela.blit(indicadorEtapa, (575, 318))

    if turno == 0 and etapa == 1:
        tela.blit(selecionarZDef, (100, 225))
    elif turno == 1 and etapa == 1:
        tela.blit(selecionarZDef, (730, 225))
    #

    #Textos que mostram "ataque" e "defesa" na tela
    tela.blit(textoAtk,(157,380))
    tela.blit(textoDef,(1009,380))

    tela.blit(vidaCastVermelho,(50, 188))
    tela.blit(vidaCastAzul, (1185, 188))

    #Textos que dizem as vantagens de cada classe
    tela.blit(statsAtk,(128, 448))
    tela.blit(statsDef, (986, 448))

    #Caso a etapa seja = 0 (Pergunta) é dado um blit na pergunta e alternativas
    if etapa == 0:
        tela.blit(perg,rectPerg.topleft)
        tela.blit(alA,rectAltA.topleft)
        tela.blit(alB,rectAltB.topleft)
        tela.blit(alC,rectAltC.topleft)
        tela.blit(alD,rectAltD.topleft)

    #bloco para criar imagens de atk
        #Zona neutra vermelha
    if guerreiroVZ:
        tela.blit(guer,(592,134))
    if arqueiroVZ:
        tela.blit(arq,(530,73))
    if magoVZ:
        tela.blit(mag,(592,70))
    if catapultaVZ:
        tela.blit(cat,(525,142))

        #Vermelho casa 1
    if guerreiroV1:
        tela.blit(guer,(464,134))
    if arqueiroV1:
        tela.blit(arq,(402,73))
    if magoV1:
        tela.blit(mag,(464,70))
    if catapultaV1:
        tela.blit(cat,(399,142))

        #Vermelho casa 2
    if guerreiroV2:
        tela.blit(guer,(336,134))
    if arqueiroV2:
        tela.blit(arq,(274,73))
    if magoV2:
        tela.blit(mag,(336,70))
    if catapultaV2:
        tela.blit(cat,(273,142))

        #Vermelho casa 3
    if guerreiroV3:
        tela.blit(guer,(208,134))
    if arqueiroV3:
        tela.blit(arq,(146,73))
    if magoV3:
        tela.blit(mag,(208,70))
    if catapultaV3:
        tela.blit(cat,(147,142))

        #Zona neutra azul
    if guerreiroAZ:
        tela.blit(guer,(720,134))
    if arqueiroAZ:
        tela.blit(arq,(658,73))
    if magoAZ:
        tela.blit(mag,(720,70))
    if catapultaAZ:
        tela.blit(cat,(651,142))

        #azul casa 1
    if guerreiroA1:
        tela.blit(guer,(848,134))
    if arqueiroA1:
        tela.blit(arq,(786,73))
    if magoA1:
        tela.blit(mag,(848,70))
    if catapultaA1:
        tela.blit(cat,(777,142))

        #azul casa 2
    if guerreiroA2:
        tela.blit(guer,(976,134))
    if arqueiroA2:
        tela.blit(arq,(914,73))
    if magoA2:
        tela.blit(mag,(976,70))
    if catapultaA2:
        tela.blit(cat,(903,142))

        #azul casa 3
    if guerreiroA3:
        tela.blit(guer,(1104,134))
    if arqueiroA3:
        tela.blit(arq,(1042,73))
    if magoA3:
        tela.blit(mag,(1104,70))
    if catapultaA3:
        tela.blit(cat,(1028,142))


    #Bloco para criar imagens de torres
    if torreV1:
        tela.blit(armazenaTipoTorreV1,(175,245))
        tela.blit(marcadorV1, (190, 295))

    if torreV2:
        tela.blit(armazenaTipoTorreV2,(305,245))
        tela.blit(marcadorV2, (320, 295))

    if torreV3:
        tela.blit(armazenaTipoTorreV3,(425,245))
        tela.blit(marcadorV3, (440, 295))

    if torreA1:
        tela.blit(armazenaTipoTorreA1,(1055,245))
        tela.blit(marcadorA1, (1070, 295)) #caso a torre esteja em campo, seu marcador de vida é iniciado

    if torreA2:
        tela.blit(armazenaTipoTorreA2,(930,245))
        tela.blit(marcadorA2, (945, 295))

    if torreA3:
        tela.blit(armazenaTipoTorreA3,(805,245))
        tela.blit(marcadorA3, (820, 295))
     #

    tela.blit(botaoGuer, (18, 450))
    tela.blit(botaoArq, (18,510))
    tela.blit(botaoMag, (18,570))
    tela.blit(botaoCat, (18,630))
    tela.blit(botaoToGuer, (875,450))
    tela.blit(botaoToArq, (875,510))
    tela.blit(botaoToMag, (875,570))

    #Quem ganhou
    if casteloAzul.vida <= 0 and casteloVermelho.vida <= 0:
        print("Empate!")
        pygame.time.delay(2000)
        pygame.quit()
        exit()

    elif casteloAzul.vida <= 0:
        print("Jogador vermelho ganhou!")
        tela.blit(vermelhoGanhou,(0,0))

    elif casteloVermelho.vida <= 0:
        print("Jogador azul ganhou!")
        tela.blit(azulGanhou,(0,0))
    #

    listaSprites.draw(tela)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if etapa == 0:
            etapa = 0

            for a in listaPerguntas.lista:
                pergunta = a.pe
                alternativaA = a.alternativaA
                alternativaB = a.alternativaB
                alternativaC = a.alternativaC
                alternativaD = a.alternativaD
                respostaCerta = a.resposta.replace('\n', '')
                break

            #Pega o click em uma das opções e compara com a resposta certa,
            # caso certo, avança para a etapa 1 (Posicionamento)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if blocoAlternativaA.rect.collidepoint(x, y):
                    respostaEnviada = 'a'
                    if classes.compararRespostas(respostaEnviada, respostaCerta) == 1:
                        etapa = 1
                    elif classes.compararRespostas(respostaEnviada, respostaCerta) == 0:
                        etapa = 2

                elif blocoAlternativaB.rect.collidepoint(x, y):
                    respostaEnviada = 'b'
                    if classes.compararRespostas(respostaEnviada, respostaCerta) == 1:
                        etapa = 1
                    elif classes.compararRespostas(respostaEnviada, respostaCerta) == 0:
                        etapa = 2

                elif blocoAlternativaC.rect.collidepoint(x, y):
                    respostaEnviada = 'c'
                    if classes.compararRespostas(respostaEnviada, respostaCerta) == 1:
                        etapa = 1
                    elif classes.compararRespostas(respostaEnviada, respostaCerta) == 0:
                        etapa = 2

                elif blocoAlternativaD.rect.collidepoint(x, y):
                    respostaEnviada = 'd'
                    if classes.compararRespostas(respostaEnviada, respostaCerta) == 1:
                        etapa = 1
                    elif classes.compararRespostas(respostaEnviada, respostaCerta) == 0:
                        etapa = 2

        if etapa == 1: #Etapa de posicionamento

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                '''Caso o clique do mouse seja em uma das classes de atk, entra no if de ataque'''
                if blocoGuer.rect.collidepoint(x, y) or blocoArq.rect.collidepoint(x, y) \
                        or blocoMag.rect.collidepoint(x, y) or blocoCat.rect.collidepoint(x, y):

                    if blocoGuer.rect.collidepoint(x, y):
                        tipo = 1
                        addAtk = classesAtaque.Guerreiro() #instancia o primeiro atk a ser colocado no turno
                        if turno == 0:
                            armazenarAtksV.criarAtk(addAtk) #adiciona ele à lista
                            guerreiroAZ = True
                        else:
                            armazenarAtksA.criarAtk(addAtk)
                            guerreiroVZ = True
                        etapa = 2
                        break

                    elif blocoArq.rect.collidepoint(x, y):
                        tipo = 2
                        addAtk = classesAtaque.Arqueiro() #instancia o primeiro atk a ser colocado no turno
                        if turno == 0:
                            armazenarAtksV.criarAtk(addAtk) #adiciona ele à lista
                            arqueiroAZ = True
                        else:
                            armazenarAtksA.criarAtk(addAtk)
                            arqueiroVZ = True
                        etapa = 2
                        break

                    elif blocoMag.rect.collidepoint(x, y):
                        tipo = 3
                        addAtk = classesAtaque.Mago() #instancia o primeiro atk a ser colocado no turno
                        if turno == 0:
                            armazenarAtksV.criarAtk(addAtk) #adiciona ele à lista
                            magoAZ = True
                        else:
                            armazenarAtksA.criarAtk(addAtk)
                            magoVZ = True
                        etapa = 2
                        break

                    else:
                        tipo = 4
                        addAtk = classesAtaque.Catapulta() #instancia o primeiro atk a ser colocado no turno
                        if turno == 0:
                            armazenarAtksV.criarAtk(addAtk) #adiciona ele à lista
                            catapultaAZ = True
                        else:
                            armazenarAtksA.criarAtk(addAtk)
                            catapultaVZ = True
                        etapa = 2
                        break

                #Caso o clique seja em uma classe de defesa
                elif blocoToArq.rect.collidepoint(x,y) or blocoToGuer.rect.collidepoint(x, y)\
                        or blocoToMag.rect.collidepoint(x,y):

                    if blocoToGuer.rect.collidepoint(x, y):
                        tipo = 1
                        break

                    elif blocoToArq.rect.collidepoint(x,y):
                        tipo = 2
                        break

                    elif blocoToMag.rect.collidepoint(x,y):
                        tipo = 3
                        break

                if turno == 0: #Caso turno do jogador vermelho, é possivel selecionar uma das 3 zonas de defesa vermelha
                    if blocoZonaDefVermelho1.rect.collidepoint(x, y):
                        if torreV1 == False:
                            armazenaTipoTorreV1 = classesTorre.imagemTorre(tipo)
                            torreV1 = True
                            # torreCorPos cria o objeto da posição, ex. torreVermelho1 cria torre vermelha na zona def 1
                            torreVermelho1 = classesTorre.tipoTorre(tipo)
                            etapa = 2
                        else:
                            print("Posição já ocupada")

                    elif blocoZonaDefVermelho2.rect.collidepoint(x, y):
                        if torreV2 == False:
                            armazenaTipoTorreV2 = classesTorre.imagemTorre(tipo)
                            torreV2 = True
                            torreVermelho2 = classesTorre.tipoTorre(tipo)
                            etapa = 2
                        else:
                            print("Posição já ocupada")

                    elif blocoZonaDefVermelho3.rect.collidepoint(x, y):
                        if torreV3 == False:
                            armazenaTipoTorreV3 = classesTorre.imagemTorre(tipo)
                            torreV3 = True
                            torreVermelho3 = classesTorre.tipoTorre(tipo)
                            etapa = 2
                        else:
                            print("Posição já ocupada")

                elif turno == 1:
                    if blocoZonaDefAzul1.rect.collidepoint(x, y):
                        if torreA1 == False:
                            armazenaTipoTorreA1 = classesTorre.imagemTorre(tipo)
                            torreA1 = True
                            torreAzul1 = classesTorre.tipoTorre(tipo)
                            etapa = 2
                        else:
                            print("Posição já ocupada")

                    elif blocoZonaDefAzul2.rect.collidepoint(x, y):
                        if torreA2 == False:
                            armazenaTipoTorreA2 = classesTorre.imagemTorre(tipo)
                            torreA2 = True
                            torreAzul2 = classesTorre.tipoTorre(tipo)
                            etapa = 2
                        else:
                            print("Posição já ocupada")

                    elif blocoZonaDefAzul3.rect.collidepoint(x, y):
                        if torreA3 == False:
                            armazenaTipoTorreA3 = classesTorre.imagemTorre(tipo)
                            torreA3 = True
                            torreAzul3 = classesTorre.tipoTorre(tipo)
                            etapa = 2
                        else:
                            print("Posição já ocupada")


        # etapa de movimentação
        '''É necessário levar em consideração que a movimentação "fisica" dos ataques (suas imagens) não correspondem
        à sua real movimentação, logo, foi preciso utilizar um codigo para realmente mover ele e um para mover sua
         imagem'''

        if etapa == 2:
            del listaPerguntas.lista[0]
            respostaEnviada = ''



                    #Código para movimentar objetos e calcular danos
                #Movimentação vermelha
            for v in armazenarAtksV.lista:
                if v.vida <= 0: #Caso a vida de um ataque seja <= 0 seu dano geral é diminuido para 0
                    v.danoT = 0
                    v.danoAoCast = 0

                if v.pos == 0:
                    v.pos = 1
                    if v.tipo == 1:
                        guerreiroAZ = False
                        guerreiroA1 = True

                    if v.tipo == 2:
                        arqueiroAZ = False
                        arqueiroA1 = True

                    if v.tipo == 3:
                        magoAZ = False
                        magoA1 = True

                    if v.tipo == 4:
                        catapultaAZ = False
                        catapultaA1 = True

                elif v.pos == 1 and torreA3 == False:
                    v.pos = 2
                    if v.tipo == 1:
                        guerreiroA1 = False
                        guerreiroA2 = True

                    if v.tipo == 2:
                        arqueiroA1 = False
                        arqueiroA2 = True

                    if v.tipo == 3:
                        magoA1 = False
                        magoA2 = True

                    if v.tipo == 4:
                        catapultaA1 = False
                        catapultaA2 = True

                elif v.pos == 1 and torreA3:
                    if v.tipo == 1:
                        v.vida -= torreAzul3.atacarGuerreiro()
                        if v.vida > 0: #Caso a vida do Ataque seja maior que 0, ele contará o dano à torre
                            torreAzul3.serAtkBalanceamento(v.tipo)
                    if v.tipo == 2:
                        v.vida -= torreAzul3.atacarArqueiro()
                        if v.vida > 0:
                            torreAzul3.serAtkBalanceamento(v.tipo)
                    if v.tipo == 3:
                        v.vida -= torreAzul3.atacarMago()
                        if v.vida > 0:
                            torreAzul3.serAtkBalanceamento(v.tipo)
                    if v.tipo == 4:
                        v.vida -= torreAzul3.atacarCatapulta()
                        torreAzul3.danoT(v.danoT)

                elif v.pos == 2 and torreA2 == False:
                    v.pos = 3
                    if v.tipo == 1:
                        guerreiroA2 = False
                        guerreiroA3 = True

                    if v.tipo == 2:
                        arqueiroA2 = False
                        arqueiroA3 = True

                    if v.tipo == 3:
                        magoA2 = False
                        magoA3 = True

                    if v.tipo == 4:
                        catapultaA2 = False
                        catapultaA3 = True

                elif v.pos == 2 and torreA2:
                    if v.tipo == 1:
                        v.vida -= torreAzul2.atacarGuerreiro()
                        if v.vida > 0:
                            torreAzul2.serAtkBalanceamento(v.tipo)
                    if v.tipo == 2:
                        v.vida -= torreAzul2.atacarArqueiro()
                        if v.vida > 0:
                            torreAzul2.serAtkBalanceamento(v.tipo)
                    if v.tipo == 3:
                        v.vida -= torreAzul2.atacarMago()
                        if v.vida > 0:
                            torreAzul2.serAtkBalanceamento(v.tipo)
                    if v.tipo == 4:
                        v.vida -= torreAzul2.atacarCatapulta()
                        torreAzul2.danoT(v.danoT)

                elif v.pos == 3:
                    v.vida -= casteloAzul.danoCausado  # Castelo ataca todas as classes à sua frente
                    if torreA1:
                        if v.tipo == 1:
                            v.vida -= torreAzul1.atacarGuerreiro()
                            if v.vida > 0:
                                torreAzul1.serAtkBalanceamento(v.tipo)
                        if v.tipo == 2:
                            v.vida -= torreAzul1.atacarArqueiro()
                            if v.vida > 0:
                                torreAzul1.serAtkBalanceamento(v.tipo)
                        if v.tipo == 3:
                            v.vida -= torreAzul1.atacarMago()
                            if v.vida > 0:
                                torreAzul1.serAtkBalanceamento(v.tipo)
                        if v.tipo == 4: #colocar código pra catapulta atacar primeiro a torre, caso exista
                            torreAzul1.danoT(v.danoT)
                            v.vida -= torreAzul1.atacarCatapulta()
                    elif torreA1 == False: #em torres, a numero 1 é a mais perto do castelo
                        casteloAzul.dano(v.danoAoCast)

                if v.vida <= 0: #Caso a vida do ataque seja <= 0, sua imagem irá sumir da tela
                    if v.pos == 1:
                        if v.tipo == 1:
                            guerreiroA1 = False

                        if v.tipo == 2:
                            arqueiroA1 = False

                        if v.tipo == 3:
                            magoA1 = False

                        if v.tipo == 4:
                            catapultaA1 = False

                    elif v.pos == 2:
                        if v.tipo == 1:
                            guerreiroA2 = False

                        if v.tipo == 2:
                            arqueiroA2 = False

                        if v.tipo == 3:
                            magoA2 = False

                        if v.tipo == 4:
                            catapultaA2 = False

                    elif v.pos == 3:
                        if v.tipo == 1:
                            guerreiroA3 = False

                        if v.tipo == 2:
                            arqueiroA3 = False

                        if v.tipo == 3:
                            magoA3 = False

                        if v.tipo == 4:
                            catapultaA3 = False

                elif v.vida > 0:
                    if v.pos == 1:
                        if v.tipo == 1:
                            guerreiroA1 = True

                        if v.tipo == 2:
                            arqueiroA1 = True

                        if v.tipo == 3:
                            magoA1 = True

                        if v.tipo == 4:
                            catapultaA1 = True

                    elif v.pos == 2:
                        if v.tipo == 1:
                            guerreiroA2 = True

                        if v.tipo == 2:
                            arqueiroA2 = True

                        if v.tipo == 3:
                            magoA2 = True

                        if v.tipo == 4:
                            catapultaA2 = True

                    elif v.pos == 3:
                        if v.tipo == 1:
                            guerreiroA3 = True

                        if v.tipo == 2:
                            arqueiroA3 = True

                        if v.tipo == 3:
                            magoA3 = True

                        if v.tipo == 4:
                            catapultaA3 = True

                #Movimentação azul
            for v in armazenarAtksA.lista:
                if v.vida <= 0:
                    v.danoT = 0
                    v.danoAoCast = 0

                if v.pos == 0:
                    v.pos = 1
                    if v.tipo == 1:
                        guerreiroVZ = False
                        guerreiroV1 = True

                    if v.tipo == 2:
                        arqueiroVZ = False
                        arqueiroV1 = True

                    if v.tipo == 3:
                        magoVZ = False
                        magoV1 = True

                    if v.tipo == 4:
                        catapultaVZ = False
                        catapultaV1 = True

                elif v.pos == 1 and torreV3 == False:
                    v.pos = 2
                    if v.tipo == 1:
                        guerreiroV1 = False
                        guerreiroV2 = True

                    if v.tipo == 2:
                        arqueiroV1 = False
                        arqueiroV2 = True

                    if v.tipo == 3:
                        magoV1 = False
                        magoV2 = True

                    if v.tipo == 4:
                        catapultaV1 = False
                        catapultaV2 = True

                elif v.pos == 1 and torreV3:
                    if v.tipo == 1:
                        v.vida -= torreVermelho3.atacarGuerreiro()
                        if v.vida > 0:
                            torreVermelho3.serAtkBalanceamento(v.tipo)
                    if v.tipo == 2:
                        v.vida -= torreVermelho3.atacarArqueiro()
                        if v.vida > 0:
                            torreVermelho3.serAtkBalanceamento(v.tipo)
                    if v.tipo == 3:
                        v.vida -= torreVermelho3.atacarMago()
                        if v.vida > 0:
                            torreVermelho3.serAtkBalanceamento(v.tipo)
                    if v.tipo == 4:
                        v.vida -= torreVermelho3.atacarCatapulta()
                        torreVermelho3.danoT(v.danoT)

                elif v.pos == 2 and torreV2 == False:
                    v.pos = 3
                    if v.tipo == 1:
                        guerreiroV2 = False
                        guerreiroV3 = True

                    if v.tipo == 2:
                        arqueiroV2 = False
                        arqueiroV3 = True

                    if v.tipo == 3:
                        magoV2 = False
                        magoV3 = True

                    if v.tipo == 4:
                        catapultaV2 = False
                        catapultaV3 = True

                elif v.pos == 2 and torreV2:
                    if v.tipo == 1:
                        v.vida -= torreVermelho2.atacarGuerreiro()
                        if v.vida > 0:
                            torreVermelho2.serAtkBalanceamento(v.tipo)
                    if v.tipo == 2:
                        v.vida -= torreVermelho2.atacarArqueiro()
                        if v.vida > 0:
                            torreVermelho2.serAtkBalanceamento(v.tipo)
                    if v.tipo == 3:
                        v.vida -= torreVermelho2.atacarMago()
                        if v.vida > 0:
                            torreVermelho2.serAtkBalanceamento(v.tipo)
                    if v.tipo == 4:
                        v.vida -= torreVermelho2.atacarCatapulta()
                        torreVermelho2.danoT(v.danoT)

                elif v.pos == 3:
                    v.vida -= casteloVermelho.danoCausado #Castelo ataca todas as classes à sua frente
                    if torreV1:
                        if v.tipo == 1:
                            v.vida -= torreVermelho1.atacarGuerreiro()
                            if v.vida > 0:
                                torreVermelho1.serAtkBalanceamento(v.tipo)
                        if v.tipo == 2:
                            v.vida -= torreVermelho1.atacarArqueiro()
                            if v.vida > 0:
                                torreVermelho1.serAtkBalanceamento(v.tipo)
                        if v.tipo == 3:
                            v.vida -= torreVermelho1.atacarMago()
                            if v.vida > 0:
                                torreVermelho1.serAtkBalanceamento(v.tipo)
                        if v.tipo == 4: #colocar código pra catapulta atacar primeiro a torre, caso exista
                            torreVermelho1.danoT(v.danoT)
                            v.vida -= torreVermelho1.atacarCatapulta()
                    elif torreV1 == False: #em torres, a numero 1 é a mais perto do castelo
                        casteloVermelho.dano(v.danoAoCast)

                if v.vida <= 0:
                    if v.pos == 1:
                        if v.tipo == 1:
                            guerreiroV1 = False

                        if v.tipo == 2:
                            arqueiroV1 = False

                        if v.tipo == 3:
                            magoV1 = False

                        if v.tipo == 4:
                            catapultaV1 = False

                    elif v.pos == 2:
                        if v.tipo == 1:
                            guerreiroV2 = False

                        if v.tipo == 2:
                            arqueiroV2 = False

                        if v.tipo == 3:
                            magoV2 = False

                        if v.tipo == 4:
                            catapultaV2 = False

                    elif v.pos == 3:
                        if v.tipo == 1:
                            guerreiroV3 = False

                        if v.tipo == 2:
                            arqueiroV3 = False

                        if v.tipo == 3:
                            magoV3 = False

                        if v.tipo == 4:
                            catapultaV3 = False

                elif v.vida > 0:
                    if v.pos == 1:
                        if v.tipo == 1:
                            guerreiroV1 = True

                        if v.tipo == 2:
                            arqueiroV1 = True

                        if v.tipo == 3:
                            magoV1 = True

                        if v.tipo == 4:
                            catapultaV1 = True

                    elif v.pos == 2:
                        if v.tipo == 1:
                            guerreiroV2 = True

                        if v.tipo == 2:
                            arqueiroV2 = True

                        if v.tipo == 3:
                            magoV2 = True

                        if v.tipo == 4:
                            catapultaV2 = True

                    elif v.pos == 3:
                        if v.tipo == 1:
                            guerreiroV3 = True

                        if v.tipo == 2:
                            arqueiroV3 = True

                        if v.tipo == 3:
                            magoV3 = True

                        if v.tipo == 4:
                            catapultaV3 = True


            #Inicia os marcadores de vida e atualiza eles
            if torreA1:
                marcadorVidaTorreA1 = torreAzul1.vida
            if torreA2:
                marcadorVidaTorreA2 = torreAzul2.vida
            if torreA3:
                marcadorVidaTorreA3 = torreAzul3.vida
            if torreV1:
                marcadorVidaTorreV1 = torreVermelho1.vida
            if torreV2:
                marcadorVidaTorreV2 = torreVermelho2.vida
            if torreV3:
                marcadorVidaTorreV3 = torreVermelho3.vida

            #Destroi as imagens das torres com a vida = 0
            if torreV1 and torreVermelho1.vida <= 0:
                torreV1 = False
                torreVermelho1 = ''

            if torreV2 and torreVermelho2.vida <= 0:
                torreV2 = False
                torreVermelho2 = ''

            if torreV3 and torreVermelho3.vida <=0:
                torreV3 = False
                torreVermelho3 = ''

            if torreA1 and torreAzul1.vida <= 0:
                torreA1 = False
                torreAzul1 = ''

            if torreA2 and torreAzul2.vida <= 0:
                torreA2 = False
                torreAzul2 = ''

            if torreA3 and torreAzul3.vida <= 0:
                torreA3 = False
                torreAzul3 = ''

            #Checar se a vida do castelo ainda é maior que 0, caso contrário, tela de vencedor ou empate
            if casteloVermelho.vida <= 0 and casteloAzul.vida <= 0:
                print("Empate")

            elif casteloVermelho.vida < 0:
                # Caso vida vermelha seja igual ou menor que 0, vermelho perde
                print("Vermelho perdeu")

            elif casteloAzul.vida < 0:
                print("Azul perdeu")
                # Caso vida azul seja menor ou igual a 0

            #Ver quem ganhou caso a lista de perguntas acabe
            if len(listaPerguntas.lista) <= 0:
                if casteloVermelho.vida == casteloAzul.vida:
                    print("Empate!")

                elif casteloVermelho.vida < casteloAzul.vida:
                    # Caso vida vermelha seja menor que a azul
                    print("Vermelho Perdeu!")

                elif casteloAzul.vida < casteloVermelho.vida:
                    print("Azul Perdeu!")
                    # Caso vida azul seja menor que a vida vermelha
                pygame.quit()
                exit()
            #

            etapa = 0
            if turno == 1: #Dois ifs que permitem a mudança de turno
                turno = 0
            elif turno == 0:
                turno = 1
            pygame.time.delay(1000)