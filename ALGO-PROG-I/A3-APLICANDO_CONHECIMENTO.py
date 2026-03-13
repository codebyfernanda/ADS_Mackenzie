velocidade = float(input('Informe a velocidade: ')); 
if (velocidade > 50): 
    print('Você será multado'); 
print('fim'); 

n1 = float(input('Digite um número: '));
if n1 % 2 == 0: 
    print('%.1f é par. ' %n1); 
else: 
    print('%.1f é ímpar. ' %n1); 

import math #biblioteca
print('Digite dois números'); 
n1 = float (input());
n2 = float (input());
if n1 > n2: 
    quadrado = math.pow(n1, 2); #n1 ao quadrado
else: 
    quadrado = math.pow(n2, 2); #n2 ao quadrado
print('Quadrado do maior: ', quadrado); 

pesoPeixe = float(input())

limiteDoPeso = 50.0
excessoDePeso = 0.0
multaDoRegulamento = 0.0

if pesoPeixe > limiteDoPeso:
    excessoDePeso = pesoPeixe - limiteDoPeso
    multaDoRegulamento = excessoDePeso * 4.0
    print(f"{excessoDePeso:.2f}")
    print(f"{multaDoRegulamento:.2f}")
else:
    bonificacao = pesoPeixe * 1.0
    print(f"{bonificacao:.2f}")

import math

area = float(input())

litros = area / 3.0
latas = math.ceil(litros / 18.0)
valor = latas * 120.0

print(latas)
print(f"{valor:.2f}")
