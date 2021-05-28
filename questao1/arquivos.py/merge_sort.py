# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:38:43 2021

@author: Eduardo Nunes
"""


def mergeSort(vetor):
    sort_half(vetor, 0, len(vetor) - 1)
    return vetor

def sort_half(vetor, start, end):
    if start >= end:
        return

    middle = (start + end)//2

    sort_half(vetor, start, middle)
    sort_half(vetor, middle + 1, end)

    merge(vetor, start, end)

def merge(array, start, end):
    array[start: end + 1] = sorted(vetor[start: end + 1])

        
import time
    
# declarando um vetor vazio
vetor = [];
vetorDecrescente = [];

while 1 == 1:
    
    inicio = 0
    fim = 0
    # declarando um vetor vazio
    vetor = [];
    vetorDecrescente = [];
    
    print("\n_____________ Merge Sort _____________\n") 
    print("\n1 - vetor com 10 elementos\n") 
    print("2 - vetor com 1.000 elementos\n")
    print("3 - vetor com 10.000 elementos\n")
    print("4 - vetor com 100.000 elementos\n")
    print("5 - vetor com 1.000.000 elementos\n")
       
    escolhaVetor = int(input("opcao desejada: "))
    
    print("\n\n1 - ordem aleatoria\n") 
    print("2 - ordem crescente\n")
    print("3 - ordem decrescente\n")
       
    escolhaOrdem = int(input("opcao desejada: "))
    print("\n\n")
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHH TEMPO HHHHHHHHHHHHHHHHHHHHHHHHHHHH\n\n")
    
    if escolhaVetor == 1:
        
        # colocando todos os numeros em um vetor ( na ordem do arquivo ).
        with open('entrada/entrada10.txt','r') as arquivo:
            for valor in arquivo:
                vetor.append(int(valor))
                
        print("• Vetor com 10 elementos\n")
                
    elif escolhaVetor == 2:
        
        # colocando todos os numeros em um vetor ( na ordem do arquivo ).
        with open('entrada/entrada1000.txt','r') as arquivo:
            for valor in arquivo:
                vetor.append(int(valor))
                
        print("• Vetor com 1.000 elementos\n")
        
    elif escolhaVetor == 3:
        
        # colocando todos os numeros em um vetor ( na ordem do arquivo ).
        with open('entrada/entrada10000.txt','r') as arquivo:
            for valor in arquivo:
                vetor.append(int(valor))
                
        print("• Vetor com 10.000 elementos\n")
                
    elif escolhaVetor == 4:
        
        # colocando todos os numeros em um vetor ( na ordem do arquivo ).
        with open('entrada/entrada100000.txt','r') as arquivo:
            for valor in arquivo:
                vetor.append(int(valor))
                
        print("• Vetor com 100.000 elementos\n")
                
    elif escolhaVetor == 5:
        
        # colocando todos os numeros em um vetor ( na ordem do arquivo ).
        with open('entrada/entrada1000000.txt','r') as arquivo:
            for valor in arquivo:
                vetor.append(int(valor))
              
        print("• Vetor com 1.000.000 elementos\n")
        
    if escolhaOrdem == 1:
           
          inicio = time.time()
          mergeSort(vetor)
          fim = time.time()
          print("• Ordem aleatória\n")
          print('• {:.4f} segundos\n\n'.format(fim-inicio))
          #print('\nvetor apos mergeSort: \n\n', vetor)
          
    elif escolhaOrdem == 2:
    
        mergeSort(vetor) # ordenando o vetor

        inicio = time.time()
        mergeSort(vetor)
        fim = time.time()
        print("• Ordem crescente\n")
        print('• {:.4f} segundos\n\n'.format(fim-inicio))
        #print('\nvetor apos mergeSort: \n\n', vetor)
    
    elif escolhaOrdem == 3:
    
        mergeSort(vetor)      
    
        # criando o vetor em ordem decrescente
        for i in range(len(vetor), 0, -1):
            vetorDecrescente.append(vetor[i-1])
        
        inicio = time.time()
        mergeSort(vetorDecrescente)
        fim = time.time()
        print("• Ordem decrescente\n")
        print('• {:.4f} segundos\n\n'.format(fim-inicio))
        #print('\nvetor apos mergeSort: \n\n', vetorDecrescente)  
        
        
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n\n")




