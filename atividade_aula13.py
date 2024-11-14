# **Exercício 1: Criar e ler um Arquivo**

import os
import shutil

with open('teste.txt', 'r') as arq:
    c = arq.read()
    print(c)

# **Exemplo 2: Entrar em um Diretório**

# with open('arquivo_do_bruno.py', 'w') as pasta:
#     os.mkdir('arquivo_do_bruno.py')

# **Exercício 3: Renomear um Diretório**

# os.rename('arquivo_do_bruno.py', 'banco de dados')

# **Exercício 4: Remover um Diretório**

# shutil.rmtree('c:/Users/aluno/Desktop/aula12/')

# **Exercício 5: Listar Arquivos em um Diretório** 

# with os.scandir('C:/Users/Aluno/Desktop/Aula13 atividade') as entrada:
#     for arquivo in entrada:
#         if arquivo.is_file():
#             print(f'arquivo encontrado: {arquivo.name}')

# **Exercício 6: Copiar Arquivos em um Diretório**

# shutil.copytree('C:/Users/Aluno/Desktop/Aula13 atividade', 'arquivo2')