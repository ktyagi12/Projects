import datetime
import random

super_user = {'admin':{'password':'admin','type':'super'}}
guest_user = {}
Train={}
Ticket={}

#===============================================================================================================================
def init():
	guest_user['ktyagi']={'password' : 'tyagi12' , 'full_name': 'Karishma Tyagi' , 'age' : 22 }
	Train[12345]={'train_name':'Duronto Express','train_src':'Delhi','train_dest':'Pune','running_days' : [0,1,1,0,1,0,1],'seats':80,'dist':2400,'fare': {'AC1':2400,'AC2':1800,'AC3':1200,'SL':700}}
	Train[98765]={'train_name':'Rajdhani Express','train_src':'Delhi','train_dest':'Pune','running_days' : [0,1,1,0,1,0,0],'seats':90,'dist':2400,'fare': {'AC1':2200,'AC2':1500,'AC3':1100,'SL':500}}
	Train[12346]={'train_name':'Goa Express','train_src':'Delhi','train_dest':'Goa','running_days' : [1,0,1,0,1,0,1],'seats':56,'dist':2410,'fare': {'AC1':1200,'AC2':1000,'AC3':800,'SL':500}}
	
#===============================================================================================================================

def modify_Train(train_num):
	if Train.has_key(train_num):
		train_name = raw_input('Enter the train name to be added: ')
		train_src = raw_input('Enter the source station of the train: ')
		train_dest = raw_input('Enter the destination station of the train: ')
		num_seats = int(raw_input('Enter the number of seats in the train: '))
		distance = int(raw_input('Enter the distance between the source station and the destination station for the train: '))
		
		print 'What is the fare for: '
		print 'AC1: '
		ac1=int(raw_input())
		print 'AC2: '
		ac2=int(raw_input())
		print 'AC3: '
		ac3=int(raw_input())
		print 'SL: '
		sl=int(raw_input())
		
		print 'On which days of the week, train runs starting from Sunday: (1/0)'
		print'Monday: '
		mon=int(raw_input())
		print'Tuesday: '
		tues=int(raw_input())
		print'Wednesday: '
		wed=int(raw_input())
		print'Thursday: '
		thurs=int(raw_input())
		print'Friday: '
		fri=int(raw_input())
		print'Saturday: '
		sat=int(raw_input())
		print'Sunday: '
		sun=int(raw_input())
		running_days=[mon,tues,wed,thurs,fri,sat,sun]

		for i in running_days:
			if i != 1 and i != 0:
				print 'You have entered the day other than 1 or 0.Kindly enter 1 or 0 for the days'
				modify_Train(train_num)

		train_temp = {'train_num':train_num,'train_name':train_name,'train_src':train_src,'train_dest':train_dest,'running_days' : running_days,'seats':num_seats,'distance':distance,'fare': {'AC1': ac1,'AC2':ac2,'AC3':ac3,'SL':sl}}
		Train[train_temp.get('train_num')] ={'train_name':train_temp.get('train_name'),
			'train_src':train_temp.get('train_src'),
			'train_dest':train_temp.get('train_dest'),
			'running_days':train_temp.get('running_days'),
			'seats':train_temp.get('seats'),
			'distance':train_temp.get('distance'),
			'fare':train_temp.get('fare')}

		print '\n','SUCCESSFULLY MODIFIED THE TRAIN'
		print '\n','NOW THE TRAINS ARE AS FOLLOWS:',Train

	else:
		print '\n\t\t\t\t\t\t\t\t','SORRY!!!! NO SUCH TRAIN EXISTS.'
		print '\n\t\t\t\t\t\t\t\t','CHOOSE AGAIN:'
#===============================================================================================================================

