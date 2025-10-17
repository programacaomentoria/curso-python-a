def verificarSeEhPrimo(contador):
    ehPrimo = False
    if contador == 1:
        ehPrimo = False
    elif contador < 4:
        ehPrimo = True
    else:
        ehPrimo = True
        controle = contador - 1
        while controle > 1:
            if contador % controle == 0:
                ehPrimo = False
                break
            controle = controle - 1

    return ehPrimo

soma = 0
quantidadeItensSoma = 100
contador = 0

while contador <= quantidadeItensSoma:
    ehPrimo = verificarSeEhPrimo(contador)
    if ehPrimo:
        soma = soma + contador
    contador = contador + 1

print(f"A somatoria de numeros primos ate {quantidadeItensSoma} é {soma}")
