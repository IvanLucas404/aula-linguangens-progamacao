# O código abaixo tem alguns problemas e está incompleto! 
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

valor1 = input("Digite o primeiro valor (ou -1 para sair): ")

while valor1 != '-1':
    operador = input("Digite o operador (+, -, *, /): ")
    valor2 = input("Digite o segundo valor: ")

    valor1 = float(valor1)
    valor2 = float(valor2)

    resultado = 0
    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        resultado = valor1 / valor2
    
    print("Resultado:", resultado)

    valor1 = input("Digite o primeiro valor (ou -1 para sair): ")
    
print("Programa encerrado.")