def add_Train(num_of_train):
	train_count = 1
	while train_count<=num_of_train:
		train_num = int(raw_input('Enter the train number to be added: '))
		if train_num == '':
			print 'You have not entered train number. Enter the details again...'
			add_Train(num_of_train)
		train_name = raw_input('Enter the train name to be added: ')
		train_src = raw_input('Enter the source station of the train: ')
		train_dest = raw_input('Enter the destination station of the train: ')
		num_seats = int(raw_input('Enter the number of seats in the train: '))
		distance = int(raw_input('Enter the distance between the source station and the destination station for the train: '))
		
		print 'What is the fare for: '
		print 'AC1: '
		ac1=int(raw_input())
		print 'AC2: '
		ac2=int(raw_input())
		print 'AC3: '
		ac3=int(raw_input())
		print 'SL: '
		sl=int(raw_input())
		
		print 'On which days of the week, train runs starting from Sunday: (1/0)'
		print'Monday: '
		mon=int(raw_input())
		print'Tuesday: '
		tues=int(raw_input())
		print'Wednesday: '
		wed=int(raw_input())
		print'Thursday: '
		thurs=int(raw_input())
		print'Friday: '
		fri=int(raw_input())
		print'Saturday: '
		sat=int(raw_input())
		print'Sunday: '
		sun=int(raw_input())
		running_days=[mon,tues,wed,thurs,fri,sat,sun]
		
		for i in running_days:
			if i != 1 and i != 0:
				print 'You have entered the day other than 1 or 0.Kindly enter 1 or 0 for the days'
				add_Train(num_of_train)
		
		train_temp = {'train_num':train_num,'train_name':train_name,'train_src':train_src,'train_dest':train_dest,'running_days' : running_days,'seats':num_seats,'distance':distance,'fare': {'AC1': ac1,'AC2':ac2,'AC3':ac3,'SL':sl}}
		print 'Current Train: ',train_temp
		print 'Existing Trains: ', Train

		if Train.has_key(train_temp.get('train_num')):
			print 'TRAIN ALREADY IN RECORDS.'
			admin_function()
		else:
			Train[train_temp.get('train_num')] ={'train_name':train_temp.get('train_name'),
			'train_src':train_temp.get('train_src'),
			'train_dest':train_temp.get('train_dest'),
			'running_days':train_temp.get('running_days'),
			'seats':train_temp.get('seats'),
			'distance':train_temp.get('distance'),
			'fare':train_temp.get('fare')}

			print '\n','SUCCESSFULLY ADDED TRAIN'
			print '\n','NOW THE TRAINS ARE:',Train

		train_count+= 1
#===============================================================================================================================

def remove_Train(train_num):
	if Train.has_key(train_num):
		Train.pop(train_num)
		print '\n','SUCCESSFULLY REMOVED THE TRAIN'
		print '\n','NOW THE TRAINS ARE AS FOLLOWS:',Train

	else:
		print 'SORRY!!!! NO SUCH TRAIN EXISTS.'
		print 'CHOOSE AGAIN:'
#===============================================================================================================================

def make_User_Admin(u_name,password):
	if guest_user.has_key(u_name):
		#guest_user.get('u_name')['type'] = 'super'
		super_user[u_name]={'password':password,'type':'super'}
		print 'Super User: ',super_user
		guest_user.pop(u_name)
		print 'Guest User: ',guest_user
	else:
		print 'SORRY!!!! NO SUCH USER EXISTS'
#===============================================================================================================================

def change_Passcode(u_name):
	if super_user.has_key(u_name):
		print 'Username is a super user itself...'
		admin_function()
	elif guest_user.has_key(u_name):
		print 'Enter the changed password for the user %s: ' %u_name
		guest_user.get(u_name)['password'] = raw_input()
		print 'Guest User: ',guest_user
	else:
		print 'SORRY!!!! NO SUCH USER EXISTS'
#===============================================================================================================================

