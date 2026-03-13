print('Digite dois números: ')
a = int(input())
b = int(input())
media = (a+b)/2
print('Média = ', media)'''

#EXERCÍCIO 1 -----------------------------------------------
''' Faça um programa que receba 4 nºs inteiros, calcule e mostre a soma entre eles'''

print('Bem-vindo/a a calculadora de soma de quatro números') 
print('Para isso, digite quatro números a seguir :)')
print('Digite o primeiro número: ')
num1 = int(input())
print('Agora, escreva o segundo número: ')
num2 = int(input())
print('E então, digite qual será o terceiro número: ')
num3 = int(input())
print('Por fim, escreva o quarto número escolhido: ')
num4 = int(input())
soma = num1 + num2 + num3 + num4
print('Então, a soma dos quatro números é =', soma) #OU print(f'Então, a soma dos quatro números é igual a {soma}') 

'''
#EXERCÍCIO 2 -----------------------------------------------
''' Faça um programa que receba 3 notas, calcule e mostre a média aritmética entre elas'''

print('-----------------------------------')
print('BEM VINDO/A AO CALCULADOR DE NOTAS ONLINE')
print('-----------------------------------')
print('Aqui vamos calcular a média de três notas')
print('-----------------------------------')
print('-----------------------------------')
print('Para isso, digite a primeira nota: ')
nota1 = float(input())
print('Agora escreva a segunda nota: ')
nota2 = float(input())
print('Então, digite a terceira e última nota: ')
nota3 = float(input())
média = (nota1 + nota2 + nota3)/3 
print('De acordo com os nossos cálculos, a sua média é =', média) #OU print('Média das notas = %.1f' %media) 

'''
#EXERCÍCIO 3 -----------------------------------------------
''' Faça um programa que receba 3 notas E SEUS RESPECTIVOS PESOS calcule e mostre a média PONDERADA dessas notas'''

print('Digite as três notas')
num1 = float(input())
num2 = float(input())
num3 = float(input())

print('Digite o peso de cada nota')
peso1 = int(input())
peso2 = int(input())
peso3 = int(input())

media = (num1 * peso1 + num2 * peso2 + num3 * peso3) / (peso1 + peso2 + peso3)
print('A média pondera é igual a ', media)

'''
#EXERCÍCIO 4 -----------------------------------------------
''' Faça um programa que receba osalério de um funionário, calcule e mostre o novo salário, com um aumento de 25%'''

print('-----------------------------------')
print('OLÁ, BEM-VINDO/A A CALCULADORA DE AUMENTO DE SALÁRIO')
print('-----------------------------------')
print('Por favor, insira seu salário aqui: ')
sal = float(input()) #OU sal = float(input('Salário:'))
novoSal = sal * 1.25
print('Seu novo salário com o aumento de 25% será =', novoSal) #OU print('Novo salário = ', sal*1.25)
print('-----------------------------------')
