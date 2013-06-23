# -*- coding: UTF-8 -*-
# fibonacci, f = f-1 + f-2, f0 = 0, f1 = 1;

print ("Hello GITHUB GITHUB");

def fib(num):
	result = 0;
	if num == 0:
		print "get in num0";
		result = 0;
	elif num == 1:
		print "get in num1";
		result = 1;
	else:
		print "get in else";
		result = fib(num-1) + fib(num-2);
	return result;
	
print fib(15);
