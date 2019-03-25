ALPHABASE = "abcdefghijklmnopqrstuvwxyz,. "
LENGTH = 3200
BITS = 15546

DEBUG = True

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
	# Reverse the bits to generate a subrandom number.
	# See: https://stackoverflow.com/a/41728178/2368124
	# for information on the Hammersley Set.
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
	b = '{:0{width}b}'.format(number, width=BITS)
	return int(b[::-1], 2)

"""
Encode a positive number in Base X

Arguments:
- `num`: The number to encode
- `alphabet`: The alphabet to use for encoding.
"""
def encode(num, alphabet=ALPHABASE):
	if num == 0:
		return alphabet[0]
	arr = []
	base = len(alphabet)
	while num:
		num, rem = divmod(num, base)
		arr.append(alphabet[rem])
	arr.reverse()
	return ''.join(arr)

"""
Decode a Base X encoded string into the number.

Arguments:
- `string`: The encoded string
- `alphabet`: The alphabet to use for encoding
"""
def decode(string, alphabet=ALPHABASE):
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