#function sugests a user name pased on a string "lastname, firstname"
#@returns a username based on the first letter of the first name and the full lastname
def suggest(fullname):
	comma = fullname.find(",")
	lastname = fullname[:comma].strip()
	firstletter= fullname[comma+1:].strip()[0]
	return (firstletter+lastname).lower()
