# Calcular fatorial de determinado número.

numero = int(input("Digite um número para calcular sua fatorial: "))
contador = 1
resultado = 1

while contador <= numero:
    resultado = resultado * contador
    contador += 1
print(f"O resultado da fatorial de {numero} é: {resultado}.")