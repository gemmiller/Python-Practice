from math import sqrt
a =  input()
b = input()
c = input()

discr = (b**2) - 4*a*c

if discr < 0:
	print "No real solution."
elif discr == 0:
	print "Only one solution."
	print (-1*b + sqrt(discr))/2
else:
	print "Two possible solutions"
	print (-1*b + sqrt(discr))/2
	print (-1*b - sqrt(discr))/2

