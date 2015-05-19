# rsa_heedo.py
#
# Let's practice RSA Public Key Cryptosystem
# 2) p = 2357, q = 2551 (using big number calculator) if M = 1234
# 3) p = 885320963, q = 238855417 (using big number calculator) if M = 1234567
# Due: 19/May/2015 (Tue) 23:59
#
# IMPORTANT: You should submit your source code with your report

# Get gcd(m, n) using Euclidean Algorithm.
def euc(m, n):
	if n == 0:
		return m
	else:
		return euc(n, m % n)

# Get array of primes below integer n.
def primes(n):
	arr = [None] * n
	res = []
	p = 2
	for i in range(2, n):
		arr[i] = i
	for i in range(2, n):
		if arr[i] == 0:
			continue
		for j in range(i + i, n)[::i]:
			arr[j] = 0
	for i in range(2, n):
		if arr[i] != 0:
			res.append(arr[i])
	return res

# Find the smallest e for encryption.
def find_e(euler):
	# for e in primes(int(sqrt(euler))):
	for e in primes(100):
		if euc(e, euler) == 1:
			return e
	return -1	# Error

# Get Euler function value for prime p, q.
def euler(p, q):
	return (p - 1) * (q - 1)

# Advanced modular function using involution.
def help_mod(a, b, n):
	total = 1
	a = a % n
	while b != 0:
		if b % 2 == 1:
			total = (total * a) % n
			# print "a:", a, "b:", b, "total:", total
		a = (a * a) % n
		b = b / 2
	return total

# Find d for decryption using Extended Euclidean Algorithm.
def find_d_EEA(e, euler):
	x = 0; old_x = 1
	y = 1; old_y = 0
	r = e; old_r = euler
	while r != 0:
		q = old_r / r
		(old_r, r) = (r, old_r - q * r)
		# (old_x, x) = (x, old_x - q * x)
		(old_y, y) = (y, old_y - q * y)
	while old_y < 0:
		old_y = old_y + euler
	if old_y > euler:
		return -1	# Error
	return old_y

# RSA function with print forms.
def rsa(p, q, m):
	n = p * q
	o = euler(p, q)
	e = find_e(o)
	d = find_d_EEA(e, o)
	m2c = help_mod(m, e, n)
	c2m = help_mod(m2c, d, n)
	print "RSA KeyGen, Enc, Dec"
	print "p:", p, "q:", q
	print "n:", n, "euler(n):", o
	print "e:", e, "d:", d
	print "m for Enc:", m
	print "Result of Enc:", m2c
	print "c for Dec:", m2c
	print "Result of Dec:", c2m

# Show result of examples.
rsa(2357, 2551, 1234)
print
rsa(885320963, 238855417, 1234567)


