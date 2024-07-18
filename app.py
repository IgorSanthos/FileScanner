import os
import fnmatch
from tqdm import tqdm


def procurar_string_em_arquivos(diretorio, string_procurada):
    arquivos_encontrados = []
    erros = []

    # Contar a quantidade total de arquivos .txt
    total_arquivos = sum(len(fnmatch.filter(files, '*.txt')) for _, _, files in os.walk(diretorio))

    with tqdm(total=total_arquivos, desc="Procurando arquivos", unit="arquivo") as pbar:
        for raiz, dirs, arquivos in os.walk(diretorio):
            for nome_arquivo in fnmatch.filter(arquivos, '*.txt'):
                caminho_arquivo = os.path.join(raiz, nome_arquivo)
                try:
                    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
                        conteudo = arquivo.read()
                        if string_procurada in conteudo:
                            arquivos_encontrados.append(caminho_arquivo)
                except Exception as e:
                    # Capturando e imprimindo o erro
                    erros.append(f"Erro ao ler {caminho_arquivo}: {str(e)}")
                pbar.update(1)

    if erros:
        print("Erros encontrados durante a leitura dos arquivos:")
        for erro in erros:
            print(erro)

    return arquivos_encontrados

# Exemplo de uso
diretorio = r'C:\Users\Igor\Documents\Arquivos ReceitanetBX'
string_procurada = 'CREDITO DE GAS'
resultados = procurar_string_em_arquivos(diretorio, string_procurada)

if resultados:
    print("Arquivos encontrados contendo a string:")
    for resultado in resultados:
        print(resultado)
else:
    print("Nenhum arquivo contendo a string foi encontrado.")
