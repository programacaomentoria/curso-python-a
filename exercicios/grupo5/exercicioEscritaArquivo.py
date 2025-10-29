# Modos de abertura:
#'r': Leitura (read). É o padrão.
#'w': Escrita (write). Cria o arquivo se não existir, ou sobrescreve se existir.
#'a': Anexar (append). Cria o arquivo se não existir, ou adiciona ao final se existir.
#'x': Criação exclusiva (exclusive creation). Cria o arquivo, mas falha se ele já existir.
#'b': Modo binário (para imagens, áudios, etc.).
#'t': Modo texto (padrão).

def escrever_arquivo_python(nome_arquivo, conteudo):
    """Escreve um conteúdo em um arquivo, sobrescrevendo se existir."""
    try:
        # 'w' abre o arquivo para escrita, sobrescreve se existir
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        print(f"Dados escritos com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")

def adicionar_ao_arquivo_python(nome_arquivo, conteudo):
    """Adiciona um conteúdo ao final de um arquivo."""
    try:
        # 'a' abre o arquivo para adicionar (append)
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write("\n") # Adiciona uma nova linha antes do conteúdo
            arquivo.write(conteudo)
        print(f"Conteúdo adicionado com sucesso ao arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao adicionar ao arquivo: {e}")

# Exemplo de uso
nome_do_arquivo_saida = "saida_python.txt"
escrever_arquivo_python(nome_do_arquivo_saida, "Primeira linha Python.\nSegunda linha Python.")
adicionar_ao_arquivo_python(nome_do_arquivo_saida, "Esta linha foi adicionada depois!")