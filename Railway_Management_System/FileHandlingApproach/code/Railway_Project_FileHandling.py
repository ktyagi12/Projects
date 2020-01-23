#RAILWAY MANAGEMENT USING FILE HANDLING IN PYTHON
import json

guest_user={}
temp_user={}
train_temp={}
super_alt_user={}

def change_Passcode(u_name):
	with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\SuperUser.py','r') as superUser_file:
		file_data = superUser_file.read()
		temp_user = json.loads(file_data)
		if temp_user.has_key(u_name):
			print 'Username is a super user itself...'
			admin_function()
		with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','r') as guestUser_file:
			guestUser_file.seek(0)
			first = guestUser_file.read(1)
			if not first:
				print 'SORRY NO SUCH USER EXISTS IN OUR RECORDS...'
				admin_function()
			else:
				guestUser_file.seek(0)
				file_data = guestUser_file.read()
				temp_user = json.loads(file_data)
				if temp_user.has_key(u_name):
					with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','w') as guestUser_file:
						temp_user[u_name]['password'] = raw_input('Enter the changed password for the user %s: ' %u_name)
						data=json.dumps(temp_user,indent=2)
						guestUser_file.write(data)	
				else:
					print 'SORRY!!!! NO SUCH USER EXISTS'
#===============================================================================================================================

def make_User_Admin(u_name,password):
	with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','r') as guestUser_file:
		guestUser_file.seek(0)
		first = guestUser_file.read(1)
		if not first:
			print 'SORRY NO SUCH USER EXISTS IN OUR RECORDS...'
			admin_function()
		else:
			guestUser_file.seek(0)
			file_data = guestUser_file.read()
			temp_user = json.loads(file_data)
			if temp_user.has_key(u_name) and temp_user.get(u_name)['password'] == password:
				super_alt_user[u_name]={"password":password,"type":"super"}
				with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\SuperUser.py','w') as superUser_file:
					data=json.dumps(super_alt_user,indent=2)
					superUser_file.write(data)
					print 'SUCCESSFULLY GIVEN THE ADMIN PRIVILEGES TO %s USER' %u_name
					superUser_file.close()
					with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','r') as guestUser_file:
						guestUser_file.seek(0)
						file_data = guestUser_file.read()
						guest_user = json.loads(file_data)
						guest_user.pop(u_name)
						with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','w') as guestUser_file:
							guest_user = json.dump(guest_user, guestUser_file)
			else:
				print 'SORRY NO SUCH USER EXISTS IN OUR RECORDS...'
#===============================================================================================================================

def remove_Train(train_num):
	with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\TrainsInfo.py','r') as trainsInfo_file:
		trainsInfo_file.seek(0)
		first = trainsInfo_file.read(1)
		if not first:
			print 'NO SUCH TRAIN EXISTS....'
			admin_function()
		else:
			trainsInfo_file.seek(0)
			file_data = trainsInfo_file.read()
			temp_user = json.loads(file_data)
			trainsInfo_file.close()
			if temp_user.has_key(train_num):
				temp_user.pop(train_num)
				print '\n','SUCCESSFULLY REMOVED THE TRAIN'
				with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\TrainsInfo.py','w') as trainsInfo_file:
					temp_user = json.dump(temp_user, trainsInfo_file)
					print 'REMOVED FROM RECORDS '
			else:
				print 'SORRY!!!! NO SUCH TRAIN EXISTS.'
				print 'CHOOSE AGAIN:'
#===============================================================================================================================

def modify_Train(train_num):
	with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\TrainsInfo.py','r') as trainsInfo_file:
		trainsInfo_file.seek(0)
		first = trainsInfo_file.read(1)
		if not first:
			print 'NO SUCH TRAIN EXISTS....'
			admin_function()
		else:
			trainsInfo_file.seek(0)
			file_data = trainsInfo_file.read()
			temp_user = json.loads(file_data)
			trainsInfo_file.close()
			if temp_user.has_key(train_num):
				train_name = raw_input('Enter the modified train name: ')
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

				train_temp[train_num] = {'train_name':train_name,'train_src':train_src,'train_dest':train_dest,'running_days' : running_days,'seats':num_seats,'distance':distance,'fare': {'AC1': ac1,'AC2':ac2,'AC3':ac3,'SL':sl}}
				with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\TrainsInfo.py','w') as trainsInfo_file:
					data = json.dumps(train_temp,indent=2)
					trainsInfo_file.write(data)
					trainsInfo_file.close()
					print '\n','SUCCESSFULLY MODIFIED THE TRAIN'
					
			else:
				print '\n\t\t\t\t\t\t\t\t','SORRY!!!! NO SUCH TRAIN EXISTS.'
				print '\n\t\t\t\t\t\t\t\t','CHOOSE AGAIN:'
#===============================================================================================================================

