# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:32:48 2021

@author: Eduardo Nunes
"""

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#                            FUNÇÕES
#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH


# A Huffman Tree Node
class noh:
    def __init__(self, freq, info, esquerda = None, direita = None):
        
        # frequencia do no
        self.freq = freq
 
        # informação do noh ( char )
        self.info = info
 
        # nó à esquerda do nó atual
        self.esquerda = esquerda
 
        # nó à direita do nó atual
        self.direita = direita
 
        # direção da árvore (0/1)
        self.direcao = ''
  
def salvarCaminhosNohs(noh, vetorCaminhos, val = ''):
    
    # codigo huffman para o nó atual
    newVal = val + str(noh.direcao)
 
    # se o nó não for da extremidade da árvore
    # então será atravessado
    if(noh.esquerda):
        salvarCaminhosNohs(noh.esquerda, vetorCaminhos, newVal)
    if(noh.direita):
        salvarCaminhosNohs(noh.direita, vetorCaminhos, newVal)
 
    # se o nó for da extremidade, então seu código é exibido
    # display its huffman code
    if(not noh.esquerda and not noh.direita):
        vetorCaminhos.append(f"{noh.info}**{newVal}")
     

# escreve um arquivo com o texto em binário
def criarArquivo(nomeArquivo, texto, vetorCharSemRepetir, vetorFreq, vetorCaminhos):        
    try:
        
        arquivo = open(nomeArquivo, 'w')
        
        for i in range(len(vetorCharSemRepetir)):
            arquivo.write(vetorCharSemRepetir[i]+"&&")
            arquivo.write(str(vetorFreq[i])+"---")
            
            for j in vetorCaminhos:               
                vetorTemp = j.split("**")
                if(vetorTemp[0] == vetorCharSemRepetir[i]):
                    arquivo.write(vetorTemp[1]+"##")
                vetorTemp = []
            
        arquivo.write("\n"+texto)
        arquivo.close()
        print("• Arquivo.dvz criado com sucesso !\n")
    except IOError:
        raise print("Erro ao criar o arquivo")


def salvarCaminhoTexto(vetorCaminhos, vetorChar, vetorCaminhoTexto):
    
    for i in vetorChar:
        for k in range(len(vetorCaminhos)):
            vetorTemp = vetorCaminhos[k].split("**")
            if vetorTemp[0] == i:
                vetorCaminhoTexto.append(vetorTemp[1])
            vetorTemp = []    

# Essa função coloca todas as frequencias em um vetor,
# além disso, coloca os caracteres em um outro vetor, sem repetir e 
# na mesma ordem das frequências.
def getVetoresProntos(vetorChar, vetorFreq, vetorCharSemRepetir): 
    
    listaFrequencia = {}
    
    # salvando as frequencias em uma lista
    for i in vetorChar:
        if i in listaFrequencia:
            listaFrequencia[i] += 1
        else:
            listaFrequencia[i] = 1

    # passando as frequencias da lista para o vetor
    for chave, value in listaFrequencia.items():
            vetorFreq.append(value)
            
    # passando os caracteres da lista para outro vetor
    for chave, value in listaFrequencia.items():
            vetorCharSemRepetir.append(chave)
                

def popularVetorCaracteres(vetorChar, arquivo):
    
    for linha in arquivo:
        for char in linha:
            if(char == '\n'):
                vetorChar.append('¨')
            else:
                vetorChar.append(char)
            
def criandoNohs():
    
    # Convertendo os caracteres e frequencias em nós da árvore
    for i in range(len(vetorCharSemRepetir)):
        nohs.append(noh(vetorFreq[i], vetorCharSemRepetir[i]))        
    
def criandoArvore(nohs):
    
    while len(nohs) > 1:
        # classifica todos os nós em ordem crescente com base na sua frequência
        nohs = sorted(nohs, key = lambda i: i.freq)
     
        # seleciona os 2 menores nós
        esquerda = nohs[0]
        direita = nohs[1]
     
        # atribuir valores de direção para os nós
        esquerda.direcao = 0
        direita.direcao = 1
     
        # juntando os dois menores nós e formando o nó pai
        novoNoh = noh(esquerda.freq + direita.freq, esquerda.info + direita.info, esquerda, direita)
     
        # remove os dois nós citados acima e insere o novo nó pai entre os outros
        nohs.remove(esquerda)
        nohs.remove(direita)
        nohs.append(novoNoh)
        
    return nohs
  
def decodificar():
    
    caminho = ''
    
    for textoZip in stringTextoZip:
        
        for char in textoZip:
            nohsTemp = nohs[0]
            caminho = caminho + char
            
            for direcao in vetorCaminhosTextoZip:
                if caminho == direcao:            
                    for index in caminho:
                        if index == '1':
                            if nohsTemp.direita:   
                                nohsTemp = nohsTemp.direita # noh vai pra direita 
                        elif(index == '0'):
                            if nohsTemp.esquerda:
                                nohsTemp = nohsTemp.esquerda # noh vai pra esquerda
                                
                    for index2 in nohs[0].info:        
                        if nohsTemp.info[0] == index2:
                            if nohsTemp.info == '¨':
                                vetorTextoDecode.append('\n')
                            else:
                                vetorTextoDecode.append(nohsTemp.info)
                            caminho = ''
      
while True:
    
    #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    #                           COMPACTANDO
    #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    
    vetorCaminhos = [] # vetor com os nohs da árvore e seus respectivos caminhos
    vetorTexto = [] # vetor com o texto completo do arquivo
    vetorChar = [] # vetor com todos os caracteres do texto, se repetindo durante o vetor
    vetorFreq = [] # vetor com todas as frequencias, para cada caracter
    vetorCharSemRepetir = [] # vetor com todos os caracteres separados e sem se repetir
    vetorCaminhoTexto = [] # vetor com o caminho completo do texto
    nohs = [] # lista que contém os nós não usados
    
    print("\n\nQual arquivo deseja usar ?\n")
    print("1  -  Compressor_1\n")
    print("2  -  Compressor_2\n")
    print("3  -  Compressor_3\n")
    print("4  -  Compressor_4\n")
    print("5  -  Compressor_5\n")
    print("6  -  Fechar o programa\n")
    opcao = int(input("opcao desejada: "))
    print("\n")
    
    if(opcao == 1):
        arquivo = open('entrada/Compressor_1.txt','r')
    elif(opcao == 2):
        arquivo = open('entrada/Compressor_2.txt','r')
    elif(opcao == 3):
        arquivo = open('entrada/Compressor_3.txt','r')
    elif(opcao == 4):
        arquivo = open('entrada/Compressor_4.txt','r')
    elif(opcao == 5):
        arquivo = open('entrada/Compressor_5.txt','r')
    else:
        print("Voce fechou o programa")
        raise SystemExit
    
    # Funções para popular os vetores
    vetorTexto = arquivo.readlines()
    arquivo.seek(0)
    popularVetorCaracteres(vetorChar, arquivo) # preenchendo o vetor separado por caracteres
    getVetoresProntos(vetorChar, vetorFreq, vetorCharSemRepetir) # preenchendo o vetor de frequencias na mesma ordem dos caracteres
    
    criandoNohs()
     
    nohs = criandoArvore(nohs)
    
    # A árvore de Huffman está pronta
    # salvando os caminhos de cada no em um vetor
    salvarCaminhosNohs(nohs[0], vetorCaminhos)
    # salvando os caminhos de acordo com o texto, letras e seus caminhos
    salvarCaminhoTexto(vetorCaminhos, vetorChar, vetorCaminhoTexto)
    
    criarArquivo("darth_vader.dvz", "".join(vetorCaminhoTexto), vetorCharSemRepetir, vetorFreq, vetorCaminhos)
    
    arquivo.close()

    #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    #                         DESCOMPACTANDO
    #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    
    # Zerando todos os vetores
    
    vetorCaminhos = [] # vetor com os nohs da árvore e seus respectivos caminhos
    vetorTexto = [] # vetor com o texto completo do arquivo
    vetorChar = [] # vetor com todos os caracteres do texto, se repetindo durante o vetor
    vetorFreq = [] # vetor com todas as frequencias, para cada caracter
    vetorCharSemRepetir = [] # vetor com todos os caracteres separados e sem se repetir
    vetorCaminhoTexto = [] # vetor com o caminho completo do texto
    nohs = [] # lista que contém os nós não usados
    nohsSeparados = [] # lista que contém os caminhos dos nós na mesma ordem que nohs
    vetorTextoDecode = [] # vetor com todos os caracteres do texto, apos decodificacao
    vetorCharFreqCaminho = []
    vetorCaminhosTextoZip = [] # vetor com todas os caminhos do texto zip
    
    arquivo = open('darth_vader.dvz','r')
    stringCharFreq = arquivo.readline()
    stringTextoZip = arquivo.readlines()
    
    vetorCharFreqCaminho = stringCharFreq.split("##")
    
    for i in range(len(vetorCharFreqCaminho)-1):
        vetorTemp = vetorCharFreqCaminho[i].split("&&")
        vetorTemp2 = vetorTemp[1].split("---")
        vetorCharSemRepetir.append(vetorTemp[0])
        vetorFreq.append(int(vetorTemp2[0]))
        vetorCaminhosTextoZip.append(vetorTemp2[1])
        vetorTemp = []
        vetorTemp2 = []
        
    criandoNohs()
     
    nohs = criandoArvore(nohs)
    
    # A árvore de Huffman está pronta
    # salvando os caminhos de cada no em um vetor
    salvarCaminhosNohs(nohs[0], vetorCaminhos)
    # salvando os caminhos de acordo com o texto, letras e seus caminhos
    salvarCaminhoTexto(vetorCaminhos, vetorChar, vetorCaminhoTexto)
    
    decodificar()
    
    print("\n-------------------------------------------------------------------------------------------------------\n")
    print("Texto Decodificado do Arquivo.dvz :")
    print("\n")
    print("".join(vetorTextoDecode))
    print("\n-------------------------------------------------------------------------------------------------------")
     
    arquivo.close()

































