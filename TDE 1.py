#Exercicio 01

#n = int(input("Digite um número para ver o seu sucessor e seu antecessor: "))
#print(f"O sucessor de {n} é {n + 1} e o seu antecessor é { n - 1}")

#Exercicio 02

#idade = int(input("Digite seu ano de nascimento: "))
#print(f"Em 2032 você terá {2032 - idade} anos.")

#Exercicio 03

#salario = float(input("Qual o seu salário atual? "))
#salario_minimo = float(input("Qual é o salário mínimo nos dias de hoje? "))
#print(f"Você ganha {salario/salario_minimo:.1f} salários-mínimos.")

#Exercicio 04

#diametro = float(input("Digite um diametro para calcular a area do círculo: "))
#print(f"A área do circulo é {diametro ** 2 * 0.7854:.2f} centimetros quadrados.")

#Exercicio 05

#produto = float(input("Digite o preço do produto: "))
#print(f"O valor da compra em 3x com 5% de juros fica 3x de {(produto+(produto*5)/100)/3:.2f}R$.\n"
#      f"O valor da compra em 2x fica 2x de {produto/2:.2f}R$.\n"
#      f"O valor da compra a vista tem 5% de desconto e fica {produto-(produto*5)/100:.2f}R$.")

#Exercicio 06
import math
#c1 = int(input("Digite um número: "))
#c2 = int(input("Digite outro número: "))
#print(f"A hipotenusa é {math.hypot(c1, c2)}")

#Exercicio 07

#hora = int(input("Digite as horas: "))
#minutos = int(input("Digite os minutos: "))
#segundos = int(input("Digite os segundos: "))
#print(f"O total de minutos decorridos ate agora foram {minutos + (hora*60) + (segundos/60)} minutos.\n"
#      f"O total de segundos decorridos ate agora foram {segundos + (minutos*60) + (hora*3600)} segundos.")

#Exercicio 08

#altura = float(input("Digite a altura do cilindro: "))
#raio = int(input("Digite o raio do cilindro: "))
#area = 2*(3.14*raio**2) + 2*(3.14*raio*altura)
#latas = area/15
#print(f"A quantidade de latas de tintas necessarias para pintar são {latas:.0f} latas.\n"
#      f"E você gastará {latas * 50:.2f}R$ para comprar as latas.")