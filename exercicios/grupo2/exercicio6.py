idade = int(input("Digite uma idade: "))

# idade = int(input("Digite uma idade: "))
if (idade > 0 and idade <= 12):
    print(f"Criança")
elif (idade > 12 and idade < 18):
    print(f"Adolescente")
elif (idade > 17 and idade < 60):
    print(f"Adulta")
elif (idade > 59):
    print(f"Idosa")
else:
    print(f"Idade inválida")
