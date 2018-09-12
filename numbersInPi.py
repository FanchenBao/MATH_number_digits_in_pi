'''
Author: Fanchen Bao
Date: 01/14/2018

Description: 
A small program to examine how many numbers (natural and 0) of a certain number of digits are in pi, with the number of digits provided by the user.
User is prompted to enter number of digits for the number to be examined. At the same time user is also prompted to enter 'quit' to exit the program
Result shows how many of those numbers with the given digit length are in pi, and how many not.
Then the program asks user whether he/she wants to view all the numbers in pi and those not in pi.
'''
import functions_for_pi


filename = 'pi_million_digits.txt'
pi_string = functions_for_pi.create_target_string(filename)
print("We have the first {} digits of pi. \nLet's examine what numbers are in these digits.".format(str(len(pi_string)-2)))

while True:
	number_of_digits = input("\nHow many digits do you want the numbers to have (type 'quit' to end program): ")
	if number_of_digits == 'quit':
		break

	# set up lists to record numbers in or not in the pi digits
	in_pi = []
	not_in_pi = []

	
	if number_of_digits == '0':
		print("Please input the number of digits larger than 0.")
		continue
	
	# make a list of numbers with 1 digit
	elif number_of_digits == '1':
		numbers_to_examine = [str(d) for d in range(0,10)]
	
	# make a list of numbers with any given number of digits other than 1
	else:
		numbers_to_examine = [str(d) for d in range(10**(int(number_of_digits)-1), 10**int(number_of_digits))]
		
	functions_for_pi.examine_number(numbers_to_examine, in_pi, not_in_pi, pi_string)	
	
	print("\n---")

	# print results
	functions_for_pi.print_results(in_pi, int(number_of_digits), pi_string, 1)
	functions_for_pi.print_results(not_in_pi, int(number_of_digits), pi_string, 0)
	
	# user chooses whether to view the numbers
	functions_for_pi.print_numbers(in_pi, 1)
	functions_for_pi.print_numbers(not_in_pi, 0)

print("Thanks for using the program!")