#!/usr/bin/python3

""" This is just a very basic module to find a specific prime number.
This is my first python program. Everything I do and plan to do is CC-BY-SA.
Thanks for stopping by. Alpha32
"""

how_high = int(input("Enter the range: "))
nth_prime = list(input("Enter the primes to find: "))


def find_a_prime(nth_prime, how_high):

	primes = [1,3,5,7]	
<<<<<<< HEAD
""" I did this because I ran into issues getting the single-digit
primes to show up.
 If you have a better solution, let me know.
"""
        
        for i in range(10, how_high):  #what is wrong with this indent?
=======

	for i in range(10, how_high):
>>>>>>> 0fd3f88986929c58bcdcd04b4d1ae66c1a718453
		if i%2==0:
			continue
		elif i%3==0:
			continue
		elif i%5==0:
			continue
		else:
			primes.append(i)
        for num in nth_prime:
            print(primes[num]) 

if __name__ == '__main__':
	find_a_prime(nth_prime, how_high)
