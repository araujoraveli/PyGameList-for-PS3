import os
import openpyxl

def ler_base_de_dados(base_de_dados):
    # Dicionário para armazenar correspondências de nomes de arquivos e nomes corretos do jogo
    base_dados_dict = {}
    # Abre o arquivo Excel
    workbook = openpyxl.load_workbook(base_de_dados)
    # Seleciona a primeira planilha
    sheet = workbook.active
    # Itera sobre as linhas da planilha (começando da segunda linha para ignorar cabeçalhos)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        # Adiciona a correspondência ao dicionário
        base_dados_dict[row[0]] = row[1]
    return base_dados_dict

def listar_arquivos_com_extensao(pasta):
    # Lista para armazenar os nomes dos arquivos com extensões
    arquivos = []
    # Itera sobre os arquivos na pasta
    for root, dirs, files in os.walk(pasta):
        for file in files:
            # Verifica se o arquivo possui uma extensão
            if '.' in file:
                arquivos.append(file)
    return arquivos

def criar_gamelist(arquivos, base_dados_dict):
    with open("gamelist.txt", "w") as f:
        for arquivo in arquivos:
            # Extrai o nome do arquivo sem extensão
            nome_arquivo, extensao = os.path.splitext(arquivo)
            # Verifica se o arquivo está na base de dados
            if arquivo in base_dados_dict:
                nome_correto = base_dados_dict[arquivo]
                f.write(f"{nome_arquivo} [{nome_correto}]\n")
            else:
                f.write(f"{arquivo}\n")

def main():
    # Pasta onde o script está sendo executado
    pasta = os.getcwd()
    # Arquivo Excel com a base de dados
    base_de_dados = os.path.join(pasta, "BaseDeDados.xlsx")
    # Ler a base de dados e armazenar em um dicionário
    base_dados_dict = ler_base_de_dados(base_de_dados)
    # Listar arquivos com extensões na pasta atual
    arquivos = listar_arquivos_com_extensao(pasta)
    # Criar gamelist.txt com os nomes corretos dos jogos, se disponíveis
    criar_gamelist(arquivos, base_dados_dict)
    print("gamelist.txt criado com sucesso!")

if __name__ == "__main__":
    main()
