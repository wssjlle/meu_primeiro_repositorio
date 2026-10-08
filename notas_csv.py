# importar biblioteca csv
import csv

# limpa o arquivo resultado.csv antes de escrever os resultados
with open('resultado.csv', mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=['nome', 'media', 'resultado'])
    escritor_csv.writeheader()

# ler notas do arquivo notas.csv
with open('notas.csv', mode='r') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)

    # calcular a média das notas e imprimir o resultado
    for linha in leitor_csv:
        nota1 = float(linha['nota1'])
        nota2 = float(linha['nota2'])
        media = (nota1 + nota2) / 2
        # adicionar nome, média e resultado no arquivo resultado.csv
        with open('resultado.csv', mode='a', newline='') as arquivo_csv:
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=['nome', 'media', 'resultado'])
            resultado = 'Aprovado' if media >= 7 else 'Reprovado'
            escritor_csv.writerow({'nome': linha['nome'], 'media': media, 'resultado': resultado})