def aula_tratamento_erros():
    print("---desafio 1: divisao ---")
try:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        resultado = numerador / denominador
        print(f"O resultado da divisão é: {resultado}")
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: O denominador não pode ser zero.")
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
else:
    print(f"Sucesso! O resultado da divisão é: {resultado}")
finally:
    print("---fim da divisao ---")
aula_tratamento_erros()
