def admin_function():
	
	while True:
		print '*' * 165,'\n\n\t\t\t\t\t\t\t\t','ADMIN PAGE...'
		print '\t\t\t\t\t\t\t','*'*35,"\n\t\t\t\t\t\t\t\t",'1. ADD TRAINS'
		print '\n\t\t\t\t\t\t\t\t','2. MODIFY TRAIN'
		print '\n\t\t\t\t\t\t\t\t','3. REMOVE TRAINS'
		print '\n\t\t\t\t\t\t\t\t','4. MAKE YOUR ALTERATIVE'
		print '\n\t\t\t\t\t\t\t\t','5. EDIT PASSWORDS'
		print '\n\t\t\t\t\t\t\t\t','6. BACK TO MAIN MENU'
		ch = int(raw_input('Enter your choice: '))

		if ch == 1:   #ADD TRAIN
			num_of_train = int(raw_input('How many trains you want to add to the database: '))
			add_Train(num_of_train)
			
		elif ch==2:  #MODIFY TRAIN
			train_num = int(raw_input('Enter the train number to be modified: '))
			modify_Train(train_num)
			
		elif ch==3:   #REMOVE TRAIN
			train_num = int(raw_input('Enter the train number to be removed: '))
			remove_Train(train_num)

		elif ch==4:    #MAKE OTHER USER SUPER USER
			u_name=raw_input('Enter the user name you want to make super user: ')
			password=raw_input('Enter the password for that user: ')
			make_User_Admin(u_name,password)

		elif ch==5:	#CHANGE PASSOWRD
			u_name=raw_input('Enter the user name for whom you want to change password: ')
			change_Passcode(u_name)
			
		elif ch==6:
			print 'YOU HAVE BEEN LOGGED OUT. KINDLY LOGIN AGAIN' ,main_page()
		else:
			print 'SORRY!!. WRONG CHOICE ENTERED..'
#===============================================================================================================================

def inquire_trains(src,dest):
	temp_train={}
	temp1={}
	print 'TRAIN SEARCHED IS: '
	for curr_train in Train.keys():
		if Train.get(curr_train)['train_src'] == src and Train.get(curr_train)['train_dest'] == dest:
			temp1[curr_train]=Train.get(curr_train)
			temp_train.update(temp1)
			
	return temp_train
			
#===============================================================================================================================
def inquire_book_trains(src,dest,num_passenger,answer):
	temp_train={}
	temp1={}
	for curr_train in Train.keys():
		if Train.get(curr_train)['train_src'] == src and Train.get(curr_train)['train_dest'] == dest and Train.get(curr_train)['seats'] >=num_passenger and Train.get(curr_train)['running_days'][answer] == 1:
			temp1[curr_train]=Train.get(curr_train)
			temp_train.update(temp1)
	return temp_train
#===============================================================================================================================

