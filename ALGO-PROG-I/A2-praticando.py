#EXERCÍCIO 1 -----------------------------------------------
'''
Escreva um programa  que permita ao usuário digitar dois números inteiros e exibir o resultado para cada uma das seguintes operações, nesta ordem: soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação. 
'''

print('-----------------------------------------------------------------')
print('OLÁ, USUÁRIO. BEM VINDO/A A CALCULADORA DE DOIS NÚMEROS INTEIROS!')
print('-----------------------------------------------------------------')
print('Aqui, você poderá digitar dois números e te mostrarei o resultado das operações, sendo elas: soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')

print('Primeiro, digite um número: ')
num1 = int(input())
print('Agora digite o segundo número: ')
num2 = int(input())

#OPERAÇÕES 
soma = num1 + num2 
sub = num1 - num2 
multi = num1 * num2 
div = num1 / num2 
divT = num1 // num2 
resto = num1 % num2 
expo = num1 ** num2 

print(f'A soma entre {num1} e {num2}, os dois números digitados, é igual a {soma}')
print(f'A subtração entre {num1} e {num2} é igual a {sub}')
print(f'A multiplicação entre {num1} e {num2} é igual a {multi}')
print(f'A divisão entre {num1} e {num2} é igual a {div}')
print(f'A divisão truncada entre {num1} e {num2} é igual a {sub}')
print(f'O resto da divisão entre {num1} e {num2} é igual a {resto}')
print(f'A exponenciação entre {num1} e {num2} é igual a {expo}')

#EXERCÍCIO 2 -----------------------------------------------

'''
Faça um programa que leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo. 
'''

print('-----------------------------------------------------------------')
print('OLÁ!! BEM VINDO/A A CALCULADORA ENTRE DOIS NÚMEROS INTEIROS!')
print('-----------------------------------------------------------------')
print('Aqui, você poderá digitar dois números e te mostrarei o resultado do quadrado da diferença do primeiro valor pelo segundo')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')

print('Digite o primeiro número: ')
num1 = int(input())
print('Sua vez de digitar o segundo número: ')
num2 = int(input())

#OPERAÇÃO 
op = (num1 - num2) ** 2
print(f'O resultado da operação é igual a {op}')


#EXERCÍCIO 3 -----------------------------------------------

'''
Faça um programa que resolva o seguinte problema: 

Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 
- o primeiro ganhador receberá 46% do prêmio; 
- o segundo ganhador receberá 32% do prêmio; 
- o terceiro ganhador receberá o restante do prêmio. 

Calcule e mostre o valor do prêmio de cada ganhador, nesta ordem: primeiro colocado, segundo colocado e terceiro colocado.
Observe que este programa não tem valor de entrada feita pelo usuário. 
'''

print('-----------------------------------------------------------------')
print('OLÁ, CALCULE AQUI O VALOR DO PRÊMIO DOS 3 GANHADORES!')
print('-----------------------------------------------------------------')
total = 780000
premioPrimeiro = 780000 * 0.46
premioSegundo = 780000 * 0.32
premioTerceiro = total - premioPrimeiro - premioSegundo

print('O VALOR DO PRÊMIO DE PRIMEIRO LUGAR SERÁ R$ %.2f' %premioPrimeiro)
print('JÁ O VALOR DO PRÊMIO DE SEGUNDO LUGAR SERÁ R$ %.2f' %premioSegundo)
print('E POR ÚLTIMO MAS NÃO MENOS IMPORTANTE, O VALOR DO PRÊMIO DE TERCEIRO LUGAR SERÁ R${premioTerceiro %.2f' %premioTerceiro)
