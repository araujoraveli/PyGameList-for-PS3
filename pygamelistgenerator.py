import os
import openpyxl
import tkinter as tk
from tkinter import messagebox

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
            if '.zip' in file:
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
                f.write(f"{nome_arquivo}.zip [{nome_correto}]\n")
            else:
                f.write(f"{arquivo} [{arquivo}]\n")

def mostrar_mensagem_sucesso():
    # Cria a janela principal
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    # Exibe a mensagem de sucesso
    messagebox.showinfo("PS3 gamelist.txt generator", "O gamelist.txt foi criado com sucesso!\n\nCaso algum jogo nao tenha sido encontrado na base de dados ele estará com o mesmo nome do arquivo .zip original no gamelist.txt.\nEdite a base de dados, inclua manualmente e execute novamente o programa para atualizar o gamelist.txt!\n\n\nGithub @araujoraveli")
    root.destroy()  # Fecha a janela principal

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
    # Exibir a mensagem de sucesso
    mostrar_mensagem_sucesso()

if __name__ == "__main__":
    main()
