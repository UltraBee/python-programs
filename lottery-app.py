import random

def get_player_numbers():
	number_csv = input("Enter your numbers, seperated by commas:")
	number_list = number_csv.split(",")
	integer_set = {int(i) for i in number_list}
	return integer_set


def create_lottery_numbers():
	lottery_numbers = set()
	while len(lottery_numbers) < 6:
		lottery_numbers.add(random.randint(0, 10))
	return lottery_numbers

def game():
	player_numbers = get_player_numbers()
	lottery_numbers = create_lottery_numbers()
	matched_numbers = player_numbers.intersection(lottery_numbers)

	if len(matched_numbers)>=1 :
		print("You matched {0} number(s): {1} \nYou won ${2}!".format(len(matched_numbers), matched_numbers, len(matched_numbers)*100))
	else:
		print("You missed!")


game()
