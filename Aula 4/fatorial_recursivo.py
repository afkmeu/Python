def fat(n):
	if n==0:
		return 1
	else:
		return n*fat(n-1)
x=fat(4)
print(x)