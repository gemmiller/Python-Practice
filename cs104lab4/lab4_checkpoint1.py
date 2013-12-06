# @returns a string with the first and last charaters switched
def switcharoo(word):
	#strings are imutable so we well break it in to a list
	chars = list(word)
	firstchar = chars[0]
	chars[0] = char[len(chars)-1]
	chars[len(chars)-1] = firstchar
	return ''.join(chars)
