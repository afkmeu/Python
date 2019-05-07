valores=input("Entre com dois valores inteiros positivos").split()
x=int(valores[0])
y=int(valores[1])
op=input("informe a operação: (+, -, *, /, **): ")
if op=="+":
	resultado=x+y
elif op=="-":
	resultado=x-y
elif op=="*":
	resultado=x*y
elif op=="/":
	resultado=x/y
elif op=="**":
	resultado=x**y
else:
	resultado=None
if resultado==None:
	print(op,":Operador Inexistente!!")
else:
	print(x, op, y, "=", resultado)