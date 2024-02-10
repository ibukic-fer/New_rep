def factorial(x):
	if x==0:
		return 1
	else
		return x * factorial(x-1)
		
t = 5
res= factorial(t)
print(f'The factorial of {t} is {res}.')
