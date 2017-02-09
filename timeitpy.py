
def benchmark(func):
	import time
	def wrapper(*args, **kwargs):
		t = time.clock()
		res = func(*args, **kwargs)
		print (func.__name__, time.clock() - t)
		return res
	return wrapper

@benchmark
def fib1(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib1(n-1) + fib1(n-2)

@benchmark	
def fib2(n):
	if n == 0:
		return 0
	lst = range(n)
	lst[0] = 0
	lst[1] = 1
	for i in range(2,len(lst)):
		lst[i] = lst[i-1] + lst[i-2]
	return lst[-1]


print fib2(20)