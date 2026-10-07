# programa para cadastro de alunos usando dicionários 

alunos = {}

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    curso = input("Digite o curso do aluno: ")

    alunos[nome] = {
        "idade": idade,
        "curso": curso
    }

def exibir_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("Alunos cadastrados:")
    for nome, info in alunos.items():
        print(f"Nome: {nome}, Idade: {info['idade']}, Curso: {info['curso']}")

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar aluno")
        print("2. Exibir alunos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            exibir_alunos()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

    