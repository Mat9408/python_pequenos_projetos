#Construir um programa que apresente a soma dos cem primeiros números naturais.

soma = 0
for contador in range(0,101):
    soma += contador
print(f"A soma dos 100 primeiros números naturais é: {soma}.")