def user_func():
	tkt_temp={}
	while True:
		print '*' * 165,'\n\n\t\t\t\t\t\t\t\t','WELCOME TO KARISHMA RAILWAYS...'
		print '\t\t\t\t\t\t\t','*'*40,"\n\t\t\t\t\t\t\t\t",'1. INQUIRE FOR TRAIN'
		print '\n\t\t\t\t\t\t\t\t','2. BOOK TRAIN'
		print '\n\t\t\t\t\t\t\t\t','3. CANCEL TRAIN'
		print '\n\t\t\t\t\t\t\t\t','4. EXIT'
		ch = int(raw_input('Enter your choice: '))
		
		if ch ==1:
			src=raw_input('Enter the source station: ')
			dest=raw_input('Enter the destination station: ')
			Train_temp=inquire_trains(src,dest)
			if not Train_temp:
				print '\n\t\t\t\t\t\t\t\t','SORRY!!!! NO SUCH TRAIN EXISTS'
				print '\n\t\t\t\t\t\t\t\t','CHOOSE AGAIN:'
			else:
				print Train_temp

		elif ch==2:
			src=raw_input('Enter the source station: ')
			dest=raw_input('Enter the destination station: ')
			date_usr=raw_input('Enter your date of journey: YYYY-MM-DD ')
			
			y,m,d = map(int,date_usr.split('-'))
			answer = datetime.date(y,m,d).isoweekday()
			
			num_passenger = int(raw_input('How many passengers travelling: '))

			Train_temp=inquire_book_trains(src,dest,num_passenger,answer)
			
			if not Train_temp:
				print '\n\t\t\t\t\t\t\t\t','SORRY!!!  THE TRAIN DOES NOT RUNS ON THE SPECIFIED DAY'
				print '\n\t\t\t\t\t\t\t\t','CHOOSE AGAIN:'
			else:
				sum = 0
				print 'TRAINS FOUND: \n',Train_temp
				print '\n\n'
				book_train_num = int(raw_input('Enter the train number you wanna proceed with: '))
				for i in Train_temp:
					if book_train_num == i:
						for j in range(1,num_passenger+1):
							full_name = raw_input('Please enter the full name of passenger %d : ' %j)
							age = int(raw_input('Enter passenger %d age: ' %j))
							birth_pref = raw_input('Enter birth preference for passenger %d (SL/AC1/AC2/AC3): ' %j)
							for ran_num in range(0,10):
								PNR = random.randint(1,1001)

							sum+=Train_temp.get(i).get('fare')[birth_pref.upper()] + ((12*  Train_temp.get(i).get('fare')[birth_pref.upper()]) /100) + ((28*  Train_temp.get(i).get('fare')[birth_pref.upper()]) /100) +200
							tkt_temp[full_name] = {'train_num':i,'Train_Name':Train_temp.get(i).get('train_name'),'age':age,'birth_pref':birth_pref,'PNR_num': PNR,'source': src,'destination': dest,'date_of_journey': date_usr,'Total_fare': sum}
							
							Train_temp.get(i)['seats']-=1
							#print 'Temp Ticket: ',tkt_temp
							#print 'Train temp: ',Train_temp
							Ticket.update(tkt_temp)
							print 'Ticket is: ' , Ticket

						print '\t\t\t\t','='* 50
						print '\n\n\t\t\t\t\t\tWELCOME TO KARISHMA RAILWAYS \n\n\t\t\t\t\t\t TICKET GENERATED: '
						print '\n\t\t\t\t TRAIN NUMBER: %d \t\t\t\t TRAIN NAME: %s' %(i,Train_temp.get(i).get('train_name'))
						print '\n\t\t\t\t SOURCE: %s \t\t\t\t\t DESTINATION: %s' %(src,dest)
						print '\n\t\t\t\t DATE OF JOURNEY: %s \t\t\t NUMBER OF PASSENGERS: %d' %(date_usr,num_passenger)
						
						print '\n\t\t\t\t PASSENGERS DETAILS: '
						for k in Ticket:
							print '\n\t\t\t\t NAME: %s \t\t\t\t AGE: %d \t\t\t\t BIRTH PREFERENCE: %s' %(k,Ticket[k].get('age'),Ticket[k].get('birth_pref').upper())	

						print '\n\t\t\t\t PAYMENT DETAILS: '
						print '\n\t\t\t\t BASE FARE: ' ,Train_temp.get(i).get('fare')[birth_pref.upper()]
						print '\n\t\t\t\t SGST: ', ((12*  Train_temp.get(i).get('fare')[birth_pref.upper()]) /100),'\n\t\t\t\t CGST: ', ((28*  Train_temp.get(i).get('fare')[birth_pref.upper()]) /100)
						print '\n\t\t\t\t Convience Fee: ', 200
						print '\n\t\t\t\t TOTAL FARE: ', sum + ((12*  Train_temp.get(i).get('fare')[birth_pref.upper()]) /100) + ((28*  Train_temp.get(i).get('fare')[birth_pref.upper()]) /100) +200
						print '\n\t\t\t\t','='* 50
						
		elif ch==3:
			PNR_num= int(raw_input('Enter the PNR number to be cancelled: '))
			print 'Ticket Keys: ',Ticket.keys() 
			for i in Ticket.keys():
				if PNR_num == Ticket[i].get('PNR_num'):
					Train.get(Ticket.get(i).get('train_num'))['seats'] += 1
					Ticket.pop(i)
					print 'Now the booked ticket are: ',Ticket
					print 'YOUR TICKET HAS BEEN CANCELLED....'
					print 'Your amount has been refunded'

		elif ch==4:
			print "\n\t\t\t\t\t\t\t\t",'YOU HAVE BEEN LOGGED OUT. KINDLY LOGIN AGAIN' ,main_page()
		else:
			print '\n\t\t\t\t\t\t\t\t','SORRY!!. WRONG CHOICE ENTERED..'

