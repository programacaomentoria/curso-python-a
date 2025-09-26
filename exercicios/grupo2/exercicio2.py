numero = int(input("Digite um numero e descubra se é primo ou não: "))
isPrimo = False
if(numero < 4):
    isPrimo = True
else:
    isPrimo = (numero % 2 != 0) and (numero % 3 != 0) and (numero % 5 != 0) and (numero % 7 != 0)

if(isPrimo == True):
    print(f"O numero {numero} é primo")
else:
    print(f"O numero {numero} não é primo")
    