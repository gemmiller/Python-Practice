def nFactorial(n):
	if n < 0:
		print " n must be greater than zero"
		return
	factorial = 1
	for i in range(2,n+1):
		factorial *= i

	return factorial

