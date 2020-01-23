'''
PROBLEM STATEMENT:
There are 21 sticks.
System Vs User
RULES:
1. Atleat 1 stick shoul be picked.
2. Upto 4 (1 - 4) sticks can be picked in one chance.
The one who is left to pick up the last stick, will be the loser.

'''

import random as rd
print '\t\t\t.....WELCOME TO THE GAME OF 21 STICKS.....'
print '\t\t...HURRAY!!!! You are our guest, So you will get the chance first!!!'
sticks_total = 21
while True:
	user_input = int(raw_input('Choose your number of sticks: '))
	if user_input >4:
		print 'You are breaking the rules... Pick the sticks again between 1 and 4...'
		pass
	
	else:

		#print 'Now system will choose: '
		if user_input == 1:
			while True:
				sys_input = rd.randint(1,5)
				if sys_input != 4:
					pass
				else:
					print 'System chooses: ', sys_input
					break 
		if user_input == 2:
			while True:
				sys_input = rd.randint(1,5)
				if sys_input != 3:
					pass
				else:
					print 'System chooses: ', sys_input
					break 
		if user_input == 3:
			while True:
				sys_input = rd.randint(1,5)
				if sys_input != 2:
					pass
				else:
					print 'System chooses: ', sys_input
					break 
		if user_input == 4:
			while True:
				sys_input = rd.randint(1,5)
				if sys_input != 1:
					pass
				else:
					print 'System chooses: ', sys_input
					break 
		sum_all = user_input + sys_input
		sticks_left = sticks_total - sum_all
		print 'Left Sticks are: ', sticks_left
		sticks_total = sticks_left

		if sticks_left == 1:
			print '\t\t*** OOPS!!! You are the last one to pick the stick.***'
			print '\t\t***** You Lose the game to the system***** '
			break