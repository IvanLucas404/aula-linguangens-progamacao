notas = []
i = 1

nota = float(input("Nota[0]"))
while nota != -1:
    nota = float(input("nota["+str(i)+"]: "))
    notas.append(nota)
    i+= 1


soma = sum(notas)

media = soma / len(notas)

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')