qtdeItensSoma = 20
contador = 0
while(contador <= qtdeItensSoma):
    ehImpar = contador %2 == 0
    naoEhDivisivelPorCinco = False
    if ehImpar and naoEhDivisivelPorCinco:
        print(f"Este numero {contador} é ímpar e não divisível por 5")

    contador += 1
