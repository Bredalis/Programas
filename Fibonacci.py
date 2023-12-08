
def Fibonacci(Numero):

	if Numero == 0 or Numero == 1:
		return Numero

	else:
		return Fibonacci(Numero - 1) + Fibonacci(Numero - 2)

for i in range(10):
	print(Fibonacci(i))