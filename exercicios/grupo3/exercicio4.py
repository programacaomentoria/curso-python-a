quantidadeItensSoma = 10
somaNumerosPares = 0
contador = 0

while contador <= quantidadeItensSoma:
    ehPar = (contador % 2 == 0)
    if ehPar == True:
        somaNumerosPares += contador
    contador += 1

print(f"A somatoria de numeros pares de 0 a {quantidadeItensSoma} é {somaNumerosPares}")