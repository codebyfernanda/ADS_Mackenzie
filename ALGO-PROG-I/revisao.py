# variáveis 
# nome, celular, endereço -> memória 

velocidade_internet = 400 
print(velocidade_internet)

# números inteiros (int)
idade = 15

# números decimais (float)
nota = 8.5

# textos (string ou str)
nome_completo = 'Fernanda Bastos'

# booleanos (True ou False ou bool)
pode_entrar = False

print (type(idade))

# Prob 1 - Valor / hora 
# Escreva um programa que retorna o valor / hora de um funcionário 
# com base no salário mensal e horas trabalhadas por mês 

'''
1. Dados de entrada necessários?
- salário mensal 
- quantidade de horas trabalhadas 

2. O que fazer com esstes dados? 
- calcular valor / hora

3. Restrições? 
- precisa ter um valor do sal mensal e horas trabalhadas

4. Resultado esperado? 
Exibir valor hora com base no cálculo de valor hora 

5. Sequência de passos? (pseudocódigo)  
receber sal mensal 
receber quantidade de horas trabalhadas 
valor hora = salário mensal / quantidade de horas trabalhadas
exibir valor hora
'''

salario_mensal = input('Qual é o seu salário mensal: ')
horas_trabalhadas = input('Quantas horas trabalhadas por mês: ')
valor_hora = float(salario_mensal) / int(horas_trabalhadas) 
print(valor_hora)

# Condicionais - if elif else 
'''
E aí, bora sair? 
Se eu terminar meu trabalho, 
'''

trabalho_terminado = False
if trabalho_terminado == True: 
    print('Bora')
else: 
    print('Não posso ir!')

'''
Ei, você consegue me ajudar a mover essas caixas lá pra fora? 
Se eu tiver livre, sim. Mas se não, pede pro meu irmão
'''

# estou_livre = False 
estou_livre = input('Você está livre? S/N ')
if estou_livre == 'S': 
    print('Ok, bora!')
else: 
    print('Pede ajuda pro meu irmão')

# mais de duas condições 

'''
Cheguei atrasado, posso entrar na aula? 
Se for a 1ª ou 2ª vez que chega atraso, sim.
Mas se for a terceira, será suspenso
'''

# atrasos = 0
atrasos = int(input('Quantas faltas você tem? '))
if atrasos >= 3: 
    print('Você está suspenso!')
elif atrasos == 2: 
    print('Mais uma falta e estará suspenso!')
elif atrasos == 1: 
    print('Mais duas faltas e estará suspenso!')
else: 
    print('Pode entrar')

# Prob 2
# Crie um programa que recebe dois valores e exibe o maior 

primeiroNumero = int(input('Digite o primeiro número aqui: '))
segundooNumero = int(input('Agora, digite o segundo número escolhido: '))

if primeiroNumero > segundooNumero: 
    print('O maior número é', primeiroNumero)
else: 
    print('O maior número é', segundooNumero)

# Laços de repetição 
for item in range(3):
    print(item)

'''
for item in colecao 
    # comandos
'''
# Range nunca inclui o último número
for item in range(10): 
    print(item)

# OU
for item in range(1,10):
    print(item)

# Pular de dois em dois 
for item in range(1,11, 2):
    print(item)

for item in range(2, 12, 2):
    print(item)

# Lista de nomes 
nomes = ['Fernanda', 'Sérgio', 'Olivia', 'Dante']
dados = [21, 'Fernanda', True, 1.61]
for nome in nomes: 
    print (nome)

for dado in dados: 
    print(dado)

idades = [21, 11, 27, 31, 60]
# Exiba somente os maiores de idade 
for idade in idades: 
    if idade >= 18: 
        print(f'{idade} é maior de idade')
    else: 
        print(f'{idade} é menor de idade')

'''
Validador de senhas
Você trabalha em um sistema que precisa verificar se as senhas digitadas pelos usuários são váçlidas.

Para ser válida, precisa de 8 caracteres. 
'''

'''
- receber a senha 
- verificar se tem 8 char
- se tiver, permitir 
- se não, não permitir
'''

# len(variavel) -> quantidade de caracteres
# len(senha) -> 8 ou não

senhas = ['ABC', 'segura123', 'python1234567', 'oi']
for senha in senhas: 
    if len(senha) >= 8:
        print(f'A senha {senha} é válida')
    else: 
        print(f'A senha {senha} deve possuir no mínimo 8 caracteres')

# Não sei quants vezes vai rodar ou algo precisa mudar

'''
sintaxe

while condicao: 
    # código a ser executado
'''

# Criar um programa que permite 3 tentativas, antes de fechar 
tentativas = 0 
while tentativas < 3: 
    print('Tente novamente')
    tentativas = tentativas + 1

# Quando queremos que uma ação continue acontecento, até que
# um critério seja satisfeito 
# Só pode logar, se digitar senha certa

senha = ''
while senha != '1234567': 
    input('Digite a senha correta: ')

print('Bem-vindo ao sistema')

# Garantir que algo esteja preenchido 
# Só deve continuar, quando o usuário infomar seu nome 

