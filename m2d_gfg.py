# Returns XOR of 'a' and 'b'
# (both of same length)
def xor(a, b):
	# initialize result
    result = []

	# Traverse all bits, if bits are
	# same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    
    print("xor",b,a,''.join(result))
    return ''.join(result)


# Performs Modulo-2 division
def mod2div(dividend, divisor):

	# Number of bits to be XORed at a time.
	pick = len(divisor)

	# Slicing the dividend to appropriate
	# length for particular step
	tmp = dividend[0 : pick]

	while pick < len(dividend):

		if tmp[0] == '1':

			# replace the dividend by the result
			# of XOR and pull 1 bit down
			tmp = xor(divisor, tmp) + dividend[pick]

		else: 
            # If leftmost bit is '0'
			# If the leftmost bit of the dividend (or the
			# part used in each step) is 0, the step cannot
			# use the regular divisor; we need to use an
			# all-0s divisor.
			tmp = xor('0'*pick, tmp) + dividend[pick]

		# increment pick to move further
		pick += 1

	# For the last n bits, we have to carry it out
	# normally as increased value of pick will cause
	# Index Out of Bounds.
	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)
	return tmp

# Function used at the sender side to encode
# data by appending remainder of modular division
# at the end of data.
def encodeData(data, key):

    l_key = len(key)

	# Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)

	# Append remainder in the original data
    codeword = data + remainder
    print("Remainder : ", remainder)
    print("Encoded Data (Data + Remainder) : ",codeword)
    return codeword

def decodeData(data, key):

    l_key = len(key)

    # Appends n-1 zeroes at end of data
    remainder = mod2div(data, key)

    # Append remainder in the original data
    codeword = data[:-(l_key-1)]
    print("Remainder : ", remainder)
    if(int(remainder)==0):
        print("Decoded Data (Data + Remainder) : ", codeword)
    else:
        print("Data Corrupted")


# Driver code
data = "10011101"
key = "1001"
d = encodeData(data, key)
# decodeData('0'+d[1:], key)
# decodeData(d, key)
