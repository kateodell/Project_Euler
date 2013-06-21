
def fib(n1, n2):
	if n2 > 4000000:
		return 0
	if n2 % 2 == 0:
		return n2 + fib(n2,n1+n2)
	else:
		return fib(n2,n1+n2)

print fib(1,2)











	






# 	if fib2 % 2 == 0:
# 		return fib2
# 	else: 
# 		return 0


# fib1 = 1
# fib2 = 2
# sum_of_evens = fib2



# while fib2 < 4000000:
# 	temp = fib2
# 	fib2 += fib1
# 	fib1 = temp
# 	if fib2 %2 == 0:
# 		sum_of_evens += fib2



# print sum_of_evens