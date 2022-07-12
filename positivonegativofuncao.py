def num(n):
    if (n > 0):
        print("Número positivo")
    elif (n == 0):
        print("Número nulo")
    else:
        print("Número negativo")

print("Positivo ou Negativo")    
n = int(input("Digite um número: "))
print(f"Este número é," ,end=" ")
num(n) 