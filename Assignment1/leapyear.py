# Script takes in a year and determins if it is a leap year

year = input("Enter a year greater than 100: ")
if (year%4==0 and  year%100!=0)or(year%100==0 and year%400==0):
	print year,"is a leap year"
else:
	print year,"is not a leap year"

