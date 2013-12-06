#compareator function comapares to objects based on the comparison function
def compareator(val1,val2,compFunc):
	return compFunc(val1,val2)

def intComp(val1,val2):
	return val1-val2

def stringComp(val1,val2):
	return len(val1)-len(val2)


