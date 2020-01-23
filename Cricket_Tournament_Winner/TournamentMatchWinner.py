'''
PROBLEM STATEMENT: 
Ask user the number of teams and their names. Then divide those teams into 2 teams and find out the ultimate winner among sub teams as well as overall.

Set and its operations from Python are used in this program.
'''


print '*'* 140
print '\n\t\t\t\t\t\t\t\t','******WELCOME TO IPL TOURNAMENT*******'
print '='* 140

name_list = set()
name_list1 = set()
name_list2 = set()
name_list_left = set()
name_list_right = set()
winner_list_left = set()
winner_list_right = set()


num_teams = int(raw_input('\nHow many teams are there: \n'))
if num_teams == 1:
	print 'Since only 1 team is there, Winner is that only.'
	exit()
else:
	for i in range(num_teams):
		name_team = raw_input('TEAM %d: ' % (i+1))
		name_list.add(name_team.upper())

	print '\n\n\t\t\tTEAMS are: ',name_list

	if num_teams%2 ==0:
		for i in range(num_teams/2):
			name_list1.add(name_list.pop().upper())
		for i in range((num_teams/2),num_teams,1):
			name_list2.add(name_list.pop().upper())
	else:
		for i in range((num_teams/2)+1):
			name_list1.add(name_list.pop().upper())
		for i in range(((num_teams/2) +1),num_teams,1):
			name_list2.add(name_list.pop().upper())

	print '\n\t\t\tLEFT TEAMS: ',name_list1
	print '\n\t\t\tRIGHT TEAMS: ',name_list2


	print '\n\n\t\t\t LET\'S FIND OUT WINNER FROM LEFT TEAM:'
	
	if len(name_list1) == 1:
		winner_list_left.add(name_list1.pop())
		print '\n\t\t\tWinner from Left team is: ', winner_list_left

	elif (len(name_list1)==2):
		winner_left = raw_input('Who\'s the winner among two:').upper()
		if winner_left not in name_list1:
			print '\n\t\t\tSorry!!!. You have selected wrong team\'s name...'
		else:
			print '\n\t\t\tWinner from Left Team is: ', winner_left
			winner_list_left.add(winner_left)
	
	else:
		
		while(len(name_list1)>0):
			
			name_list_left.add(name_list1.pop())
			name_list_left.add(name_list1.pop())
			
			print '\nChoose winner from Set: ', name_list_left
			winner_left = raw_input().upper()		
			
			if winner_left not in name_list_left:
				print '\nSorry!!!. You have selected wrong team\'s name...'
			else:
				winner_list_left.add(winner_left)
				name_list_left.clear()
				
				if len(winner_list_left)==2:
					print '\nChoose winner from Set:\n',winner_list_left 
					winner_left1 = raw_input().upper()		
					
					if (winner_left1 not in winner_list_left):
						print 'Sorry!!!. You have selected wrong team\'s name...'
						break
					
					else:
						print 'Winner from Left Team is: ', winner_left1
						winner_list_left.clear()
						winner_list_left.add(winner_left1)
										
				if len(name_list1) ==1:
					print '\nChoose winner from Set:\n',winner_list_left,name_list1 
					winner_left1 = raw_input().upper()		
					
					if ((winner_left1 not in winner_list_left) and (winner_left1 not in name_list1)):
						print 'Sorry!!!. You have selected wrong team\'s name...'
						break
					
					else:
						print 'Winner from Left Team is: ', winner_left1
						winner_list_left.clear()
						winner_list_left.add(winner_left1)
						break	 
				
				if len(name_list1) ==0:
					print 'Winner from LEFT TEAM is: ', winner_list_left

		print 'Winner from left team is: ', winner_list_left
					
	print '\n\n\t\t\tLET\'S FIND OUT WINNER FROM RIGHT TEAM:'
	if len(name_list2) == 1:
		winner_list_right.add(name_list2.pop())
		print '\n\t\t\tWinner from Right team is: ', winner_list_right
	
	
	elif (len(name_list2)==2):
		winner_right = raw_input('Who\'s the winner among two:').upper()
		if winner_right not in name_list2:
			print '\n\t\t\tSorry!!!. You have selected wrong team\'s name...'
		else:
			print '\n\t\t\tWinner from Right Team is: ', winner_right
			winner_list_right.add(winner_right)
	
	else:
		
		while(len(name_list2)>0):
			
			name_list_right.add(name_list2.pop())
			name_list_right.add(name_list2.pop())
			
			print '\nChoose winner from Set: ', name_list_right
			winner_right = raw_input().upper()		
			
			if winner_right not in name_list_right:
				print '\nSorry!!!. You have selected wrong team\'s name...'
			else:
				winner_list_right.add(winner_right)
				print 'Winners from right team till now: ', winner_list_right
				name_list_right.clear()
				
				if len(winner_list_right)==2:
					print '\nChoose winner from Set:\n',winner_list_right
					winner_right = raw_input().upper()		
					
					if (winner_right not in winner_list_right):
						print 'Sorry!!!. You have selected wrong team\'s name...'
						break
					
					else:
						print 'Winner from Right Team is: ', winner_right
						winner_list_right.clear()
						winner_list_right.add(winner_right)
										
				if len(name_list2) ==1:
					print '\nChoose winner from Set:\n',winner_list_right,name_list2
					winner_right = raw_input().upper()		
					
					if ((winner_right not in winner_list_right) and (winner_right not in name_list2)):
						print 'Sorry!!!. You have selected wrong team\'s name...'
						break
					
					else:
						print 'Winner from Left Team is: ', winner_right
						winner_list_right.clear()
						winner_list_right.add(winner_right)
						break	 
				
				if len(name_list2) ==0:
					print 'Winner from RIGHT TEAM is: ', winner_list_right

	print 'LEFT TEAM WINNER: ', winner_list_left
	print 'RIGHT TEAM WINNER: ', winner_list_right
	print '\nChoose the ultimate winner from :\n',winner_list_left,winner_list_right
	winner = raw_input().upper()		
	if ((winner not in winner_list_right) and (winner not in winner_list_left)):
		print 'Sorry!!!. You have selected wrong team\'s name...'
	else:
		print 'The ultimate Winner is: ', winner
		print '!=' * 80
						
