def escreveLinhaCabecalho():
    print("==============================")

def escreveCabecalho(mensagem):
    escreveLinhaCabecalho()
    print(f"{mensagem}")
    escreveLinhaCabecalho()

escreveCabecalho("Perguntas - Nome e idade")
nome = input("Escreva seu nome: ")
idade = input("Escreva sua idade: ")
print(f"Seu nome é: {nome} e sua idade: {idade}")