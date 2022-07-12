for contador in range(1,16):
    if (contador % 3 ==0):
        print(contador)
    if (contador == 10):
        print("Saindo do laço!")
        print("Não será exibido.")
        break
print("Fim do programa!")