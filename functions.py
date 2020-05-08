#definition
def my_function():
	print "hello"

#arguments
def add(n1, n2):
	return n1+n2

#multiple return values
def square(n1, n2):
	return n1**2, n2**2
	
#calling
my_function()
ret = add(1123,2)
print ret

#calling functions, which have multiple return values
#unpacking returned tuples
ret1, ret2 = square(2, 3)
print ret1, ret2