'''
Author: Fanchen Bao
Date: 01/14/2018

Description: 
A small program to examine all possible digit (0 to 9) combinations in pi, with the number of digits provided by the user.
Note that such combination is NOT a permutation of 0-9, but allows repeats on each digit.
E.g. a three digit combination is every arrangement from 000 to 999.

User is prompted to enter number of digits for the digit combination to be examined. At the same time user is also prompted to enter 'quit' to exit the program
Result shows how many of those combinations are in pi, and how many not.
Then the program asks user whether he/she wants to view all the combinations in pi and those not in pi.
'''

import functions_for_pi

filename = 'pi_million_digits.txt' # file that stores the first million pi digits
pi_string = functions_for_pi.create_target_string(filename)

print("\nWe have the first {} digits of pi. \nLet's examine what digit (from 0 to 9) combinations are in these digits.".format(str(len(pi_string)-2)))

while True:
	number_of_digits = input("\nHow many digits do you want to examine? (type 'quit' to end program): ")
	if number_of_digits.lower() == 'quit':
		break
	else:
		# set up lists to record numbers in or not in the pi digits
		in_pi = []
		not_in_pi = []
		
		# original single digits
		digit_combinations = list(range(0,10))
		
		# make digit combinations by calling the function multiple times.
		# the number of time the function is called depends on how many digits are in the number.
		# for single digit number, function not called; 2-digit, 1 time; 3-digit, 2 times; etc.
		for i in range(int(number_of_digits)-1):
			digit_combinations = functions_for_pi.make_combination_lists(digit_combinations)

		functions_for_pi.examine_number(digit_combinations, in_pi, not_in_pi, pi_string)

		print("---")
		# display results
		functions_for_pi.print_results(in_pi, number_of_digits, pi_string, 1)
		functions_for_pi.print_results(not_in_pi, number_of_digits, pi_string, 0)

		# prompt user whether to show all the digit combinations
		functions_for_pi.print_numbers(in_pi, 1)
		functions_for_pi.print_numbers(not_in_pi, 0)

print("Thank you for using the program.")