def add_Train(num_of_train):
	train_count = 1
	while train_count<= num_of_train:
		train_num = raw_input('Enter the train number to be added: ')
		if train_num == '':
			print 'You have not entered any train number. Enter the details again...'
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
		
		train_temp[train_num] = {'train_name':train_name,'train_src':train_src,'train_dest':train_dest,'running_days' : running_days,'seats':num_seats,'distance':distance,'fare': {'AC1': ac1,'AC2':ac2,'AC3':ac3,'SL':sl}}
		
		with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\TrainsInfo.py','r') as trainsInfo_file:
			trainsInfo_file.seek(0)
			first = trainsInfo_file.read(1)
			if not first:
				trainsInfo_file.close()
				with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\TrainsInfo.py','w') as trainsInfo_file:
					data = json.dumps(train_temp,indent=2)
					trainsInfo_file.write(data)
					trainsInfo_file.close()
			else:
				trainsInfo_file.seek(0)
				file_data = trainsInfo_file.read()
				temp_user = json.loads(file_data)
				if temp_user.has_key(train_num):
					print 'TRAIN ALREADY IN RECORDS.'
					trainsInfo_file.close()
					admin_function()
				else:
					trainsInfo_file.close()
					with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\TrainsInfo.py','w') as trainsInfo_file:
						data = json.dumps(train_temp,indent=2)
						trainsInfo_file.write(data)
						trainsInfo_file.close()
			print '\n','SUCCESSFULLY ADDED TRAIN'
			
		train_count+= 1
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
			train_num = raw_input('Enter the train number to be modified: ')
			modify_Train(train_num)
			
		elif ch==3:   #REMOVE TRAIN
			train_num = raw_input('Enter the train number to be removed: ')
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


def sign_in():
	print "\n\n\t\t\t\t",'=' * 80
	print '\n\t\t\t\t\t\t\t\t','LOGIN PAGE'
	
	u_name = raw_input('Enter your user name: ')
	password = raw_input('Enter your password: ')
	
	temp_dict ={'username' : u_name , 'password' : password }

	with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\SuperUser.py','r') as superUser_file:
		file_data = superUser_file.read()
		temp_user = json.loads(file_data)
			
		if temp_user.has_key(temp_dict.get('username')) and temp_user.get(temp_dict.get('username'))['password'] == temp_dict.get('password'):
			print '\n\t\t\t\t\t\t\t\t','ADMIN LOGIN SUCCESSFUL'
			superUser_file.close()
			admin_function()
		else:
			with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','r') as guestUser_file:
				guestUser_file.seek(0)
				first = guestUser_file.read(1)
				if not first:
					print 'SORRY!! YOU ARE NOT A REGISTERED USER... KINDLY SIGN UP FIRST'
					sign_up()
				else:
					guestUser_file.seek(0)
					file_data1 = guestUser_file.read()
					temp_user1 = json.loads(file_data1)
					if temp_user1.has_key(u_name) and temp_user1.get(u_name)['password'] == password:
						user_func()
					else:
						print '\n\t\t\t','SORRY!!!! NO SUCH USER EXISTS'

	main_page()
#===============================================================================================================================

def sign_up():
	print "\n\n\t\t\t\t",'=' * 80
	print '\n\t\t\t\t\t\t\t\t','NEW USER SIGN UP PAGE'
	full_name =raw_input('Enter your full name: ')
	age= int(raw_input('Enter your age: '))
	u_name=raw_input('Enter the user name: ')
	password=raw_input('Enter the password: ')
	
	if u_name == '' or password == '':
		print 'You have entered either username or password blank. Enter the details again...'
		sign_up()
	
	guest_user[u_name]={'password' : password , 'full_name': full_name , 'age' : age }
	
	with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','r') as guestUser_file:
		guestUser_file.seek(0)
		first = guestUser_file.read(1)
		if not first:
			guestUser_file.close()
			with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','w') as guestUser_file:
				data=json.dumps(guest_user,indent=2)
				guestUser_file.write(data)
		else:
			guestUser_file.close()
			with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','r') as guestUser_file:
				file_data = guestUser_file.read()
				temp_user = json.loads(file_data)
				if temp_user.has_key(u_name):
					print '\n\t\t\t','USER ALREADY EXISTS IN RECORDS WITH SAME USERNAME. TRY WITH DIFFERENT ONE.'
					guestUser_file.close()
					sign_up()

				else:
					guestUser_file.close()
					with open('D:\KTyagi\KT\Python_Workspace\Railways_FileHandling\GuestUser.py','w') as guestUser_file:
						data=json.dumps(guest_user,indent=2)
						guestUser_file.write(data)
						guestUser_file.close()
				
	print '\n\t\t\t\t','YOU HAVE BEEN SUCCESSFULLY ADDED TO OUR RECORDS. NOW YOU CAN LOGIN DIRECTLY'
	main_page()

#=======================================================================================================

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



main_page()