#===============================================================================================================================

def sign_in():
	print "\n\n\t\t\t\t",'=' * 80
	print '\n\t\t\t\t\t\t\t\t','LOGIN PAGE'
	
	u_name = raw_input('Enter your user name: ')
	password = raw_input('Enter your password: ')
	
	temp_dict ={'username' : u_name , 'password' : password }
	#print 'guest_user',guest_user
	#print 'temp_dict',temp_dict
	if super_user.has_key(temp_dict.get('username')) and super_user.get(temp_dict.get('username'))['password'] == temp_dict.get('password'):
		print '\n\t\t\t\t\t\t\t\t','ADMIN LOGIN SUCCESSFUL'
		admin_function()
		
	else:
		if guest_user.has_key(u_name) and guest_user.get(u_name)['password'] == password:
			print 'guest_user',guest_user
			user_func()
		else:
			print '\n\t\t\t','SORRY!!!! NO SUCH USER EXISTS'
			main_page()
#===============================================================================================================================

def sign_up():
	print "\n\n\t\t\t\t",'=' * 80
	print '\n\t\t\t\t\t\t\t\t','NEW USER SIGN UP'

	full_name =raw_input('Enter your full name: ')
	age= int(raw_input('Enter your age: '))
	u_name=raw_input('Enter the user name: ')
	if u_name == '':
		print 'You have entered either username or password blank. Enter the details again...'
		sign_up()
	password=raw_input('Enter the password: ')

	temp_dict = {'username' : u_name , 'password' : password , 'full_name': full_name , 'age' : age }

	if guest_user.has_key(temp_dict.get('username')):
		print '\n\t\t\t','USER ALREADY EXISTS IN RECORDS WITH SAME USERNAME. TRY WITH DIFFERENT ONE.'
		sign_in()
	else:
		guest_user[temp_dict.get('username')] ={'password':temp_dict.get('password'),'type':'guest','full_name': temp_dict.get('full_name') , 'age' : temp_dict.get('age') }
		print '\n\t\t\t\t','YOU HAVE BEEN SUCCESSFULLY ADDED TO OUR RECORDS. NOW YOU CAN LOGIN DIRECTLY'
		print '\n','NOW THE USERS ARE:',guest_user
		main_page()
#===============================================================================================================================

def main_page():
	while True:
		print "\n\t\t\t\t",'=' * 80
		print "\n\t\t\t\t\t\t\t",' WELCOME TO KARISHMA RAILWAYS'
		print "\n\t\t\t\t\t\t\t\t",'1. SIGN IN'
		print "\n\t\t\t\t\t\t\t\t",'2. SIGN UP'
		print "\n\t\t\t\t\t\t\t\t",'3. EXIT'
		print "\n\t\t\t\t", '='* 80
 		print 'Enter your choice:'
		ch = int(raw_input())
		
		if ch ==1:
			sign_in()

		elif ch ==2:
			sign_up()

		elif ch==3:
			print '\n\n','YOU HAVE BEEN LOGGED OUT. KINDLY LOGIN AGAIN' ,exit()

		else:
			print '\n\n','SORRY!!. WRONG CHOICE ENTERED..'
#Main
init()
main_page()