# TODO figure out how to guarantee converting base 10 to ALPHABASE
# yields an output of length LENGTH. Sometimes the output returns
# a subrandom sequence larger or smaller than LENGTH by 1.

DEBUG = True

# Alpha-numeric-symbolic characters the pages are allowed to use.
ALPHABASE = "abcdefghijklmnopqrstuvwxyz,. "

# Length of each page in characters.
LENGTH = 3200

# We want len(ALPHABASE)**LENGTH to be about the same as the 2**x.
# e.g. 29**3200 ≈ 2**15546
# So far I've used WolframAlpha to find the equivalencies, but there might be a way to do it in Python.
BITS = 15546

def main():
	ed = input('[e]ncode or [d]ecode? ')
	if ed == 'e' or ed == 'E':
		x = int(input('Enter a number: '))
		print(page_by_seed(x))
	else:
		x = input('Enter a string: ')
		x_rev = seed_by_page(x)
		print("The initial seed number is:")
		print(x_rev)

def page_by_seed(seed):
	"""
	Takes a base 10 seed, reverses the number bitwise, 
	converts to base 29, in this case, and returns the result.
	"""
	seed_rev = reverse_bits(seed)
	encoded_string = encode(seed_rev)
	if DEBUG:
		print('DEBUG encoded string length: ' + str(len(encoded_string)))
	return encoded_string

def seed_by_page(page):
	page_decoded = decode(page)
	seed = reverse_bits(page_decoded)
	return seed

def reverse_bits(number):
	"""
	This is the Hammersley Set operation that reverses a number bitwise.
	e.g. 1100011101 -> 1011100011
	See: https://stackoverflow.com/a/41728178/2368124
	for information on the Hammersley Set.
	"""
	b = '{:0{width}b}'.format(number, width=BITS)
	return int(b[::-1], 2)

def encode(num, alphabet=ALPHABASE):
	"""
	Encode a positive number in Base X

	Arguments:
	- `num`: The number to encode
	- `alphabet`: The alphabet to use for encoding.
	"""
	if num == 0:
		return alphabet[0]
	arr = []
	base = len(alphabet)
	while num:
		num, rem = divmod(num, base)
		arr.append(alphabet[rem])
	arr.reverse()
	return ''.join(arr)

def decode(string, alphabet=ALPHABASE):
	"""
	Decode a Base X encoded string into the number.

	Arguments:
	- `string`: The encoded string
	- `alphabet`: The alphabet to use for encoding
	"""
	base = len(alphabet)
	strlen = len(string)
	num = 0

	idx = 0
	for char in string:
		power = (strlen - (idx + 1))
		num += alphabet.index(char) * (base ** power)
		idx += 1

	return num

if __name__ == '__main__':
	main()