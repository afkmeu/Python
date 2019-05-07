
# Função que retorna a média de cada aluno e diz se está aprovado ou reprovado
def mediaAlunos(alunos,notas,minimo): # Cria a função mediaAlunos com os parâmetros alunos, notas e mínimo
	#Loop 1 verifica os alunos aprovados
	for i in range(len(alunos)): # Loop onde i é o comprimento da lista alunos
		media = (notas[i][0]+notas[i][1]+notas[i][2])/3 # A variável média recebe a soma das notas   
		if media >= minimo: # Compara se a média do aluno no índice i for maior ou igual ao valor mínimo
			print(f'{alunos[i]} Aprovado com média{media:.2f}') # Exibe o nome do aluno ... e a média formatada com duas casas decimais depois do ponto
	print('~'* 25) # Exibe o caractere ~ 25 vezes
# Loop 2 verifica os alunos reprovados
	for i in range(len(alunos)): # Loop onde i é o comprimento da lista alunos
		media = (notas[i][0]+notas[i][1]+notas[i][2])/3 # A variável média recebe a soma das notas
		if media < minimo: # Compara se a média do aluno no índice i for maior ou igual ao valor mínimo
			print(f'{alunos[i]} Reprovado com média{media:.2f}')# Exibe o nome do aluno ... e a média formatada com duas casas decimais depois do ponto
	return None
# lista com nome dos alunos
alunos=["a","b","c"]  
# Lista que contem listas com as notas dos alunos
notas=[[3.2,4.5,4.0], 
       [7.1,8.0,9.0],
	   [5.6,8.0,9.9]]
# Chamada da função mediaAlunos
#%%
mediaAlunos(alunos,notas,6)