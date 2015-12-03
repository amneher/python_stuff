#!/usr/bin/python3

""" This is just a very basic module to find a specific prime number. This is my first python program. Everything I do and plan to do is CC-BY-SA. Thanks for stopping by. --Alpha32

Version: 0.0.3 -- made it loop to find more priiiiiimmmmmeeeessss!!! unless you're really looking for the answer to life, the universe, and everything.
"""

how_high = int(input("Enter the range: "))
# nth_prime = int(input("Enter the prime to find: "))

def get_them_primes(how_high):
	
	print('To quit the program, enter 42. \nIf you really want to know, the 42nd prime is 173.')

	primes = [1,3,5,7]	

	for i in range(10, how_high):
		if i%2==0:
			continue
		elif i%3==0:
			continue
		elif i%5==0:
			continue
		elif i%7==0:
			continue
		else:
			primes.append(i)
			
	while True:
		try:
			nth_prime = int(input("Enter the prime to find: "))
			print(primes[nth_prime]) 
			if nth_prime == 42:
				break
		except ValueError:
			print('Sorry, was that a number?')
			return get_them_primes(how_high)
		except IndexError:
			print('Whoops! Too far.')
			return get_them_primes(how_high)
			
if __name__ == '__main__':
	get_them_primes(how_high)
