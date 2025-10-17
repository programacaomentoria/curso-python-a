numeroFatorial = int(input("Digite um numero para calcular o fatorial: "))
calculoFatorial = 1
contador = numeroFatorial
while contador > 0:
    calculoFatorial = calculoFatorial * contador
    contador = contador - 1

print(f"O fatorial de {numeroFatorial} é {calculoFatorial}")