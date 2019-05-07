def code(n):
	for i in range(n):
		ent=str(input())
		x=int(ent[0])
		y=ent[1]
		z=int(ent[2])
		saida=0
		if y.isupper() == True and x != z:
			saida=z-x
			print(saida)
		elif y.isupper()==False and x !=z :
			saida=x+z
			print(saida)
		else:
			saida= x * z
			print(saida)

x=code(int(input()))
