import crud_notas

def menu():
    while True:
        print("\n--- SISTEMA DE NOTAS PIT ---")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Remover Aluno")
        print("4. Sair")
        
        op = input("Escolha uma opção: ")
        
        if op == "1":
            nome = input("Nome do aluno: ")
            n1 = float(input("Nota 1: "))
            n2 = float(input("Nota 2: "))
            crud_notas.adicionar_aluno(nome, [n1, n2])
        elif op == "2":
            crud_notas.listar_alunos()
        elif op == "3":
            crud_notas.listar_alunos()
            idx = int(input("Digite o ID do aluno a remover: "))
            crud_notas.excluir_aluno(idx)
        elif op == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()