nome = ''
while nome == '': 
    nome = input('Digite seu nome: ')

print(f'Bem vindo/a {nome}')

# Contadores dentro do while (contador controla o while)

# Ser avisado às 17hrs sobre o pôr-do-sol 
# Contar de hora em hora até chegar às 17hrs 
# Ao chegar às 17hrs, exibir: "hora do pôr-do-sol"

horario = 0 
while horario <= 17: 
    print(horario)
    horario = horario + 1 

print('Hora de ver o pôr-do-sol')

'''
Crie um gerenciador de login, com máximo de 3 tentativas 
(Um único usuário e senha permitidos)

Usuário - Fernanda 
Senha - senha123

Após 3 tentativas, se o usuário estiver errado, exibir: 
"Aguardo 30 mins antes de tentar novamente!"

Se acertar o usuário e senha antes disso, exibir: 
"Login feito com sucesso"
'''

usuario = ''
senha = ''
tentativas = 0 

while (usuario != 'Fernanda' and senha != 'senha123') and tentativas < 3:
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    tentativa += 1

if usuario != 'Fernanda' and senha != 'senha123':
    print('Aguarde 30 mins antes de tentar novamente')
else: 
    print('Login feito com sucesso')

# Listas 
precos = [21,31, 111]
#[21,31, 111]
#  0  1    2
print(precos[1])

nomes = ['Brasil', 'EUA', 'Austrália']
print(nomes[1])

# Encontrar o índice automaticamente 
print(nomes.index('EUA'))

# Manipular - add novos itens
salarios = [2500, 5000, 7000]
salario_usuario = float(input('Qual é o seu salário? '))
salarios.append(salario_usuario)
print(salarios)

# Problema - Gastos totais com pag. de salários
# Dado uma lista de salários, calcule o total pago a todos os funcionários 

salarios = [2500, 5000, 7000]
total = 0 
for salario in salarios: 
    total = total + salario

print(total)

# Projeto 1 - Fatorial de um número
# Crie um programa que recebe um número e imprime seu fatorial

numero = int(input('Digite o fatorial que deseja calcular: '))
if numero > 0 and type(numero) == int: 
    fatorial = 1
    for item in range (1, numero+1):
        print(f'{fatorial} * {item}')
        fatorial = fatorial * item 
        print(f'{fatorial}')
    print(f'O fatorial de {numero} é {fatorial}')
else: 
    print('favor informar apenas números inteiros positivos')

# Projeto 2 - Chute o nº 
'''
Escreva um programa que, ao iniciar, gere um valor aleatório de 1 a 21 e permita
que o usuário chite números até acertar o valor gerado. 

O programa deve informar se o chute foi maior, menor ou igual ao valor aleatório
gerado no início
'''

import random 

valor_aleatorio = random.randint(1,21)
acerto = False 

while acertou == False: 
    chute = int(input('Chute um número: '))
    if chute > valor_aleatorio: 
        print('Chute um valor mais baixo')
    elif chute < valor_aleatorio: 
        print('chute um valor mais alto')
    else: 
        print('Você acertou!')
        acertou = True


# Projeto 3 - Medidor de Velocidade
'''
Um programa que receba do usuário um valor que represente a velocidade em
uma via cuja velocidade máxima permitida é de 80 km/h. 

O programa deve informar se o motorista levou multa:

    Sem multa - velocidade =< 80km 
        Leve - 10km/h acima 
        Grave - 11~20km/h acima
        Gravíssima - acima de 20km/h 

'''

velocidade = float(input('Digite a velocidade: '))
velocidade_maxima = 80 
if velocidade <= velocidade_maxima: 
    print('Não houve multa')
elif velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')
elif velocidade <= velocidade_maxima + 20:
    print('Levoumulta grave')
else: print('Multa gravíssima')

# -------------------------------------------------------------------------------------------------

def getSessionCount(timeout, userIds, timestamps):
    # 1. Criar o dicionário para agrupar tempos por usuário
    eventos_por_usuario = {}
    
    # 2. Preencher o dicionário
    for i in range(len(userIds)):
        user = userIds[i]
        time = timestamps[i]
        
        if user not in eventos_por_usuario:
            eventos_por_usuario[user] = []
        eventos_por_usuario[user].append(time)
    
    total_de_sessoes = 0
    
    # 3. Contar as sessões para cada usuário
    for user in eventos_por_usuario:
        # Ordena apenas os timestamps deste usuário específico
        eventos = sorted(eventos_por_usuario[user])
        
        sessoes = 1  # Se o usuário tem eventos, ele tem pelo menos 1 sessão
        
        for i in range(1, len(eventos)):
            # Se o intervalo entre eventos for maior que o timeout, nova sessão
            if eventos[i] - eventos[i - 1] > timeout:
                sessoes += 1
        
        total_de_sessoes += sessoes
        
    return total_de_sessoes

# Exemplo de teste para você rodar no VS Code:
t = 5
ids = [1, 1, 2]
times = [10, 20, 10]
print(getSessionCount(t, ids, times))
