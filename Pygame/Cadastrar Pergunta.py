def addPergunta(prg,A,B,C,D,resp): #Função que abre o arquivo contendo as perguntas
    arq = open("pergunta.txt","a")# e escreve os parametros que foram passados em suas respectivas linhas
    arq.write('\n')
    arq.write(prg)
    arq.write('\n')
    arq.write("A)\t")
    arq.write(A)
    arq.write('\n')
    arq.write("B)\t")
    arq.write(B)
    arq.write('\n')
    arq.write("C)\t")
    arq.write(C)
    arq.write('\n')
    arq.write("D)\t")
    arq.write(D)
    arq.write('\n')
    arq.write(resp)
    arq.write('\n')
    arq.close()

def criarPergunta(): #Criador de perguntas, irá ser interrompido ao escrever 'fim' como pergunta
    while True:
        prg = input("Pergunta: ")
        if prg == "fim":
            break
        else:
            a = input("Alternativa A: ")
            b = input("Alternativa B: ")
            c = input("Alternativa C: ")
            d = input("Alternativa D: ")
            resp = input("Resposta: ")
            addPergunta(prg,a,b,c,d,resp)

criarPergunta()