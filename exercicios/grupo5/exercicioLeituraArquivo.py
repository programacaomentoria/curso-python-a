def ler_arquivo_python(nome_arquivo):
    """Lê e imprime o conteúdo de um arquivo de texto."""
    try:
        # 'with open(...)' garante que o arquivo será fechado automaticamente
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(f"Conteúdo do arquivo {nome_arquivo}:")
            for linha in arquivo:
                print(linha.strip()) # .strip() remove quebras de linha e espaços em branco extras
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# Para testar: crie um arquivo 'exemplo.txt' com algum texto
ler_arquivo_python("exemplo.txt")