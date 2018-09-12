'''
Author: Fanchen Bao
Date: 01/13/2018

Description: 
A small program to check whether a user-input number appears in the first million digits of pi.
User is prompted to enter any number in string format (i.e. prefix 0 allowed) to be examined. At the same time user is also prompted to enter 'quit' to exit the program
Result tell whether the user-input number is in the first million digits of pi, and at which position it occurs for each time.
'''

import functions_for_pi

filename = 'pi_million_digits.txt' # file that stores the first million pi digits
pi_string = functions_for_pi.create_target_string(filename)

print("\nWe have the first {} digits of pi.".format(str(len(pi_string)-2)))

while True:
	#ask user to input any number to see if it's in pie
	target_number = input('\nPlease input any number you think of (type "quit" to exit program): ')

	# use "quit" input to end program
	if target_number.lower() == 'quit':
		break

	# count how many times the number appears in pi
	counter = 0

	if target_number in pi_string:
		print("The number {} is in pi.\n".format(target_number))
		
	# find out at which position the target number matches to pi digits
		for i in range(2, len(pi_string) - len(target_number)):
			if pi_string[i : i+len(target_number)] == target_number:
				counter += 1
				print("It appears the {}th time at the {}th position of pi after decimal point.".format(counter, i-1))
	else:
		print("Sorry, the number {} is not in pi".format(target_number))

print("Thank you for using the program.")




