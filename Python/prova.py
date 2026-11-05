from datetime import datetime

# Dicionário com os dados do aluno
aluno = {
    "nome": "Luiz Augusto Xavier de Oliveira",
    "disciplina": "Python Básico",
}

print("\n=======================================\n")
print("============= Cabeçalho Geral =============")

# Acessando os valores do dicionário
print("aluno:", aluno["nome"])
print("disciplina:", aluno["disciplina"])

# Usando f-strings
print(f"👤 Aluno(a): {aluno['nome']}")
print(f"📚 Disciplina: {aluno['disciplina']}")


# Data atual formatada
data_formatada = datetime.now().strftime("%d/%m/%Y")
print(f"🗓 Data: {data_formatada}")

print("===========================================")

# ================================================================
# PROVÃO PRÁTICO PYTHON - GABARITO COMPLETO
# Técnico em Desenvolvimento Web e Mobile
# ================================================================

import random

# VARIÁVEIS GLOBAIS
alunos = []
estoque = {}

# ================================================================
# FUNÇÕES DO SISTEMA 1 - ALUNOS
# ================================================================
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    alunos.append(nome)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLISTA DE ALUNOS")
        for aluno in alunos:
            print(aluno)
        print(f"Total: {len(alunos)} aluno(s)")

def sortear_aluno():
    if len(alunos) == 0:
        print("Cadastre alunos primeiro.")
    else:
        sorteado = random.choice(alunos)
        print(f"Aluno sorteado: {sorteado}")

# ================================================================
# FUNÇÕES DO SISTEMA 2 - ESTOQUE
# ================================================================
def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    estoque[nome] = quantidade
    print("Produto cadastrado.")

def consultar_produto():
    nome = input("Produto para consulta: ")
    if nome in estoque:
        print(f"Quantidade disponível: {estoque[nome]}")
    else:
        print("Produto não encontrado.")

def atualizar_estoque():
    nome = input("Produto: ")
    if nome in estoque:
        nova_qtd = int(input("Nova quantidade: "))
        estoque[nome] = nova_qtd
        print("Estoque atualizado.")
    else:
        print("Produto não encontrado.")

def listar_produtos():
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("ESTOQUE")
        for produto, quantidade in estoque.items():
            print(f"{produto} -> {quantidade}")

# ================================================================
# FUNÇÕES DO SISTEMA 3 - NOTAS
# ================================================================
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def sistema_notas():
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    media = calcular_media(nota1, nota2, nota3)
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    if media >= 7:
        print("Situação: APROVADO")
    elif media >= 5:
        print("Situação: RECUPERAÇÃO")
    else:
        print("Situação: REPROVADO")

# ================================================================
# FUNÇÕES DO SISTEMA 4 - JOGO DA ADIVINHAÇÃO
# ================================================================
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    while True:
        palpite = int(input("Digite um número entre 1 e 10: "))
        tentativas += 1
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
            break
        else:
            print("Tente novamente!")

# ================================================================
# MENU PRINCIPAL
# ================================================================
while True:
    print('=' * 50)
    print('EDUCATIONAL SYSTEM - PRO')
    print('=' * 50)
    print('1 - Cadastro de Alunos')
    print('2 - Listar Alunos')
    print('3 - Sortear Aluno')
    print('4 - Cadastro de Produtos')
    print('5 - Consultar Produto')
    print('6 - Atualizar Estoque')
    print('7 - Listar Produtos')
    print('8 - Sistema de Notas')
    print('9 - Jogo da Adivinhação')
    print('0 - Sair')
    print('=' * 50)
    opcao = input('Escolha uma opção: ')

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        sortear_aluno()
    elif opcao == "4":
        cadastrar_produto()
    elif opcao == "5":
        consultar_produto()
    elif opcao == "6":
        atualizar_estoque()
    elif opcao == "7":
        listar_produtos()
    elif opcao == "8":
        sistema_notas()
    elif opcao == "9":
        jogo_adivinhacao()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida.")
    
