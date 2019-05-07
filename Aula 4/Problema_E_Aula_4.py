cache=[]
def code(n):
	for i in range(n):
		ent=str(input())
		x,y,z,saida=int(ent[0]),ent[1],int(ent[2]),0
		if y.isupper() == True and x != z:
			saida=z-x
			print(saida)
			cache.append(saida)
		elif y.isupper()==False and x !=z :
			saida=x+z
			print(saida)
			cache.append(saida)
		else:
			saida= x * z
			print(saida)
			cache.append(saida)
	print(cache)
x=code(int(input()))