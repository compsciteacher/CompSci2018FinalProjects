import os, time, random

status = {'Warrior Level': 1, 'Turrets Level': 1, 'Gate Level': 1, 'Enemies': 100, 'Round' : 1} #Dictionary with status for king
stats = {'Minion Level': 1, 'Cannons Level': 1, 'Sentinel Level': 1, 'Enemies': 100, 'Round' : 1} #Dictionary with stats for assassin
option = []
roundstatus = None

def playerinfo ():
	os.system('clear')
	print('Welcome to PyConquest!')
	time.sleep(1.5)
	name = input('What is your name? ') #Asks name
	name = name.title()
	print ('Hello %s!' %(name))
	time.sleep(1.5)
	return name
playerinfo()

def gamestart():

	os.system('clear')

	print('PyConquest\nEnter New Game to start a new game.\nEnter Load Game to continue from exit point.\nEnter Quit to quit.') #Asks options
	menu = input('')
	menu = menu.upper()
	if menu == 'NEW GAME': #If new game
		classes() #Goes to classes function
	elif menu == 'LOAD GAME': #If load game
		try: #Tries to pull out saved data and put into dictionary
			load = open('/storage/sdcard0/Download/gamesave.txt', 'r')
			loading = load.readlines()
			loading = [item.strip('\n') for item in loading]
			time.sleep(1.5)
			if loading[5] == 'king':
				status['Warrior Level'] = int(loading[0])
				status['Turrets Level'] = int(loading[1])
				status['Gate Level'] = int(loading[2])
				status['Enemies'] = int(loading[3])
				status['Round'] = int(loading[4])
				load.close()
				king()
			elif loading[5] == 'assassin':
				stats['Minion Level'] = int(loading[0])
				stats['Cannons Level'] = int(loading[1])
				stats['Sentinel Level'] = int(loading[2])
				stats['Enemies'] = int(loading[3])
				stats['Round'] = int(loading[4])
				load.close()
				assassin()
		except IOError: #If IOError
			print('No saved data. You will have to start the game from the beginning.')
			classes() #States no saved file and goes to classes to start new game
	elif menu == 'QUIT': #If quit
		quit() #Quits game
	else:
		print('You did something wrong. Try again.') #If error
		time.sleep(1.5)
		gamestart() #Restarts function

def classes():
	os.system('clear')
	global option	
	print ('Choose a Class:\nKing\nAssassin\nEnter Quit to quit.') #Lists classes and asks if need to quit
	options = input('')
	options = options.upper()
	option.append(option)
	if options == 'KING':
		time.sleep(1)
		king() #If king enter goes to king function
	elif options == 'ASSASSIN':
		time.sleep(1)
		assassin() #If assassin is entered goes to assassin function
	elif options == 'QUIT':
		quit()
	else:
		print('You did something wrong.')
		time.sleep(1)
		classes()
