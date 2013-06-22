def recursive_largest_prime_factor(n):
	for i in range((n / 2), 1, -1):
		if isPrime(i):
			if (n % i == 0 ):
				if (recursive_largest_prime_factor(i)) == i:
					print "the largest prime of %r is %r" % (n,i)
					return i
	return n

def largest_prime_factor(n):
	print "checking for largest prime factor of ",n
	i = 2
	while i < n/2 +1:
#	for i in range(n/2,1,-1):
		# print "checking if %r is largest prime of %r" % (n/i,n)
		if  n/i%2 != 0 and n/i%3 != 0 and n/i%5 != 0 and n/i%7 != 0 and n/i != n/(i-1):
			print "checking if %r is largest prime of %r" % (n/i,n)
			if (n%i == 0):
				if isPrime(n/i):
					return n/i
				n = n/i
		i += 1


def isPrime(n):
#	print "checking to see if %r is prime" %r
	# for i in range(n/2,1,-1):
	i = 2
	while i < (n/2)+1:
		if (n%i == 0):
			return False
		i += 1
	return True

#print largest_prime_factor(18)
#print largest_prime_factor(13195)
print largest_prime_factor(600851475143)

# print recursive_largest_prime_factor(600851475143)
# print recursive_largest_prime_factor(18)


