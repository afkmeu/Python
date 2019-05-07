#Passagem de função por parâmetro
def media(a,b,c,d):
	return (a+b+c+d)/4

def sit(a,b,c,d):
	x = media(a,b,c,d)
	if x>=5.0:
		return 1
	elif x >=7.0:
		return 2
	else:
		return 3

n1=float(input("Informe a Nota 1: "))
n2=float(input("Informe a Nota 2: "))
n3=float(input("Informe a Nota 3: "))
n4=float(input("Informe a Nota 4: "))
daniel = sit(n1,n2,n3,n4)

if daniel ==1:
	print("Regular")
elif daniel ==2:
	print("Bom")
else:
	print("Ruim")

