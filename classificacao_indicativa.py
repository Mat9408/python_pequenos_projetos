idade = int(input(f"Informe sua idade: "))

if (idade >= 18):
    print("Sem restrições de conteúdo.")

elif(idade >= 16 and idade < 18):
    print("Apenas conteúdos com classificação indicativa abaixo de 18 anos.")

elif(idade >= 14 and idade < 16):
    print("Apenas conteúdos com classificação indicativa abaixo de 16 anos.")

elif(idade >= 12 and idade < 14):
    print("Apenas conteúdos com classificação indicativa abaixo de 14 anos.")

elif(idade >= 10 and idade < 12):
    print("Apenas conteúdos com classificação indicativa abaixo de 12 anos.")

elif(idade < 10):
    print("Apenas conteúdos livres para todos os públicos.") 