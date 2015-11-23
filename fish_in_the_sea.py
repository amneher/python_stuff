#!/usr/bin/env python3

import csv

age = int(input('Enter your age: '))
gender_pref = input('Enter your preferred gender. 1 for male, 2 for female: ')

def fish_in_the_sea(age, gender_pref):
	fish = csv.reader(open('census_data.csv'))
	
	min_age = (age/2)+7
	max_age = (age-7)*2

	for line in fish:
		if line[0] == gender_pref:
			new_age = int(line[1])
			if new_age>=min_age and new_age<=max_age:
				print(line[1:3])
		else: 
			pass
	# fish.close()
	
if __name__ == '__main__':
	fish_in_the_sea(age, gender_pref)
