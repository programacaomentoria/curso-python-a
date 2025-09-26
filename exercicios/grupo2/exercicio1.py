textoNumerico = input("Digite um numero e descubra se é par ou ímpar: ")    #"3"
numero = int(textoNumerico)     
restoDaDivisao = numero % 2
isPar = restoDaDivisao == 0

if (isPar == True):
    print(f"O numero {numero} é par!")
else:
    print(f"O numero {numero} é ímpar!")