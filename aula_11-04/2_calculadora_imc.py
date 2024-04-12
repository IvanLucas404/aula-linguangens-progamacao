# Este código tenta contar o número de palavras em uma string fornecida pelo usuário.
# No entanto, está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma string, e seu programa deve imprimir o número de palavras nessa string.
# Considere uma palavra como qualquer sequência de caracteres delimitada por espaços.

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Baixo peso"
elif imc < 24.9:
    classificacao = "Peso normal"
elif imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}")