def king():
	global roundstatus
	global option
	time.sleep(1.5)
	os.system('clear')
	if status['Round'] == 1:
		print("You are the king. Your job is to strengthen your army and fortify your defenses.")
		time.sleep(1.5)
		print("You will have 15 bloody battles against an evil Assassin attempting to take over your kingdom.")
		time.sleep(1.5)
	while True: #While statment so it goes until victory
		if status['Round'] >= 16: #Complete level 15 then you have a boss fight
			os.system('clear')
			print ('All your warriors and all your enemies are dead. The only ones left alive is you, the King, and the leader of your enemies, The Assassin.')
			time.sleep(1.5)
			print ('You both see this as an opportunity. Not a peace treaty but the ultimate battle that will permanantly get rid of the enemy.')
			time.sleep(1.5)
			print ('Both of you head to the center of the battlefield armed to the teeth.')
			time.sleep(1.5)
			King = status['Warrior Level'] * 500
			Assassin = King
			Kpower = round(King/5)
			Apower = Kpower
			o1 = round(Kpower * 1.1)
			o2 = round(Apower * 2.5)
			Critical = random.randrange(o1, o2)
			for i in range(Assassin+King):
				if King <= 0:
					print('You lose this round. If you wish to retry enter something. If you wish to quit then enter Quit.')
					redo = input('')
					redo = redo.upper()
					if redo == 'QUIT':
						quit()
					else:
						King = status['Warrior Level'] * 500
						Assassin = King
						continue
				elif Assassin <= 0: #Resets save
					status['Round'] = 1
					status['Warrior Level'] = 1
					status['Turrets Level'] = 1
					status['Gate Level'] = 1
					status['Enemies'] = 100
					savedata = open('/storage/sdcard0/Download/gamesave.txt', 'w')
					savedata.write(str(1) + '\n')
					savedata.write(str(1) + '\n')
					savedata.write(str(1) + '\n')
					savedata.write(str(100) + '\n')
					savedata.write(str(1) + '\n')
					savedata.write(str('king)') + '\n')
					savedata.close()
					print('You win! You have successfully beaten the game.')
					time.sleep(1.5)
					quit()
				os.system('clear')
				print ('Your HP:%i' %(King))
				time.sleep(1.5)
				print ('Asssassin HP:%i' %(Assassin))
				time.sleep(1.5)
				CritChance = random.randrange(1, 6)
				CritChance2 = random.randrange(1, 6)
				print('Enter Attack to Attack.\nEnter Defend to Defend.\nEnter Surrender to give up.')
				time.sleep(1.5)
				movement = input('')
				movement = movement.upper()
				enemymove = random.randrange(1,3)
				if movement == 'ATTACK':
					if enemymove == 1:
						if CritChance == 5:
							Assassin -= Critical
							print ('Your attack landed a critical blow on the enemy. The Assassin took %i damage.' %(Critical))
							time.sleep(1.5)
						else:
							Assassin -= Kpower
						print ('The Assassin took %i damage.' %(Kpower))
						time.sleep(1.5)
						if CritChance2 == 5:
							King -= Critical
							print ('The Assassin landed a critical blow on the you. You took %i damage.' %(Critical))
							time.sleep(1.5)
						else:
							King -= Apower
							print ('The Assassin attacked you. You took %i damage' %(Apower))
							time.sleep(1.5)
					elif enemymove >= 2:
						print('The Assassin Defended himself.')
						time.sleep(1.5)
						Assassin -= round(Kpower*.5)
						damage = round(Kpower*.5)
						print ('The Assassin took %i damage.' %(damage))
						time.sleep(1.5)
				elif movement == 'DEFEND':	
					King -= round(Apower*.5)
					damage = round(Apower*.5)
					print ("You defended. The Assassin's attack damage was %i" %(damage))
					time.sleep(1.5)
				elif movement == 'SURRENDER':
					print ('Congratulations! Surrender was successful. You were too cowardly to fight the Assassin and have lost everything. You have shamed everyone you know.')
				time.sleep(1.5)
				quit()
			else:
				print('You did something wrong. Try again!')
				time.sleep(1.5)
		os.system('clear')
		status['Enemies'] = status['Round'] * 100
		for akey in status.keys(): #Shows stuff in dictionary
			value = status[akey]
			print ('%s : %i' %(akey, value))
		time.sleep(1.5)
		gatehealth = status['Gate Level'] * 100
		warriors = status['Warrior Level'] * 100
		turretaccuracy = random.randrange(1, status['Turrets Level'] * 25)
		status['Enemies'] = status['Enemies'] - turretaccuracy

		if status['Enemies'] <= 0:
			print("Your turrets managed to destroy all the enemies")
			print ("You are left with %i warriors." %(warriors))
			time.sleep(1.5)
			roundstatus = 'Win'
			transferround()
			break
		def ready():
			os.system('clear')
			fight = input('Your troops and weapons are ready. Are you ready to fight? (Yes or No) ')
			fight = fight.upper()
			if fight == 'YES':
				return True
			elif fight == 'NO':
				print ('You will be taken to the menu...')
				time.sleep(1.5)
				gamestart()
			else:
				print ('You did something wrong. Try again.')
				time.sleep(1.5)
				ready()
		if ready() == True:
			print('Commencing Battle...')	
			time.sleep(1.5)
		for x in range(status['Enemies']):

			if status['Enemies'] <= 0: #If no enemies you win
				print("Your enemies were successfully destroyed! You win this round!")
				time.sleep(1.5)
				print ("You are left with %i warriors" %(warriors))
				time.sleep(1.5)
				roundstatus = 'Win'
				transferround()
				break
			if gatehealth > 0: #Destroys gate 
				gatehealth -= 10
				
				if gatehealth <= 0:
					print ('Your gate has been destroyed and the turrets have fallen!')
					time.sleep(1.5)
					print ("You have %i warriors ready to fight." %(warriors))
					time.sleep(1.5)
		def deploy(): #Calls fighters to front lines
			os.system('clear')
			global roundstatus
			amount = input('How many warriors would you like to send to the front lines?  Your limit is %i warriors.\nKeep in mind that enemy invaders have been spotted inside your base.\nYou must keep 10 warriors in base unless your first wave of troops were all killed. ' %(warriors))
			try:
				amount = int(amount)
			except ValueError:
				print('Please use numbers.')
				time.sleep(1.5)
				print('You must restart this round and your mistake.')
				time.sleep(1.5)
				roundstatus = 'Lose'
				transferround()
			if amount <= warriors:
				return amount
			elif amount > warriors:
				print("You can't send that many warriors. You only have %i warriors." %(warriors))
				time.sleep(1.5)
				print('You must restart this round and your mistake.')
				time.sleep(1.5)
				roundstatus = 'Lose'
				transferround()
			else:
				print("You did something wrong. Try again.")
				time.sleep(1.5)
				print('You must restart this round and fix your mistake.')
				time.sleep(1.5)
				roundstatus = 'Lose'
				transferround()
		fighters = deploy()
		warriors = warriors - fighters
		if warriors < 10:
			print('You did not have at least 10 people inside the base and as a result your base was taken over. You lose this round!')
			time.sleep(1.5)
			roundstatus = 'Lose'
			transferround()
			break
		if gatehealth <= 0:
			for x in range(status['Enemies']): #Each fighter dies killing each enemy
				if status['Enemies'] > 0:
					status['Enemies'] = status['Enemies'] - 1
					fighters -= 1
					if fighters <= 0 and not status['Enemies'] <= 0:
						print ('The troops you sent in all been killed')
						time.sleep(1.5)
						print ('%i enemies remain alive and are about to break in.' %(status['Enemies']))
						time.sleep(1.5)
						print('You must send backup.')
						time.sleep(1.5)
						fighters = deploy()
						warriors = warriors - fighters
						continue
					if warriors <= 0 and fighters <= 0:
						print ('All your warriors have been killed! You lose this round!')
						time.sleep(1.5)
						roundstatus = 'Lose'
						transferround()
						break
						
					elif status['Enemies'] <= 0:
						print("Your enemies were successfully destroyed!")
						time.sleep(1.5)
						warriors = warriors + fighters
						print ("You are left with %i warriors" %(warriors))
						time.sleep(1.5)
						print ("All the warriors have been recalled to base to fight the invaders that snuck in while the warriors were battling on the front lines.")#Calls warriors to base
						time.sleep(1.5)
						print ("There is a small chance of reinforcments, however it is not to be expected and all efforts will be put into defending the base.")
						time.sleep(1.5)
						warriors = warriors + fighters
						fighters = 0
						invaders = random.randrange(1, warriors + 5)
						ranger = max(invaders, warriors)
						for i in range(ranger):
							warriors -= 1
							invaders -= 1
							if warriors <= 0 and not invaders <=0:
								print('The invaders have mercilessly defeated all your warriors enemies. There are %i invaders left alive.' %(invaders-warriors))
								time.sleep(1.5)
								roundstatus = 'Lose'
								transferround()
								break
							elif invaders <= 0 and warriors > 0:
								print ('All the invaders have been killed by your warriors. %i warriors are left standing.' %(warriors-invaders))
								time.sleep(1.5)								
								roundstatus = 'Win'
								transferround()
								break
