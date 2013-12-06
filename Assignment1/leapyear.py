#Author: Geoff Miller
#takes in a year and determins if it is a leap year
def leapyearStandard(year):
	if (year%4==0 and  year%100!=0) or (year%100==0 and year%400==0):
		print year,"is a leap year"
	else:
		print year,"is not a leap year"


leapyearStandard(year)



