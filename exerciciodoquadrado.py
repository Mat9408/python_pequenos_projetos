# Exercício do quadrado dos números inteiros entre 15 e 200.

contador = 15
numero = 15
resultado = None

while(contador < 201):
    resultado = numero * numero
    print(f"O número {numero} ao quadrado é: {resultado}.")
    contador += 1
    numero += 1