def assassin():
	global roundstatus
	global option
	#Use the possible deploy fix with while True
	#option fix
	os.system('clear')
	if stats['Round'] == 1:
		print("You are an Assassin. You have conquered countless empires and made them your own. The whole world is under your control, and one kingdom alone is left to rebel. You have gathered ruthless killers and forced them to be your minions so that you can stop the rebellion.")
		time.sleep(3)
		print("You will have 15 bloody battles against a disgustingly kind king to cruelly rule over your empire.")
		time.sleep(1.5)
	while True: #While statment so it goes until victory
		if stats['Round'] >= 16: #Complete level 15 then you have a boss fight
			os.system('clear')
			print ('All your minions and all your enemies are dead. The only ones left alive is you, the Assassin, and the leader of your enemies, The King.')
			time.sleep(1.5)
			print ('You both see this as an opportunity to permanantly get rid of your enemy.')
			time.sleep(1.5)
			print ('Both of you head to the center of the battlefield armed to the teeth.')
			time.sleep(1.5)
			Assassin = stats['Minion Level'] * 500
			King = Assassin
			Apower = round(Assassin/5)
			Kpower = Apower
			o1 = round(Apower * 1.1)
			o2 = round(Kpower * 2.5)
			Critical = random.randrange(o1, o2)
			for i in range(Assassin+King):
				if Assassin <= 0:
					print('You lose this round. If you wish to retry enter something. If you wish to quit then enter Quit.')
					redo = input('')
					redo = redo.upper()
					if redo == 'QUIT':
						quit()
					else:
						Assassin = stats['Minion Level'] * 500
						King = Assassin
						continue
				elif King <= 0: #Resets save
					stats['Round'] = 1
					stats['Minion Level'] = 1
					stats['Cannons Level'] = 1
					stats['Sentinel Level'] = 1
					stats['Enemies'] = 100
					savedata = open('/storage/sdcard0/Download/gamesave.txt', 'w')
					savedata.write(str(1) + '\n')
					savedata.write(str(1) + '\n')
					savedata.write(str(1) + '\n')
					savedata.write(str(100) + '\n')
					savedata.write(str(1) + '\n')
					savedata.write(str('assassin') + '\n')
					savedata.close()
					print('You win! You have successfully beaten the game.')
					time.sleep(1.5)
					quit()
				os.system('clear')
				print ('Your HP:%i' %(Assassin))
				time.sleep(1.5)
				print ('King HP:%i' %(King))
				time.sleep(1.5)
				CritChance = random.randrange(1, 6)
				CritChance2 = random.randrange(1, 6)
				print('Enter Attack to Attack.\nEnter Defend to Defend.\nEnter Surrender to give up.')
				time.sleep(1.5)
				movement = input('')
				movement = movement.upper()
				enemymove = random.randrange(1,3)
				if movement == 'ATTACK':
					if enemymove == 1:
						if CritChance == 5:
							King -= Critical
							print ('Your attack landed a critical blow on the enemy. The King took %i damage.' %(Critical))
							time.sleep(1.5)
						else:
							King -= Apower
						print ('The King took %i damage.' %(Apower))
						time.sleep(1.5)
						if CritChance2 == 5:
							Assassin -= Critical
							print ('The King landed a critical blow on the you. You took %i damage.' %(Critical))
							time.sleep(1.5)
						else:
							Assassin -= Kpower
							print ('The King attacked you. You took %i damage' %(Kpower))
							time.sleep(1.5)
					elif enemymove >= 2:
						print('The King Defended himself.')
						time.sleep(1.5)
						King -= round(Apower*.5)
						damage = round(Apower*.5)
						print ('The King took %i damage.' %(damage))
						time.sleep(1.5)
				elif movement == 'DEFEND':	
					Assassin -= round(Kpower*.5)
					damage = round(Kpower*.5)
					print ("You defended. The King's attack damage was %i" %(damage))
					time.sleep(1.5)
				elif movement == 'SURRENDER':
					print ('Congratulations! Surrender was successful. You were too cowardly to fight the Assassin and have lost everything. You have shamed everyone you know.')
					time.sleep(1.5)
					quit()
				else:
					print('You did something wrong. Try again!')
					time.sleep(1.5)
		os.system('clear')
		stats['Enemies'] = stats['Round'] * 100
		for akey in stats.keys(): #Shows stuff in dictionary
			value = stats[akey]
			print ('%s : %i' %(akey, value))
		time.sleep(1.5)
		sentinelhealth = stats['Sentinel Level'] * 100
		minions = stats['Minion Level'] * 100
		cannonaccuracy = random.randrange(1, stats['Cannons Level'] * 25)
		stats['Enemies'] = stats['Enemies'] - cannonaccuracy

		if stats['Enemies'] <= 0:
			print("Your cannons managed to destroy all the enemies")
			print ("You are left with %i minions." %(minions))
			time.sleep(1.5)
			roundstatus = 'Win'
			roundtransfer()
			break
		def ready():
			os.system('clear')
			fight = input('Your minions and cannons are ready. Are you ready to fight? (Yes or No) ')
			fight = fight.upper()
			if fight == 'YES':
				return True
			elif fight == 'NO':
				print ('You will be taken to the menu...')
				time.sleep(1.5)
				gamestart()
			else:
				print ('You did something wrong. Try again.')
				time.sleep(1.5)
				ready()
		if ready() == True:
			print('Commencing Battle...')	
			time.sleep(1.5)
		for x in range(stats['Enemies']):

			if stats['Enemies'] <= 0: #If no enemies you win
				print("Your enemies were successfully destroyed!")
				time.sleep(1.5)
				print ("You are left with %i minions" %(minions))
				time.sleep(1.5)
				roundstatus = 'Win'
				roundtransfer()
				break
			if sentinelhealth > 0: #Destroys gate 
				sentinelhealth -= 10
				
				if sentinelhealth <= 0:
					print ('Your sentinels have been destroyed and the cannons have fallen!')
					time.sleep(1.5)
					print ("You have %i minions ready to fight." %(minions))
					time.sleep(1.5)
		def deploy(): #Calls fighters to front lines
			os.system('clear')
			global roundstatus
			amount = input('How many minions would you like to send to the front lines?  Your limit is %i minions.\nKeep in mind that enemy invaders have been spotted inside your base.\nYou must keep 10 minions in base unless your first wave of minions were all killed. ' %(minions))
			try:
				amount = int(amount)
			except ValueError:
				print('Please use numbers.')
				time.sleep(1.5)
				print('You must restart this round and your mistake.')
				time.sleep(1.5)
				roundstatus = 'Lose'
				roundtransfer()
			if amount <= minions:
				return amount
			elif amount > minions:
				print("You can't send that many minions. You only have %i minions." %(minions))
				time.sleep(1.5)
				print('You must restart this round and fix your mistake.')
				time.sleep(1.5)
				roundstatus = 'Lose'
				roundtransfer()
			else:
				print("You did something wrong. Try again.")
				time.sleep(1.5)
				print('You must restart this round and your mistake.')
				time.sleep(1.5)
				roundstatus = 'Lose'
				roundtransfer()
		fighters = deploy()
		minions = minions - fighters
		if minions < 10:
			print('You did not have at least 10 minions inside the base and as a result your base was taken over. You lose this round!')
			time.sleep(1.5)
			roundstatus = 'Lose'
			roundtransfer()
			break
		if sentinelhealth <= 0:
			for x in range(stats['Enemies']): #Each fighter dies killing each enemy
				if stats['Enemies'] > 0:
					stats['Enemies'] = stats['Enemies'] - 1
					fighters -= 1
					if fighters <= 0 and not stats['Enemies'] <= 0:
						print ('The minions you sent in all been killed')
						time.sleep(1.5)
						print ('%i enemies remain alive and are about to break in.' %(stats['Enemies']))
						time.sleep(1.5)
						print('You must send backup.')
						time.sleep(1.5)
						fighters = deploy()
						minions = minions - fighters
						continue
					if minions <= 0 and fighters <= 0:
						print ('All your minions have been killed! You lose this round!')
						time.sleep(1.5)
						roundstatus = 'Lose'
						roundtransfer()
						break
						
					elif stats['Enemies'] <= 0:
						print("Your enemies were successfully destroyed! You win this round!")
						time.sleep(1.5)
						minions = minions + fighters
						print ("You are left with %i minions" %(minions))
						time.sleep(1.5)
						print ("All the minions have been recalled to base to fight the invaders that snuck in while the minions were battling on the front lines.")#Calls minions to base
						time.sleep(1.5)
						print ("There is a small chance of reinforcments, however it is not to be expected and all efforts will be put into defending the base.")
						time.sleep(1.5)
						minions = minions + fighters
						fighters = 0
						invaders = random.randrange(1, minions + 5)
						ranger = max(invaders, minions)
						for i in range(ranger):
							minions -= 1
							invaders -= 1
							if minions <= 0 and not invaders <= 0:
								print('The invaders have mercilessly defeated all your minions enemies. There are %i invaders left alive.' %(invaders-minions))
								time.sleep(1.5)
								roundstatus = 'Lose'
								roundtransfer()
								break
							elif invaders <= 0 and minions > 0:
								print ('All the invaders have been killed by your minions. %i minions are left standing.' %(minions-invaders))
								time.sleep(1.5)								
								roundstatus = 'Win'
								roundtransfer()
								break

