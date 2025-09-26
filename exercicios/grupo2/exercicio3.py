numero = int(input("Digite um numero e descubra se é divisível por 3 ou não: "))
ehDivisivelPor3 = False
ehDivisivelPor3 = (numero != 0 and numero % 3 == 0)

if(ehDivisivelPor3 == True):
    print(f"O numero {numero} é divisível por 3")
else:
    print(f"O numero {numero} não é divisível por 3")
    