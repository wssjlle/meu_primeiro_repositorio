# Criação do arquivo diário.txt e escrita de uma linha nele

# função para criar o arquivo diário.txt e escrever uma linha nele
def criar_arquivo():
    with open("diario.txt", "w") as arquivo:
        arquivo.write("Diário de Bordo\n")
        arquivo.write("================\n")


# função para digitar a frase que será gravada no arquivo diário.txt
def digitar_frase():
    frase = input("Digite a frase que deseja gravar no diário: ")
    return frase

# função para gravar a frase digitada no arquivo diário.txt
def gravar_frase(frase):
    with open("diario.txt", "a") as arquivo:
        arquivo.write(frase + "\n")

# função para ler o conteúdo do arquivo diário.txt
def ler_arquivo():
    with open("diario.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("\nConteúdo do diário:")
        print(conteudo)

# função principal do programa
def main():
    criar_arquivo()
    while True:
        print("\nMenu:")
        print("1. Digitar frase")
        print("2. Ler diário")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            frase = digitar_frase()
            gravar_frase(frase)
        elif opcao == "2":
            ler_arquivo()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()