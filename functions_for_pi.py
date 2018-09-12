def create_target_string (filename):
	''' open a file and then turn its content into one string'''
	with open(filename) as file_object:
		content = file_object.readlines()

	target_string =''
	for line in content:
		target_string += line.strip()
	return (target_string)

def make_combination_lists(number_list):
	''' adding a single digit to each of the given number in the number_list, 
	thus making a new number_list with one more digit'''
	all_digits = list(range(0,10))
	new_number_list = []
	for digit in all_digits:
		for i in number_list:
			new_number_list.append(str(digit)+str(i))
	return(new_number_list)


def examine_number (number_list, in_string, not_in_string, target_string):
	''' examine whether the numbers in number_list are also in a target string.
		in_string records those that are in target_string, not_in_string those not.'''
	for i in number_list:
		if str(i) not in target_string:
			not_in_string.append(i)
		else:
			in_string.append(i)	

def print_results (number_list, number_of_digits, target_string, in_or_not):
	''' print results, if print numbers in pi, in_or_not == 1, otherwise 0'''
	length = len(number_list)
	if in_or_not:
		if length == 0 or length == 1:
			print("  {} number with {} digits is in the first {} digits of pi.".format(str(length), number_of_digits,str(len(target_string)-2)))
		else:
			print("  {} numbers with {} digits are in the first {} digits of pi.".format(str(length), number_of_digits, str(len(target_string)-2)))	
	else:
		if length == 0 or length == 1:
			print("  {} number with {} digits is NOT in the first {} digits of pi.".format(str(length), number_of_digits,str(len(target_string)-2)))
		else:
			print("  {} numbers with {} digits are NOT in the first {} digits of pi.".format(str(length), number_of_digits, str(len(target_string)-2)))	

def print_numbers (number_list, in_or_not):
	''' based on user's choice, decide whether to print all numbers'''
	while True:
		if in_or_not:
			choice = input("\nDo you want to view all the numbers found in pi? Y/N ")
		else:
			choice = input("\nDo you want to view all the numbers NOT found in pi? Y/N ")
		if choice.lower() == 'n':
			break
		elif choice.lower() == 'y':
			if number_list:
				for number in number_list:
					print(number)
				break
			else:
				print("No number to show.")
				break
		else:
			print("Please only choose Y or N, thanks.")