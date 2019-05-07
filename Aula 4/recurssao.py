# Recurssão final
seq=[]
def rec(n):
	if n > 0:
		seq.append(n)
		while n > 1:
			if n % 2 ==0:
				n = int(rec(n / 2))
			else:
				n = int(rec(n * 3 + 1))
	return n

x=int(input())
while 1 <= x <= 500:
	rec(int(x))
	print(int(max(seq)))
	seq=[]
	x=int(input())