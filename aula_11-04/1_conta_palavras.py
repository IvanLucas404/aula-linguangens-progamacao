# Este código tenta contar o número de palavras em uma string fornecida pelo usuário.
# No entanto, está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma string, e seu programa deve imprimir o número de palavras nessa string.
# Considere uma palavra como qualquer sequência de caracteres delimitada por espaços.

texto = input("Digite um texto: ")

palavras = texto.split()

numero_de_palavras = len(palavras)

print("O número de palavras é: ",(numero_de_palavras))