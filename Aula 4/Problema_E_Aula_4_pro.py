def code(n):
	for i in range(n):
		ent=str(input())
		x,y,z,saida=int(ent[0]),ent[1],int(ent[2]),0
		if y.isupper() == True and x != z:
			saida=z-x
			print("%d = %d - %d "%(saida,z,x))
		elif y.isupper()==False and x !=z :
			saida=x+z
			print("%d = %d + %d "%(saida,z,x))
		else:
			saida= x * z
			print("%d = produto de %d e %d "%(saida,z,x))

x=code(int(input()))