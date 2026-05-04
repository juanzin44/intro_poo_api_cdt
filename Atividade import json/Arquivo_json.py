'''
Anotação des explicativas sobre o código em GUI:
'''
import os 
import json

def configurar_sistema():
    if not os.path.exists("uploads_projetos"):
        os.makedirs("uploads_projetos")

def listar_projetos():
    """Lista todos os arquivos JSON na pasta de uploads."""
    arquivos= [f for f in os.listdir("uploads_projetos")if f.endswith(".json")]
    print('\n'+ '=' *40)
    print('  PROJETOS CADASTRADOS')
    print('='*40)

    if not arquivos:
        print("Nenhum projeto encontrado.")
        return[]

for i, arquivo in enumerate(arquivos, 1):
    nome_exibicao = arquivo.replace("projeto_","").replace(".json","").replace("_","")
    print(f"{i}. {nome_exibicao.title()}")

    return arquivos 
def gerenciar_projeto()
    """Permite visualizar e ALTERAR um projeto existente. """
    arquivos = listar projetos()
    if not arquivos: return

    try:
escolha = int(input("\nEscolha o número do projeto para gerenciar(ou 0 para voltar):"))
if escolha ==0: return
nome_arquivo = arquivos[escolha -1]
caminho = f"uploads_projetos/{nome_arquivo}"

with open(caminho, "r", encoding="utf-8")as f:
    dados = json.load(f)

print(f"\n---Dados Atuais---")
print(f"Aluno: {dados['aluno']}")
print(f"Projeto: {dados['projeto']}")

confirmar = input("\nDeseja alterar as informações deste projeto? (s/n):").lower()
if confirmar == 's':
    dados['aluno'] = input(f"Novo nome [{dados['aluno']}]:") or dados ['aluno']
    dados['projeto'] = input(f"Novo resumo:") or dados['projeto']

with open(caminho, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)
print("\n[SUCESSO] projeto atualizado com sucessso!")

except (ValueError, indexError)
    print("[ERRO] Escolha inválida. Voltando ao menu") 

def fazer_upload_json():
    print('\n' + '='*40)
    print('  NOVO UPLOAD DE PROJETO')
    print('='*40)
    nome_aluno = input("Nome do aluno:").strip()
    resumo = input("Resumo do projeto:")

dados = {"aluno":nome_aluno, "projeto": resumo}
nome_fich = nome_aluno.replace("","_").lower()
caminho = f" uploads_projetos/projeto_{nome_fich}.json"

with open(caminho, "w", encoding="utf-8") as f:
    json.dump(dados,f, indent=4, ensure_ascii=false)
print(f"\n[SUCESSO]projeto de {nome_aluno} guardado!")































