
def shiftbyn(zin, reeks, n):
	reeks *= 2
	if type(n) == type(0): n = [n]*(4*len(zin))

	nieuwezin = ''
	for il, letter in enumerate(zin):
		print il
		if letter != ' ':
			pos = reeks.find(letter)
			nieuweletter = reeks[pos+n[il]]
		else: nieuweletter = ' '
		nieuwezin += nieuweletter

	return nieuwezin


if __name__ == "__main__":
	zin = "ffc ubcbeo feobl jmbqofedbibe jdbp"
	reeks = 'abcdefghijklmnopqrstuvwxyz'
	# nummers = [11,6,4,5,9,4,8,9,7,6,34,6,6,7,4,9,32,8,8,0,4,7,5,3,9,3,6,17]*3
	for i in range(35):
		print shiftbyn(zin, reeks, i)
	print "---\n"
	# print shiftbyn(zin, reeks, nummers)
