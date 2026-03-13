'''
Lista -> linear, mutável, de comprimento variável que permite tipos diferentes de elementos
Vetor: posição de memória (índice ou posição 0) 

['cereal', 'banana', 'maçã', 'melão', 'iogurte']

Entrada de Dados em uma Lista (append) e Tamanho da Lista (len)
O objetivo é criar um programa que:
    Solicita ao usuário a quantidade de elementos da lista.
    Insere essa quantidade de elementos na lista (usando o método append).
    Mostra os elementos armazenados nela.

lista=[]

def quantidade():
    x = int(input('Quantidade de números:'))
    return x

def entrada(x):
    for i in range(x):
        num = int(input('Número:'))
        lista.append(num)
        
def saida():
    for i in range(len(lista)):
        print('Valor:', lista[i])
        
def main():
    x=quantidade()
    entrada(x)
    print(lista)
    saida()
    
main()

Criando uma lista
Vetor = [0]*10 #cria uma lista preenchida com 10 zeros 
Vetor [0] = 3  #coloca o valor 3 na posição 0 da lista
vetor = [3,0,0,0,0,0,0,0,0,0,0]
lista = []     #cria uma lista vazia

Acrescentando um elemento no final da lista 
lista = [1,2]
lista.append(3)
lista 
[1,2,3]

Acrescentando um elemento na posção indicada por índice 
lista= [0,1,2,3]
lista.insert(1, 'dois')
lista
[0,'dois',1,2,3]

Verificando se um elemento está na lista 
lista=[1, 'a','bc']
1 in lista
True
2 in lista 
False
'b' in lista 
False 
'b' in lista[2]
True

Ordenando lista em ordem crescente 
lista=[9,8,7,1,4,2]
lista.sort()
lista
[1,2,4,7,8,9]


Ordenando lista em ordem decrescente
lista=[1,2,3]
lista.reverse()
lista
[3,2,1]

Exemplo:
nome = ['Ana', 'Marcos', 'Roberto', 'João']
print(nome[1])
print('Antes: ', nome)
nome[2] = 'Carlos'
print('Depois: ', nome)
nome.insert(2, 'Aline')
print('Depois de inserir: ', nome)
nome.append('Maria')
nome.append('Beatriz')
print('Depois do append: ', nome)
del nome[3]
print('Depois de apagar: ', nome)
nome.sort()
print('Lista de nomes em ordem crescente: ', nome)
nome.reverse()
print('Lista de nomes em ordem decrescente: ', nome)

Marcos
Antes: ['Ana', 'Marcos', 'Roberto', 'João']
Depois: ['Ana', 'Marcos', 'Carlos', 'João']
Depois de inserir: ['Ana', 'Marcos', 'Aline', 'Carlos', 'João']
Depois do append: ['Ana', 'Marcos', 'Aline', 'Carlos', 'João', 'Maria', 'Beatriz']
Depois de apagar: ['Ana', 'Marcos', 'Aline', 'João', 'Maria', 'Beatriz']
Lista de nomes em ordem crescente: ['Aline', 'Ana', 'Beatriz', 'João', 'Marcos', 'Maria']
Lista de nomes em ordem decrescente: ['Maria', 'Marcos', 'João', 'Beatriz', 'Ana', 'Aline']
>>>
'''
