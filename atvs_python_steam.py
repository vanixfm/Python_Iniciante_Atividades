
lista = 7.5
 trabalho = 8.0
 prova = 5.5
 media = (lista + trabalho + prova)/3
 print('A média do aluno é: ',media)


lista = 7.5
 trabalho = 8.0
 prova = 5.5
 media = (lista * 0.3) + (trabalho *0.2) + (prova *0.5)
 print('A média do aluno é: ',media)



lista = 7.5
trabalho = 8.0
prova = 5.5
p_lista = 3
p_trabalho = 5
p_prova = 7
media = (lista * p_lista) + (trabalho * p_trabalho) + (prova * p_prova) 
media_fim = media / (p_lista + p_trabalho + p_prova)
print(media_fim)



num = int(input("Digite um numero: "))
if num % 2 == 1:
    print("primo")
else:
    print("não primo")



nome_compl = input('Digite seu nome completo: ')
ano_nasc = input('Digite o ano de nascimento: ')
var_atual = 2023
var_user = int (input ('Digite o seu ano: '))
print('A sua idade atual é de:',var_atual-var_user,'anos')


var_atual = 2023
print(var_atual)
nome_compl = input('Digite seu nome completo: ')
ano_nasc = int (input('Digite o ano de nascimento: '))



nome = 'Boas - vindas'
print(nome)

ano_atual = int(input('Digite o valor do ano atual: '))
print(ano_atual)

ano_nasc = int (input('Digite o ano de nascimento: '))

salario = float(input('Informe seu salário: '))
print('Voce recebe', salario, 'reais antes')

ano_atual = 2023
ano_nascimento =  int(input('Digite o ano de seu nascimento: '))
print('Você tem: ', ano_atual - ano_nascimento)


sal_atual = float(input('Qual é o valor de seu salário? obs:use ponto para separar '))
print('O meu salário é: ',sal_atual)
sal_add = 0.10
sal_novo = sal_atual + (sal_atual * sal_add)
print('Você recebe {:.2f} reais'.format(sal_novo))


import math

n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
soma = n1 + n2
print(soma)
algo = input('Digito alguma coisa: ')
print(type(algo))
n = int(input("Informe um número inteiro: "))
print('n: ',n)

# mostra o antecessor
print('Antecessor de {} é o {}'.format(n,n-1))
# mostra o sucessor
print('Sucessor de {} é o {}'.format(n,n+1))
# mostra o dobro
print('Dobro de {} é o {}'.format(n,2*n))
# mostra o elevado ao cubo
print('O {} elevado ao cubo é o {}'.format(n,n**3))
# mostra a raiz quadrada
print('Raiz quadrada de {} é o {}'.format(n,n**(1/2)))
print('Raiz quadrada de {} é o {}'.format(n,math.sqrt(n)))

#media
num1 = float(input('Informe n1: '))
num2 = float(input('Informe n2: '))
media = (num1 + num2)/2
print('A média entre {:.2f} e {:.2f} é {:.2f}'.format(num1,num2,media))



preco = int(input("Digite o preço do produto: "))
notas_50 = preco // 50
preco = preco % 50
notas_20 = preco // 20
preco = preco % 20
notas_10 = preco // 10
preco = preco % 10
notas_5 = preco // 5
preco = preco % 5
notas_2 = preco // 2
preco = preco % 2
notas_1 = preco
print(f"Serão necessárias {notas_50} notas de 50, {notas_20} notas de 20, {notas_10} notas de 10, {notas_5} notas de 5, {notas_2} notas de 2 e {notas_1} notas de 1.")



texto = input("Digite algo: ")
print("Tem espaços em branco? ", " " in texto)
print("É um número? ", texto.isnumeric())
print("É alfabético? ", texto.isalpha())
print("É alfanumérico? ", texto.isalnum())
print("Está em maiúsculo? ", texto.isupper())
print("Está em minúsculo? ", texto.islower())
print("Texto em maiúsculo: ", texto.upper())
print("Texto sem espaços em branco: ", texto.replace(" ", ""))
print("Texto capitalizado: ", texto.capitalize())
print("Texto com título: ", texto.title())


import math
num = float(input('Digite um valor usando . como separador: '))
raiz_quadrada = round(math.sqrt(num), 2)#2 é casas decimais
print("Raiz quadrada:", raiz_quadrada)
potencia = round(num ** 5, 2)#2 é casas decimais
print("Elevado à 5ª potência:", potencia)
print("Arredondado para cima:", math.ceil(num))
print("Arredondado para baixo:", math.floor(num))
print("Parte inteira:", int(num))


num1 = float(input("Digite um número: "))
fatorial = math.factorial(int(num1))
fatorial_limitado = round(fatorial, 2)#o round ele limita o resultado do fatorial a 2 casas
print("Fatorial:", fatorial_limitado)
