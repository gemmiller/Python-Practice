from math import ceil , sqrt

# Takes an integer and prints of wether it is a perfect number or not
def find_perfect(perfect):
	sum = 1
	top =ceil(sqrt(perfect)) + 1
	for i in range(2,int(top)):
		if(perfect%i==0):
			sum+= i + perfect/i
	if(sum == perfect):
		print "Perfect number"
	else:
		print "Not a perfect number"

#This is some extra stuff because find perfect is to easy and boring
#The following fucntions handle basic functions used in finding primes and prime factors

#returns the greatest common divisor of a and b
def gcd(a,b):
	while b:
		a,b = b, a%b
	return a

#retruns a factor of n based starting point s and incrementation function f
#returns d == n when fails
#if failure occuers it is likly that n is semi prime
#uses a simplfied version the orginal pollard_rho algorithm using Floyds cycle detection
def pollard_rho(n,s,f):
	x = y = s
	d = 1
	while d == 1:
		x = f(x,n)
		y = f(f(y,n),n)
		d= gcd(abs(y-x),n)
	return d

#Primality test based around a seive
#It is not segmented or compressed so large values n encounter a memory issues
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

#An idetion to pollard_rho to handle failed case with brute force divsion
def g_rho(v,s,f):
	d = pollard_rho(v,s,f)
	#handle semi-primes with brute force
        if d == v and not isPrime(d):
		primes = getPrimes(d)
		for p in primes:
			if v%p ==0 :
				return p
	return d

#Uses a seive to find all Primes underneith a give value n
#returns a list of primes less than or equal to n
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

#calculates all prime factors of a number
#returns a list of all the prime factors
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

#checks if the list contains all the factors of number
#returns true if the list contains all factors of number, false otherwise
def checkFactors(number, factors):
	check = 0
	for f in factors:
		check = number/f

	if check == 1:
		return True
	else:
		return False



