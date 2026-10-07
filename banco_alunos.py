# programa para testar lista de alunos com dicionários

alunos = [
    { "nome": "Alice", "idade": 20, "curso": "Engenharia", "nota": 8.5 },
    { "nome": "Bob", "idade": 22, "curso": "Medicina", "nota": 7.5 },
    { "nome": "Charlie", "idade": 21, "curso": "Direito", "nota": 3.0 },
    { "nome": "Diana", "idade": 23, "curso": "Arquitetura", "nota": 8.0 }
]

aprovados = 0

for aluno in alunos:
    if aluno["nota"] >= 7.0:
        print(f"{aluno['nome']} está aprovado com nota {aluno['nota']}.")
        aprovados += 1

print(f"Total de alunos aprovados: {aprovados}")