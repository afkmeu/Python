#Aula 4, Funções
#Def + nomeEscolhido+(lista de parâmetros):
def trocar(valores,pos1,pos2):
	temp=valores[pos1]
	valores[pos1]=valores[pos2]
	valores[pos2]=temp
	return None

amigas=["maria","Regina","Eliana","Angélica"]
trocar(amigas,0,4)
print(amigas)