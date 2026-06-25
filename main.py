import streamlit as st
import crud_notas

st.title("📚 Sistema de Notas PIT")

menu = st.sidebar.selectbox(
    "Escolha uma opção",
    ["Cadastrar", "Listar", "Atualizar", "Remover"]
)

# CADASTRAR
if menu == "Cadastrar":
    st.header("Cadastrar Aluno")

    nome = st.text_input("Nome do aluno")
    n1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0)
    n2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0)

    if st.button("Cadastrar"):
        crud_notas.adicionar_aluno(nome, [n1, n2])
        st.success("Aluno cadastrado com sucesso!")

# LISTAR
elif menu == "Listar":
    st.header("Lista de Alunos")

    dados = crud_notas.carregar_dados()

    if dados:
        st.table(dados)
    else:
        st.warning("Nenhum aluno cadastrado.")

# ATUALIZAR
elif menu == "Atualizar":
    st.header("Atualizar Aluno")

    dados = crud_notas.carregar_dados()

    if dados:
        nomes = [f"{i} - {a['nome']}" for i, a in enumerate(dados)]

        escolha = st.selectbox("Escolha o aluno", nomes)

        idx = int(escolha.split(" - ")[0])

        novo_nome = st.text_input("Novo nome")

        n1 = st.number_input("Nova Nota 1", min_value=0.0, max_value=10.0)
        n2 = st.number_input("Nova Nota 2", min_value=0.0, max_value=10.0)

        if st.button("Atualizar"):
            crud_notas.atualizar_aluno(idx, novo_nome, [n1, n2])
            st.success("Aluno atualizado!")

# REMOVER
elif menu == "Remover":
    st.header("Remover Aluno")

    dados = crud_notas.carregar_dados()

    if dados:
        nomes = [f"{i} - {a['nome']}" for i, a in enumerate(dados)]

        escolha = st.selectbox("Escolha o aluno", nomes)

        idx = int(escolha.split(" - ")[0])

        if st.button("Remover"):
            crud_notas.excluir_aluno(idx)
            st.success("Aluno removido!")