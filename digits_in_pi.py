''' A small program to examine all possible digit (0 to 9) combinations in pi'''

import functions_for_pi

filename = 'pi_million_digits.txt'
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
		functions_for_pi.print_results(in_pi, number_of_digits, pi_string, 1)
		functions_for_pi.print_results(not_in_pi, number_of_digits, pi_string, 0)

		functions_for_pi.print_numbers(in_pi, 1)
		functions_for_pi.print_numbers(not_in_pi, 0)

print("Thank you for using the program.")