def transferround(): #Function auto saves data wheather win or lose. If win go to next round if you lose you get to repeate the round.
	os.system('clear')
	global roundstatus
	if roundstatus == 'Win': #If round was beaten goes to next round and level up with auto data save
		status['Round'] = status['Round'] + 1
		status['Warrior Level'] = status['Warrior Level'] + 1
		status['Turrets Level'] = status['Turrets Level'] + 1
		status['Gate Level'] = status['Gate Level'] + 1
		savedata = open('/storage/sdcard0/Download/gamesave.txt', 'w')
		savedata.write(str(status['Warrior Level']) + '\n')
		savedata.write(str(status['Turrets Level']) + '\n')
		savedata.write(str(status['Gate Level']) + '\n')
		savedata.write(str(status['Round'] * 100) + '\n')
		savedata.write(str(status['Round']) + '\n')
		savedata.write(str('king'.lower()))
		savedata.close()
		print('Data has been saved.')
		time.sleep(1.5)
		decide = input('Enter anything to keep playing or enter Quit to quit. ')
		decide = decide.upper()
		if decide == 'QUIT':
			quit()
		else:
			print('Starting next round...')
			time.sleep(1.5)
			king()
	elif roundstatus == 'Lose': #Lose round and you restart and data auto saves
		retry = input('Would you like to try the round again? If so enter anything, otherwise enter Quit. ')
		retry = retry.upper()
		if retry == 'QUIT':
			savedata = open('/storage/sdcard0/Download/gamesave.txt', 'w')
			savedata.write(str(status['Warrior Level']) + '\n')
			savedata.write(str(status['Turrets Level']) + '\n')
			savedata.write(str(status['Gate Level']) + '\n')
			savedata.write(str(status['Round'] * 100) + '\n')
			savedata.write(str(status['Round']) + '\n')
			savedata.write(str('king'.lower()))
			savedata.close()
			print('Data has been saved.')
			time.sleep(1.5)
			quit()
		else:
			status['Round'] = status['Round'] + 0
			savedata = open('/storage/sdcard0/Download/gamesave.txt', 'w')
			savedata.write(str(status['Warrior Level']) + '\n')
			savedata.write(str(status['Turrets Level']) + '\n')
			savedata.write(str(status['Gate Level']) + '\n')
			savedata.write(str(status['Round'] * 100) + '\n')
			savedata.write(str(status['Round']) + '\n')
			savedata.write(str('king'.lower()))
			savedata.close()
			print('Data has been saved.')
			time.sleep(1.5)
			king()
