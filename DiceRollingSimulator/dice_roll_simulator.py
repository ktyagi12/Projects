import random

def dice_roll():
	min_dice = 1
	max_dice = 6

	repeat = 'yes'

	while(repeat == 'yes' or repeat == 'y'):
		print(random.randint(min_dice,max_dice))
		repeat = input('Wanna continue??').lower()


if __name__ == '__main__':
	dice_roll()