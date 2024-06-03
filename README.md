# Gerador de gamelist.txt em python para JOGOS ARCADE do RetroarchCE + WebmanMOD para Playstation3

## Descrição
Os arquivos dos jogos de arcade nao podem ter seu nome alterado pois param de funcionar, o que impossibilita uma melhor organização da biblioteca de jogos.
Este script em python e base de dados em excel foram criados na intensão de automatizar e aplicar os nomes corretos nos jogos de ARCADE (MAME, FBNEO, etc...) de forma mais prática e massiva
gerando o arquivo gamelist.txt com as devidas informações e formatações necessárias para reconhecimento e listagem no WebmanMOD.

## Funcionalidades
  - Lista arquivos em uma pasta.
  - Busca nomes corretos dos jogos em um arquivo Excel (database).
  - Cria um arquivo "gamelist.txt" com os nomes corretos dos jogos.

## Requisitos

- [Python 3.x](https://www.python.org/downloads/)
- Pacote Python necessário: openpyxl (caso for editar o código)

## Como Usar

1. Baixe os arquivos deste repositório:
   - BaseDeDados.xlsx
   - pygamelistgenerator.py
2. Coloque ambos no mesmo diretório das suas ROMS de ARCADE e execute o `pygamelistgenerator.py`
3. Verifique o arquivo `gamelist.txt` criado na mesma pasta, estando ok, só enviar os jogos e o `gamelist.txt` para a pasta correta no PS3 e atualizar a lista de jogos via WebmanMOD

## Finalizando...
Agradecimentos ao @aldostools pela implementação recente deste recurso no WebmanMOD!
- [@aldostools/webMAN-MOD](https://github.com/aldostools/webMAN-MOD)
