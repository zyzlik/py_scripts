word = 'qabccbatc'

max_poly = len(word)

print len(word)/2

def poly(seq):
	if seq == ''.join(list(reversed(seq))):
		return True
	return False


def max_poly(word):
	max_poly = len(word)
	variants = 1
	while variants < len(word):
		for i in range(variants):
			print('check for '+ word[i:i + max_poly])
			if poly(word[i:i + max_poly]):
				return word[i:i + max_poly]
		variants += 1
		max_poly -= 1


print max_poly('artrartrt')