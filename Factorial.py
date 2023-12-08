
def Factorial(Numero):

	if Numero == 0:
		return 1

	else:
		return Numero * Factorial(Numero - 1)
		
for i in range(5):
	print(Factorial(i))