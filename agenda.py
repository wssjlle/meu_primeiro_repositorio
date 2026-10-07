# cadastro de alunos usando listas e dicionarios

alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    curso = input("Digite o curso do aluno: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)

def listar_alunos():
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")

def pesquisar_aluno():
    nome = input("Digite o nome do aluno a ser pesquisado: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print(f"Aluno encontrado: Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")
            return
    print("Aluno não encontrado.")

def excluir_aluno():
    nome = input("Digite o nome do aluno a ser excluído: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            alunos.remove(aluno)
            print(f"Aluno {nome} excluído com sucesso.")
            return
    print("Aluno não encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Pesquisar aluno")
        print("4. Excluir aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            pesquisar_aluno()
        elif opcao == "4":
            excluir_aluno()
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()  

    