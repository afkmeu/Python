# Função que retorna a média de cada aluno e diz se está aprovado ou reprovado
def mediaAlunos(infos,minimo): # Cria a função mediaAlunos com os parâmetros alunos, notas e mínimo
	#Loop 1 verifica os alunos aprovados
	for i in range(len(infos)): # Loop onde i é o comprimento da lista alunos
		media = (infos[i][1][0]+infos[i][1][1]+infos[i][1][2])/3 # A variável média recebe a soma das notas   
		if media >= minimo: # Compara se a média do aluno no índice i for maior ou igual ao valor mínimo
			print(f'{infos[i][i]} Aprovado com média{media:.2f}') # Exibe o nome do aluno ... e a média formatada com duas casas decimais depois do ponto
	print('~'* 25) # Exibe o caractere ~ 25 vezes
# Loop 2 verifica os alunos reprovados
	for i in range(len(infos)): # Loop onde i é o comprimento da lista alunos
		media = (infos[i][1][0]+infos[i][1][1]+infos[i][1][2])/3 # A variável média recebe a soma das notas
		if media < minimo: # Compara se a média do aluno no índice i for maior ou igual ao valor mínimo
			print(f'{infos[i]} Reprovado com média{media:.2f}')# Exibe o nome do aluno ... e a média formatada com duas casas decimais depois do ponto
	return None
def lerAlunosNotas(qtdAlunos,qtdNotas):
    saida=[]
    for indAluno in range(qtdAlunos):
        nome=input(f'Insira o nome do aluno {indAluno + 1}')
        linha=[nome,[]]
        for indNotas in range(qtdNotas):
            nota=float(input(f'Insira a nota {indNotas + 1}'))
            linha[1].append(nota)
        saida.append(linha)
    return saida
resultado=lerAlunosNotas(3,3)
mediaAlunos(resultado,6)

