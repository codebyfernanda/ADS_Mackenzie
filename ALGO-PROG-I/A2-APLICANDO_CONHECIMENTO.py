# print(-------------------------------------------------------------);
# print(Bem-vindo/a, usuário! Aqui, você poderá fazer alguns cálculos);
# print(Como por exemplo: o salário bruto mensal, o valor a ser pago ao INSS, a taxa sindical e o salário líquido, após a dedução do INSS e da taxa sindical");
# print(-------------------------------------------------------------);

# print('Primeiro, digite o seu salário por hora: '); 
salHora = float(input())
# print('Agora, digite quantas horas foram trabalhadas no último mês: ');
horas = int(input())

salTotal = salHora * horas
contribuicaoINSS = salTotal * 0.08
taxaSindical = salTotal * 0.05
salLiq = salTotal - contribuicaoINSS - taxaSindical 

print('%.2f' %salTotal) 
print('%.2f' %contribuicaoINSS) 
print('%.2f' %taxaSindical)
print('%.2f' %salLiq)
