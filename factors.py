from math import sqrt
def gcd(a,b):
	while b:
		a,b = b, a%b
	return a

def pollard_rho(n,s,f):
	x = y = s
	d = 1
	while d == 1:
		x = f(x,n)
		y = f(f(y,n),n)
		d= gcd(abs(y-x),n)
	return d

def isPrime(n):
	if n ==1 or n == 0:
		return False
	if n == 2:
		return True
	if n%2 == 0:
		return False

	seive = [True]*(n+1)
	for i in range(2,n+1):
		if seive[i] ==  True:
			j = i*i
			while j < len(seive):
				seive[j]=False;
				j+=i
	if seive[n] == True:
		return True
	else:
		return False

def g_rho(v,s,f):
	d = pollard_rho(v,s,f)
	#handle semi-primes with brute force
        if d == v and not isPrime(d):
		primes = getPrimes(d)
		for p in primes:
			if v%p ==0 :
				return p
	return d

def getPrimes(n):
	seive = [True]*(n+1)
	for i in range(2,n+1):
		if seive[i] == True:
			j = i*i
			while j < len(seive):
				seive[j]=False
				j+=i
	primes = list()
	for i in range(2,len(seive)):
		if seive[i] == True:
			primes.append(i)
	return primes

def findPrimeFactors(n):
	s = 2
	f = lambda x, m: (x**2 + 2) % m
	stack = [n]
	factors = list()
	while len(stack)>0:
		v = stack.pop()
		if(isPrime(v)):
			factors.append(v)
		elif v == 1:
			continue
		else:
			d = g_rho(v,s,f)
			stack.append(d)
			stack.append(v/d)
		
	return factors

def checkFactors(number, factors):
	check = 0
	for f in factors:
		check = number/f

	if check == 1:
		return True
	else:
		return False
