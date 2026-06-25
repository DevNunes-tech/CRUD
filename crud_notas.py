import json

FILE_NAME = "notas_alunos.json"

def carregar_dados():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_dados(dados):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def adicionar_aluno(nome, notas):
    dados = carregar_dados()
    media = sum(notas) / len(notas)
    novo_aluno = {"nome": nome, "notas": notas, "media": round(media, 2)}
    dados.append(novo_aluno)
    salvar_dados(dados)
    print(f"Sucesso: {nome} adicionado com média {novo_aluno['media']}.")

def listar_alunos():
    dados = carregar_dados()
    if not dados:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- Lista de Alunos ---")
    for i, aluno in enumerate(dados):
        print(f"{i} | Nome: {aluno['nome']} | Notas: {aluno['notas']} | Média: {aluno['media']}")

def atualizar_aluno(indice, novo_nome=None, novas_notas=None):
    dados = carregar_dados()
    if 0 <= indice < len(dados):
        aluno = dados[indice]

        if novo_nome:
            aluno["nome"] = novo_nome

        if novas_notas:
            aluno["notas"] = novas_notas
            aluno["media"] = round(sum(novas_notas) / len(novas_notas), 2)
        
        salvar_dados(dados)

        print(f"{novo_nome} atualizado com sucesso.")
    else:
        print("Erro: Índice inválido.")

def excluir_aluno(indice):
    dados = carregar_dados()
    if 0 <= indice < len(dados):
        removido = dados.pop(indice)
        salvar_dados(dados)
        print(f"Aluno {removido['nome']} excluído com sucesso.")
    else:
        print("Erro: Índice inválido.")