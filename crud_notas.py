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
    return True

def listar_alunos():
    return carregar_dados()

def atualizar_aluno(indice, novo_nome=None, novas_notas=None):
    dados = carregar_dados()

    if 0 <= indice < len(dados):

        if novo_nome:
            dados[indice]["nome"] = novo_nome

        if novas_notas:
            dados[indice]["notas"] = novas_notas
            dados[indice]["media"] = round(sum(novas_notas) / len(novas_notas), 2)
        
        salvar_dados(dados)

        return True
    return False

def excluir_aluno(indice):
    dados = carregar_dados()

    if 0 <= indice < len(dados):
        dados.pop(indice)
        salvar_dados(dados)
        
        return True
    return False