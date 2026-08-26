# -- LIVE CODE: Aula 7 - Exceções e Sets ---
# Codificando no PyCharm

from datetime import datetime

print("\n-------------------------------")
print("         CABEÇALHO GERAL         ")
print("-------------------------------")

aluno = {
    "nome": "Luiz Augusto",
    "disciplina": "Python Básico",
}

# Usando as F-STRINGS e acessando as chaves
print(f" Aluno(a): {aluno["nome"]}")
print(f" Disciplina: {aluno["disciplina"]}")

# Data atual formatada
data_formatada = datetime.now().strftime("%d/%m/%y")
print(f"Data {data_formatada}")

print("-------------------------------")

print("=== SISTEMA DE HIGIENIZAÇÃO DE DADOS ===")

# 1. Criando uma lista de cadastros que possui elementos duplicados
lista_suja = ["Ana", "Carlos", "Ana", "Beatriz", "Carlos"]

# Convertendo para Set (Conjunto) para eliminar duplicatas automaticamente!
conjunto_limpo = set(lista_suja)

print(f"Lista original (com duplicados): {lista_suja}")
print(f"Conjunto final (Sets removem duplicados): {conjunto_limpo}\n")

# 2. Protegendo o código contra erros com try/except 
try:
    # Se o usuário digitar letras ou o número zero, o programa não travará!
    numero = int(input("Digite um número inteiro divisor de 100:"))
    resultado = 100 / numero
    print(f"Sucesso! O resultado da divisão de 100 por {numero} é {resultado:2f}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros válidos!")

except Exception as erro_inesperado:
    print(f" ocorreu um erro desconhecido: {erro_inesperado}")

finally:
    print("\nExeecução da análise segura finalizada com sucesso.")
    print("================================================")
