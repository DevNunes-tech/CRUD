# Sistema de Gerenciamento de Notas PIT

Projeto desenvolvido para a disciplina de **Algoritmos e Programacao** do 1º periodo do curso de **Bacharelado em Inteligencia Artificial** do **Piaui Instituto de Tecnologia (PIT)**.

A disciplina e ministrada pela professora **Evelyn Karinne Macedo Mota Silva**.

**E-mail da professora:** [evelyn.silva@pitpiaui.com](mailto:evelyn.silva@pitpiaui.com)

## Descricao do Projeto

O sistema realiza o gerenciamento de notas de alunos por meio de uma aplicacao web criada com **Streamlit**. A aplicacao permite cadastrar, listar, atualizar e remover alunos, mantendo os dados salvos em um arquivo JSON.

O projeto implementa um CRUD completo (**Create, Read, Update e Delete**) usando listas de dicionarios em Python e persistencia local no arquivo `notas_alunos.json`.

## Funcionalidades

* **Cadastrar Aluno:** registra o nome do aluno, duas notas e calcula automaticamente a media.
* **Listar Alunos:** exibe todos os alunos cadastrados com suas notas e medias.
* **Atualizar Aluno:** permite alterar o nome e as notas de um aluno cadastrado.
* **Remover Aluno:** exclui um aluno selecionado pelo usuario.
* **Persistencia de Dados:** salva os registros no arquivo `notas_alunos.json`.

## Tecnologias Utilizadas

* **Python 3:** linguagem principal do projeto.
* **Streamlit:** framework utilizado para criar a interface web.
* **JSON:** formato usado para armazenar os dados dos alunos.
* **Biblioteca `json`:** biblioteca nativa do Python usada para ler e salvar o arquivo JSON.

## Como Executar o Projeto

1. Instale as dependencias:

```bash
pip install -r requirements.txt
```

2. Execute a aplicacao:

```bash
streamlit run main.py
```

3. Abra no navegador o endereco exibido pelo Streamlit.

## Estrutura do Projeto

```text
CRUD/
├── main.py
├── crud_notas.py
├── requirements.txt
├── .gitignore
├── notas_alunos.json
└── README.md
```

### `main.py`

Arquivo responsavel pela interface web em Streamlit. Ele exibe o menu lateral e as telas de cadastro, listagem, atualizacao e remocao de alunos.

### `crud_notas.py`

Arquivo responsavel pela logica do CRUD. Ele contem as funcoes para carregar dados, salvar dados, adicionar aluno, listar alunos, atualizar aluno e excluir aluno.

### `notas_alunos.json`

Arquivo criado automaticamente para guardar os dados cadastrados. Ele nao precisa ser enviado para o GitHub, pois representa dados locais gerados durante o uso do sistema.

## Uso de Inteligencia Artificial

A Inteligencia Artificial utilizada para transformar e documentar o projeto foi o **Codex, baseado no GPT-5, da OpenAI**.

A IA foi utilizada como apoio para adaptar o projeto para Streamlit, organizar a documentacao, preencher o `.gitignore`, criar o `requirements.txt` e melhorar as referencias do README.

### Prompts Utilizados

1. **Transformacao para Streamlit**

```text
Transforme este projeto Python de CRUD de notas para Streamlit, mantendo a logica existente e criando uma interface web para cadastrar, listar, atualizar e remover alunos.
```

2. **Atualizacao do README**

```text
Atualize o README seguindo as orientacoes da atividade, informando a IA utilizada e todos os prompts usados para transformar o projeto em Streamlit.
```

## Links do Projeto

* **Repositorio no GitHub:** https://github.com/DevNunes-tech/CRUD
* **Aplicacao no Streamlit:** [https://pitcrud.streamlit.app/](https://pitcrud.streamlit.app/)

## Equipe

* **Adler Jose da Silva Oliveira** - [alunoadler@gmail.com](mailto:alunoadler@gmail.com)
* **Arthur Daladier Beserra da Silva** - [rthurvxdala@gmail.com](mailto:rthurvxdala@gmail.com)
* **Mateus Oliveira Nunes** - [mateusoliveiranunes2@gmail.com](mailto:mateusoliveiranunes2@gmail.com)


---

# Referencias

## Materiais da Disciplina (PIT)

* Fundamentos de Logica e Python.
* Estruturas Condicionais.
* Estruturas de Repeticao.
* Manipulacao de Listas.
* Funcoes e Modularizacao.
* Uso de Bibliotecas.
* Dicionarios e Listas de Dicionarios.
* Persistencia de Arquivos e JSON.

## Python e JSON

* PYTHON SOFTWARE FOUNDATION. **The Python Tutorial: Data Structures**. Disponivel em: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html). Acesso em: 25 jun. 2026.
* PYTHON SOFTWARE FOUNDATION. **json - JSON encoder and decoder**. Disponivel em: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html). Acesso em: 25 jun. 2026.
* JSON.ORG. **Introducing JSON**. Disponivel em: [https://www.json.org/json-en.html](https://www.json.org/json-en.html). Acesso em: 25 jun. 2026.

## Streamlit

* STREAMLIT. **Installation**. Disponivel em: [https://docs.streamlit.io/get-started/installation](https://docs.streamlit.io/get-started/installation). Acesso em: 25 jun. 2026.
* STREAMLIT. **st.sidebar**. Disponivel em: [https://docs.streamlit.io/develop/api-reference/layout/st.sidebar](https://docs.streamlit.io/develop/api-reference/layout/st.sidebar). Acesso em: 25 jun. 2026.
* STREAMLIT. **st.selectbox**. Disponivel em: [https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox](https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox). Acesso em: 25 jun. 2026.
* STREAMLIT. **st.number_input**. Disponivel em: [https://docs.streamlit.io/develop/api-reference/widgets/st.number_input](https://docs.streamlit.io/develop/api-reference/widgets/st.number_input). Acesso em: 25 jun. 2026.
* STREAMLIT. **st.table**. Disponivel em: [https://docs.streamlit.io/develop/api-reference/data/st.table](https://docs.streamlit.io/develop/api-reference/data/st.table). Acesso em: 25 jun. 2026.

## CRUD e Inteligencia Artificial

* WIKIPEDIA. **Create, read, update and delete**. Disponivel em: [https://en.wikipedia.org/wiki/Create,_read,_update_and_delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete). Acesso em: 25 jun. 2026.
* OPENAI. **Codex**. Disponivel em: [https://developers.openai.com/codex](https://developers.openai.com/codex). Acesso em: 25 jun. 2026.