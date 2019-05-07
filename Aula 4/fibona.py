#Cria-se um array para armazenar os resultados para não ter que rodar a recursividade novamente do zero até chegar no valor seguinte, isso poupa tempo e faz o programa não travar. 
fibo = []
for i in range(40):
	fibo.append(0)

# sendo o (num_calls para n) calls(n) = calls(n - 1) + calls(n - 2) + 2 (para as calls serem chamadas,devemos pre-processar um array com o numero das calls).
calls = [0, 0, 2]
for i in range(3, 40):
	calls.append(calls[i - 1] + calls[i - 2] + 2)

def fibonacci(n):
	if n <= 1:
		return n
		
	elif n != 0:
		return fibo[n]
	else:
		fibo[n] = fibonacci(n - 1) + fibonacci(n - 2)
		return fibo[n]

n = int(input("n"))

for i in range(n):
	if n==0:
		fib=n
	else:
		fib = i+1
		fibonacci(fib)

print ("fib(%d) = %d calls = %d " % (fib, calls[fib], fibo[fib]))
print()
print(fibo)
print(calls)