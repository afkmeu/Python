def flip(n):
	print("flip")
	if n>0:
		flop(n-1)
	else:
		print("fim")
def flop(n):
	print("flop")
	if n>0:
		flip(n-1)
	else:
		print("fim")
print(flip(1))