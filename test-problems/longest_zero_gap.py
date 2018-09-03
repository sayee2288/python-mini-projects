from collections import Counter
import math

def convert_to_binary(number):

	b_num = int(format(number, 'b'))
	print('Integer is {} , binary representation is {}, Now to find the longest gap' .format(number, (b_num)))
	n_to_list = [(b_num//(10**i))%10 for i in range(math.ceil(math.log(b_num, 10))-1, -1, -1)]
	b_count = Counter(n_to_list)
	if b_count[1] < 2:
		print('0')
	else:
		find_longest_gap(n_to_list, b_count[1])

def find_longest_gap(n_to_list, num_of_ones):
	longest_gap = 0
	current_gap = 0
	one_counter = 0
	for i in n_to_list:
		if i == 1:
			one_counter += 1
			if current_gap > longest_gap:
				longest_gap = current_gap
				current_gap = 0
				if one_counter == num_of_ones:
					break
			else:
				current_gap = 0
				continue
		else:
			current_gap += 1

	print('The longest gap is {}' .format(longest_gap))


while True:
	try:
		my_int = int(input('Enter a number: '))
	except ValueError:
		print('Please enter a valid integer with no deciaml points')
		continue
	break

convert_to_binary(my_int)
