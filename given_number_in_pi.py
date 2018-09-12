# A small program to check whether a user-input number appears in the first million digits of pie

filename = 'pi_million_digits.txt'

# open a file with many digits of pi
with open(filename) as file_object:
	lines = file_object.readlines()

# set the file content into one string, named as pi_string
pi_string = ''

for line in lines:
	pi_string += line.strip()

print("We have the first {} digits of pi:\n{}...".format(str(len(pi_string)-2), pi_string[:100]))

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
				if counter == 1:
					print("It appears the first time at the {}th position of pi after decimal point.".format(str(i-1)))
				elif counter == 2:
					print("It appears the second time at the {}th position of pi after decimal point.".format(str(i-1)))
				elif counter == 3:
					print("It appears the third time at the {}th position of pi after decimal point.".format(str(i-1)))
				else:
					print("It appears the {}th time at the {}th position of pi after decimal point.".format(str(counter), str(i-1)))
	else:
		print("Sorry, the number {} is not in pi".format(target_number))

print("Thank you for using the program.")




