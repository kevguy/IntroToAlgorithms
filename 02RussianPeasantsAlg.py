#Russian Peasants Algorithm
def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1 # Shifting to left --> Doubling y
        x = x >> 1 # Shifting to right --> Halving x
    return z

def recursive_russian(a,b):
	if a == 0:
		return 0
	if a % 2 == 0:
		return 2 * recursive_russian(a / 2, b)
	return b + 2 * recursive((a - 1) / 2, b)

# Example
print russian(14, 11)
# Output: 154
#	x	y	z
#	14	11	0
#	7	22	0
#	3	44	22
#	1	88	66
#	0	176	154 <--
#
# Proof of correctness
# Claim: ab = xy + z
# base case: it holds
# inductive step: if ab = xy + z holds
#					then ab = x'y' + z' afterwards
# case I: x is odd
#
#	x' = (x - 1) / 2 
#	y' = 2y
#	z' = z + y
#
#	So,
#	x'y' + z' = ((x - 1) / 2) 2y + z + y = xy - y + z + y = xy + z = ab
#
# case II: x is even
#
#	x' = x / 2
#	y' = 2y
#	z' = z
#
#	So,
#	x'y' + z' = (x / 2)2y + z = xy + z = ab