def roundtransfer():
	os.system('clear')
	global roundstatus
	if roundstatus == 'Win': #If round was  beaten goes to next round and level up with auto data save
		stats['Round'] = stats['Round'] + 1
		stats['Minion Level'] = stats['Minion Level'] + 1
		stats['Cannons Level'] = stats['Cannons Level'] + 1
		stats['Sentinel Level'] = stats['Sentinel Level'] + 1
		savedata = open('/storage/sdcard0/Download/gamesave.txt', 'w')
		savedata.write(str(stats['Minion Level']) + '\n')
		savedata.write(str(stats['Cannons Level']) + '\n')
		savedata.write(str(stats['Sentinel Level']) + '\n')
		savedata.write(str(stats['Round'] * 100) + '\n')
		savedata.write(str(stats['Round']) + '\n')
		savedata.write(str('assassin'.lower()))
		savedata.close()
		print('Data has been saved.')
		decide = input('Enter anything to keep playing or enter Quit to quit. ')
		decide = decide.upper()
		if decide == 'QUIT':
			quit()
		else:
			print('Starting next round...')
			time.sleep(1.5)
			assassin()
	elif roundstatus == 'Lose': #Lose round and you restart and data auto saves
		retry = input('Would you like to try the round again? If so enter anything, otherwise enter Quit. ')
		retry = retry.upper()
		if retry == 'QUIT':
			savedata = open('/storage/sdcard0/Download/gamesave.txt', 'w')
			savedata.write(str(stats['Minion Level']) + '\n')
			savedata.write(str(stats['Cannons Level']) + '\n')
			savedata.write(str(stats['Sentinel Level']) + '\n')
			savedata.write(str(stats['Round'] * 100) + '\n')
			savedata.write(str(stats['Round']) + '\n')
			savedata.write(str('assassin'.lower()))
			savedata.close()
			print('Data has been saved.')
			time.sleep(1.5)
			quit()
		else:
			savedata = open('/storage/sdcard0/Download/gamesave.txt', 'w')
			savedata.write(str(stats['Minion Level']) + '\n')
			savedata.write(str(stats['Cannons Level']) + '\n')
			savedata.write(str(stats['Sentinel Level']) + '\n')
			savedata.write(str(stats['Round'] * 100) + '\n')
			savedata.write(str(stats['Round']) + '\n')
			savedata.write(str('assassin'.lower()))
			savedata.close()
			print('Data has been saved.')
			time.sleep(1.5)
			assassin()
gamestart()