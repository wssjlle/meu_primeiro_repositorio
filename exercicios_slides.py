
def slide97():
    print("Slide 97: Exercício - Criando e acessando itens em uma lista")
    frutas = ["maçã", "banana", "uva"]
    print(frutas[0])
    print(frutas[2])
    print(frutas[-1])

def slide98():
    print("Slide 98: Exercício - Fatiamento de listas")
    numeros = [10, 20, 30, 40, 50]
    print(numeros[1:3])
    print(numeros[:2])
    print(numeros[::-1])

def slide108():
    print("Slide 108: Exercício - Tuplas")
    coordenada = (10, 20)
    cores_primarias = ("vermelho", "azul", "amarelo")
    print(coordenada[0])
    print(cores_primarias[1])

def slide115():
    print("Slide 115: Exercício - Dicionários")
    aluno = {"nome": "Ana", "idade": 22, "curso": "ML e VC"}
    print(aluno["nome"])
    print(aluno.get("telefone", "Telefone não informado"))

def slide120():
    print("Slide 120: Exercício - Dicionários com listas")
    alunos = [
        {"nome": "Alice", "idade": 20, "curso": "Engenharia"},
        {"nome": "Bob", "idade": 22, "curso": "Medicina"},
        {"nome": "Charlie", "idade": 21, "curso": "Direito"}
    ]
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")

def slide121():
    print("Slide 121: Exercício - Dicionários aninhados")
    empresa = {
        "nome": "TechCorp",
        "endereco": {"cidade": "Florianópolis", "estado": "SC"}
    }
 
    print(empresa["endereco"]["cidade"])

def slide122():
    print("Slide 122: Exercício - Percorrendo lista de dicionários com for")
    alunos = [
        {"nome": "Ana", "nota": 8.5},
        {"nome": "Bruno", "nota": 6.0}
    ]
    
    for aluno in alunos:
        if aluno["nota"] >= 7:
            print(aluno["nome"], "foi aprovado")
        else:
            print(aluno["nome"], "foi reprovado")

def slide126():
    print("Slide 126: Exercício - Agenda de contatos com listas e dicionários")
    contatos = []
 
    def adicionar(nome, telefone):
        contatos.append({"nome": nome, "telefone": telefone})
 
    adicionar("Ana", "48 9999-0001")
    adicionar("Bruno", "48 9999-0002")
    
    for contato in contatos:
        print(contato["nome"], "-", contato["telefone"])


# menu para escolher exercício
def exercicio_slides():
    while True:
        print("\nEscolha um exercício:")
        print("1. Slide 97 - Criando e acessando itens em uma lista")
        print("2. Slide 98 - Fatiamento de listas")
        print("3. Slide 108 - Tuplas")
        print("4. Slide 115 - Dicionários")
        print("5. Slide 120 - Dicionários com listas")
        print("6. Slide 121 - Dicionários aninhados")
        print("7. Slide 122 - Percorrendo lista de dicionários com for")
        print("8. Slide 126 - Agenda de contatos com listas e dicionários")
        print("9. Sair")

        opcao = input("Digite o número do exercício desejado: ")


        if opcao == "1":
            slide97()
        elif opcao == "2":
            slide98()
        elif opcao == "3":
            slide108()
        elif opcao == "4":
            slide115()
        elif opcao == "5":
            slide120()
        elif opcao == "6":
            slide121()
        elif opcao == "7":
            slide122()
        elif opcao == "8":
            slide126()
        elif opcao == "9":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    exercicio_slides()