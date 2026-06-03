# Sistema de Gerenciamento de Notas PIT

Projeto desenvolvido para a disciplina de **Algoritmos e Programação** do 1º período do curso de **Bacharelado em Inteligência Artificial** do **Piauí Instituto de Tecnologia (PIT)**.

## Descrição do Projeto

O sistema tem como objetivo realizar o gerenciamento acadêmico de alunos da faculdade PIT, permitindo o armazenamento permanente dos dados por meio de arquivos JSON.

O software implementa um CRUD completo (**Create, Read, Update e Delete**) utilizando listas de dicionários para armazenar informações dos alunos, aplicando os conceitos estudados durante a disciplina.

## Funcionalidades

* **Cadastrar Aluno:** adiciona um novo aluno ao sistema, registrando suas notas e calculando automaticamente a média.
* **Listar Alunos:** exibe todos os alunos cadastrados juntamente com suas respectivas médias.
* **Remover Aluno:** exclui registros do sistema por meio da seleção do índice correspondente.
* **Persistência de Dados:** armazena todas as informações no arquivo `notas_alunos.json`, garantindo que os dados permaneçam disponíveis mesmo após o encerramento da aplicação.

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Biblioteca:** `json` (biblioteca nativa para serialização e persistência de dados)

## Estrutura do Projeto

O sistema foi organizado de forma modular para facilitar a manutenção e a reutilização do código:

### `main.py`

Responsável pela interface com o usuário, exibição do menu principal e controle da navegação utilizando a estrutura `match...case`.

### `crud_notas.py`

Contém as funções responsáveis pela lógica de negócio, manipulação dos dados, leitura e gravação de arquivos JSON, além do tratamento de exceções utilizando `try...except`.

## Desafios Encontrados

Durante o desenvolvimento, um dos principais desafios foi garantir a integridade dos dados durante a exclusão de registros da lista de alunos. Também foi necessário tratar adequadamente a conversão de tipos de dados e lidar com situações em que o arquivo JSON ainda não existia, evitando falhas na execução do programa.

## Uso de Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio ao desenvolvimento do projeto, auxiliando em:

1. Estruturação da arquitetura modular do sistema, separando as responsabilidades entre os arquivos `main.py` e `crud_notas.py`.
2. Implementação de boas práticas de programação, incluindo tratamento de erros com `try...except`.
.

## Equipe

* Adler
* Arthur
* Mateus

---

# Referências

## Materiais da Disciplina (PIT)

* Fundamentos de Lógica e Python
* Estruturas Condicionais
* Estruturas de Repetição
* Manipulação de Listas
* Funções e Modularização
* Uso de Bibliotecas
* Dicionários e Listas de Dicionários
* Persistência de Arquivos e JSON

## Fontes Técnicas de Consulta

* CRUD em Python com JSON. Disponível em: [https://github.com/VILHALVA/CRUD-PYTHON-EM-JSON](https://github.com/VILHALVA/CRUD-PYTHON-EM-JSON)
* Tutorial: Como Fazer CRUD em JSON com Python. Disponível em: [https://projetocybernetico.blogspot.com](https://projetocybernetico.blogspot.com)
* Diferença entre dump, dumps, load e loads em JSON. Disponível em: [https://www.dicas-de-django.com.br](https://www.dicas-de-django.com.br)
* Lista de Exercícios: Manipulação de Arquivos JSON. Disponível em: [https://pt.scribd.com](https://pt.scribd.com)

## Vídeos de Apoio

* Python – Manipulação de Arquivos JSON
* Como Salvar e Carregar Listas em JSON
* Estrutura de Dados: Dicionários no Python
* Introdução a Sistemas de Gerenciamento