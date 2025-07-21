
valor_1 = float(input('Qual o primeiro número'))
valor_2 = float(input('Qual o segundo número'))
valor_3 = float(input('Qual o terceiro número?'))


if valor_1== 0:
    print ('Por favor, insira um número superior a 0')
if valor_2== 0:
    print ('Por favor, insira um número superior a 0')
if valor_3== 0:
    print ('Por favor, insira um número superior a 0')
if valor_1>valor_2 and valor_1>valor_3:
    print ('O primeiro número é maior')
if valor_2>valor_1 and valor_2>valor_3:
    print ('O segundo número é maior')
if valor_3>valor_1 and valor_3>valor_2:
    print ('O terceiro número é o maior')
if valor_1 == valor_2 == valor_3:
    print ('Os três valores são iguais!!!')
if valor_2 == valor_1 < valor_3:
    print ('O terceiro é maior, enquanto o primeiro e o segundo são iguais.')
if valor_1 == valor_3 < valor_2:
    print ('O segundo valor é o maior, enquanto o primeiro e o terceiro são iguais.')
if valor_2 == valor_3 < valor_1:
    print ('O primeiro valor é o maior, enquanto o segundo e terceiro são iguais.')
