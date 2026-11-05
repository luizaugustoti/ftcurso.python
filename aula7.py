from datetime import datetime

print("\n-------------------------------")
print("         CABEÇALHO GERAL         ")
print("-------------------------------")

aluno = {
    "nome": "Luiz augusto",
    "disciplina": "Python Básico",
}

# Usando as F-STRINGS e acessando as chaves
print(f" Aluno(a): {aluno["nome"]}")
print(f" Disciplina: {aluno["disciplina"]}")

# Data atual formatada
data_formatada = datetime.now().strftime("%d/%m/%y")
print(f"Data {data_formatada}")

print("-------------------------------")

print("--- COLETOR DE CADASTROS ÚNICOS---")
cpfs_cadastrados = set() # Criando um conjutos vazio
while True:
    try:
        #strip remove espaços em branco invisíveis
        entrada = input("Digite o CPF (apenas números inteiros) ou 'sair:'").strip()

        if entrada.lower() == 'sair':
            break
        # Tenta converter a entrada em número para validar se digitaram apenas dígitos
        cpf = int(entrada)

        # Se for um CPF válido, adiciona ao Set
        cpfs_cadastrados.add(cpf)

        print("CPF registrado com sucesso!")
        except ValueError:
        print("Erro: Digite apenas números inteiros válidos para o CPF!")

print("\n--- CADASTROS REGISTRADOS (SEM DUPLICATAS) ---")
print(cpfs_cadastrados)
print("--------------------------------")
