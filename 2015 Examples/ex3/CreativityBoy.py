import os, time
os.system('clear') #import os and time and clear junk
check1="false"
check2="false" #create 2 variables that will change the game depending on path
def main():
		def beginning():
				os.system('clear') 
				global name #clear the screen and get their names
				print("""	
	It is a stormy day. You find yourself in a field by yourself. Lightning is striking everywhere but there is no cover in sight. You try to run away but lightning hits you and you black out knowing full well that you may never again awaken.
		
	"Wake up, mister" a voice calls to you. You open you eyes and not only there is a girl standing over you but a group of people surround you. "Sir, the people here have gathered to talk to you of a disaster.
		""") #print the scenario
				option=input(name+", what do you want to do?"+"""
	Type 1 to listen to their story
		
	Type 2 to wet your pants
		
	Type 3 to fight
		
	Type 4 to quit
	""") #ask them what they want to do
				if option=="1":
						story() #move on
				elif option=="2":
						print("You wet your pants but that doesn't seem to change anything...")
						time.sleep(5)
						story() #talk and move on
				elif option=="3":
						print(""""I guess we were wrong about you, sir" the girl says. The peope start to attack you, and you try to fight back but you fail to put up a fight and die.""")
						time.sleep(5)
						beginning() #let them fail and retry
				elif option=="4":
						print("Your password is thunder")
						time.sleep(5)
						quit() #tell them their password and quit
				else:
						print("Your input is invalid. Try again.")
						time.sleep(5)
						beginning() #tell them the choice is invalid and restart
		def story():
				global name
				os.system('clear') #get name and clear screen
				print("""
	"I knew you would listen, sir" she says.
	"Who are you?" you ask.
	"I am Zelda, princess of Hyrule"
	"But you're not real!"
	"Oh, but I am, but not in your world."
	"That makes no sense."
	"Then listen. At the dawn of man, your race lacked what would set you apart from all the other animals on Earth, imagination. Only one man truly had this vision to make things happen. He knew had to spread this idea if mankind was to survive. He sacrificed his life to give us life. We knew us alone could not keep it thriving. So, we decided that every 100 years, when mankind's need was greatest we would grant special powers to one who most represented the old one. This power would allow him or her to summon us to their world to help. You are the next in line for the job. You are Creativity Boy"
	"I'm only 15 years old!"
	"But you are the perfect age. You are old enough to think deeply, but young enough to believe in us."
	"Wait, you said 'when mankind's need is greatest', what's wrong?"
	"An enemy not of this earth. This comes from an alien race who is so old and has not been seen for so long that we had all but forgotten them. They hate imagination and rely on cunning. They are called Xenomorph"
	"How can I help? I'm stuck here with you and I don't know where to start"
	"We can help with that. You can either head to Paris to meet someone who knew the hero before and could give you more info or you could head to Fort Hood to train with one of our contacts there. We'll provide transport either way.
	""")		
				time.sleep(15) #give scenario and slow program
				choice=input(name+""", What is your decision?
	Type 1 to head to Paris
	
	Type 2 to Fort Hood in Texas
	
	Type 3 to deny your destiny
	
	Type 4 to quit
	""") #ask them for their option
				if choice=="1":
						print("You tell her that you want to go to Paris and she teleports you.")
						time.sleep(5)
						paris() #move on to their choice
				elif choice=="2":
						print("You tell her Fort Hood is your destination and she sends you off.")
						time.sleep(5)
						hood() #move on to the other choice
				elif choice=="3":
						print(""'"If you wish, sir, but the world is doomed. Unfortunately, we cannot let you leave with this memory in case the Xenomorph get you. You must die."'"")
						time.sleep(7)
						story() #tell them they died and retry
				elif choice=="4":
						print("Your password is xenomorph")
						time.sleep(5)
						quit() #tell them the password and quit
				else:
						print("Your input was invalid, try again.")
						time.sleep(5)
						story() #if it is an invalid password, restart
		def hood():
				os.system('clear')
				global check1
				global check2
				global name #get name, clear screen, and get the 2 variables that will change the level, if necessary
				print("""
	You find yourself in Texas in the middle of the summer in front of the gate. Even now you're sweating, but you walk up to the gate anyway. "Sir, do you have an ID?" the soldier asks. You dig in your pocket for hope that you have something. Your hand closes around plastic and you look at it. It's a fake ID. You give it to the soldier and he sends you off.
	You don't know where to look for this contact but he must be of some rank. You see a visitor center and walk in because it is as good of place as any. You ask the receptionist for help and she points to you to the general of the fort. 
	"Are you the contact I'm looking for?" you ask.
	"That depends, Private, on who you're looking for."
	"Zelda told me that you could help me train. I'm Creativity Boy."
	"Did she now? I guess I'm your man then. But I warn you, you will be treated as every other soldier here and you will train hard, Private."
	"Sir, yes sir!"
	You work hard for several weeks and soon you are in tip top physical condition and you are ready to face any threat.
	"Sir, may I take leave now?"
	"Why son? You are powerful but not quite ready to fight."
	"I am ready"
	"Ok, but I must test you first" """)
				time.sleep(25) #give scenario
				print("""
	Just then, an alien breaks into the room. It's a Xenomorph!. The general tries to fight but is no match. You evaluate your options and decide there is no choice but to fight.""")
				option=input(name+""", what is your decision?
	Type 1 to try to turn traitor and ask to join them
	
	Type 2 to summon Luke Skywalker to your side
	
	Type 3 to call an airstrike from the Star Fox team
	""") #ask for choice
				if option=="1":
						print("You try to talk to the alien, but it doesn't seem to understand English. It kills you with a horn stab to the chest. You know you should have never tried to turn traitor")
						time.sleep(7)
						hood() #tell that they died and restart
				elif option=="2":
						print("Young Skywalker bursts from nowhere and begins to fight with the Xenomorph. SSSS, he cuts off the alien's head. The general wakes up and tells you that you did a great job.")
						time.sleep(7) #move on
				elif option=="3":
						print("You look out the window and see the four Arwings and know to duck and cover. You grab the general and dive behind a desk. The Smart Bomb incinerates the Xenomorph and you are unscathed.") 
						time.sleep(7) #move on
				else:
						print("Your input is invalid, try again.")
						time.sleep(7)
						hood() #tell them option is not real and restart
				if check1=="false":
						os.system('clear') #if paris is not done, do this
						print("""
	"Son, you deserve a medal for your bravery. Unfortunately, the army doesn't hand out medals for magic."
	"That's OK, general."
	"I wish I could say that was the only Xenomorph in the world, but that would be a lie. You need to complete your training and it isn't going to happen here."
	"Where do I head then, general"
	"You need to head to Paris"
	"Why?"
	"I am only able to teach you the physical part of your training. Paris will teach you the mental. Remember, knowing is the first step to victory."
	"See you later, sir"
	"I'll make sure Zelda sends you transportation" """)
						quit=input("Do you want to quit? Type 1 for yes and anything else for no ") #print good-bye and ask if they want to quit
						if quit=="1":
								print("Your password is death star")
								time.sleep(7)
								quit() #tell them the password and quit
						time.sleep(20)
						check2=="true"
						paris() #change the variable so paris changes and do paris
				elif check1=="true":
						os.system('clear') #if paris is done do this
						print("""
	"Son, you sure have learned much in your short training. If you were a soldier, I would be putting a patch on your chest promoting you."
	"Where do I go now?"
	"You are going back to meet Zelda to discuss strategy"
	"Why?"
	"We tried to keep this a secret, but the Xenomorph have already invaded New York City"
	"NOOOOO!!! Now we'll never get decent pizza!"
	"I share your concern, son, but we need straegy and I have never seen one quite as good as Zelda"
	"LET'S GO!" """)
						quit=input(name+", do you want to quit now? Type 1 for yes, and anything else for no ") #print statment and ask if they want to quit
						if quit=="1":
								print("Your password is barrel roll")
								time.sleep(7)
								quit() #tell them their password and quit
						time.sleep(15)
						zelda() #if paris is done, move on
		def paris():
				os.system('clear')
				global check1
				global check2
				global name #clear screen, get name, and get two variables that change level
				print("""
	You find yourself in the middle of winter in Paris. It's pretty, but you start to shiver. You need to find this person who knew the last hero. You walk into a cafe on the streets near the Eiffel Tower. You order a warm coffee and admire the view. A woman walks up to you. She sits down and orders herself something too. She's clearly pretty, but you don't understand in all of the City of Love she would want to sit next to you. 
	"Hello, Creativity Boy" she says.
	"Hello, ma'am"
	"Please call me Jesse"
	"Okay, Jesse, how do you know who I am?"
	"I knew the previous hero and believe I can tell who is the new one."
	"Are you the person whom I am supposed to meet?"
	"Yes, let us begin"
	You walk with her to her house and you spend the next few months learning how to use your mind in combination with your powers to fight evil. You spend time in countless scenarios planning for any possible situtation.
	One day, Jesse calls you and and you walk into her office.
	"I'm putting you through one last simulation and then I'll graduate you"
	Just then, a theif breaks in and snatches the CD and runs away!
	""")		
				time.sleep(20) #tell scenario
				choice=input(name+""", time to make a quick decision!
	Type 1 to call the police
				
	Type 2 to summon Captain Holly Short of the LEP
				
	Type 3 to call the dragon, Saphira""") #ask for option
				if choice=="1":
						print("You call the police but you know the chances of them finding the CD are slim and without it, you can't finish your training. This training you know is essential, and without it, you will die in battle. You have to try again...")
						time.sleep(7)
						paris() #tell them they failed and restart
				elif choice=="2":
						print("You think hard and soon a haze appears outside and you know its Holly shielded. You walk outside and tell her what she needs to do. She flies off, stuns the criminal, and brings the CD back to you with no problems.")
						time.sleep(9) #move on
				elif choice=="3":
						print("You reach out with your mind for the blue dragon. She comes flying in flames roaring. You tell her to chase that theif down and come back. She almost burns him to a crisp, but he lives and Saphira saves the CD")
						time.sleep(9) #move on
				else:
						print("Your input was invalid, try again")
						time.sleep(5)
						paris() #tell them option is incorrect and restart
				if check2=="false":
						os.system('clear') #if hood is not done, do this
						print("""
	"Great job, Creativity Boy"
	"Thank you, Jesse"
	"Let us complete your training"
	You enter the simulation and pass with flying colors. You hop out waiting further instructions.
	"Jesse, where do I go now?"
	"You are heading to Texas to complete the physical part of your training"
	"Yes, ma'am"
	""")
						check1="true" #change variable so hood is different
						time.sleep(20)
						quit=input("Do you want to quit? Type 1 for yes and anything else for no ") #type message and ask if they want to quit
						if quit=="1":
								print(name+", your password is artemis fowl")
								time.sleep(5)
								quit() #tell them the password and quit
						hood() #move on
				elif check2=="true":
						os.system('clear') #if hood is done, do this
						print("""
	"Creativity Boy, you have passed my test"
	"What?"
	"That thief was really hired by me to see if you could handle real world situations and you passed!"
	"But I thought the CD was the real test"
	"That was to make sure your priority was the disk"
	"All right, what do I do now?"
	"You will head to Zelda to discuss strategy"
	"Why? The Xenomorph couldn't have invaded yet"
	"Yes, they have invaded Tokyo"
	"NO! Now there won't be any good Godzilla movies!"
	"Yes, but first you must return so that we may discuss a counterstategy"
	"Time to fight!"
	""")
						quit=(name+", do you want to quit? You need only to type 1 for yes ") #type message and ask if they want to quit
						if quit=="1":
								print(name+", your password is brisingr")
								time.sleep(7)
								quit() #tell them the password and quit
						time.sleep(5)
						zelda() #move on
		def zelda():
				os.system('clear')
				global name #clear screen and get name
				print("""
	"Welcome back, Creativity Boy"
	"Nice to you again too Zelda"
	"I wish we could say we could rest but New York City and Tokyo have been invaded and we must stop them"
	"Agreed"
	"I thought you would say that, and you three options: you could travel with Link three days into the past to stop the mothership, head to New York with the Avengers, or you could head to Tokyo with Dr. Grant"
	"Let me think..."
				""") #tell scenario
				choice=input(name+"""! We need your decision. Where do you want to go?
	Type 1 to go to New York with the World's Mightest Heroes
	
	Type 2 to go to Tokyo with the dinosaur specialist, Dr. Grant
	
	Type 3 to travel back in time with the hero in green
	
	Type 4 to quit
				""") #ask for their choice
				if choice=="1":
						print("You decide to go to New York and a helicarrier carries you there")
						time.sleep(7)
						newyork() #send them to new york
				elif choice=="2":
						print("You think Tokyo will be fun and you fly on a Pterdactyl flies you there")
						time.sleep(7)
						tokyo() #send them to tokyo
				elif choice=="3":
						print("Time travel is always the cool choice and you walk over to Link")
						time.sleep(7)
						mothership() #send them back in time
				elif choice=="4":
						print("Your password is crossroad")
						time.sleep(5)
						quit() #tell them the password and quit
				else:
						print("Your input was invalid, try again")
						time.sleep(5)
						zelda() #tell them the password is invalid and restart
		def newyork():
				os.system('clear')
				global name #clear screen and get name
				print("""
	You arrive in New York and meet Captian America, Thor, Iron Man, Hulk, Hawkeye, and Black Widow
	"Nice to meet you, soldier" Captain says
	"Same to you all" you reply
	"There is no time for this lallygagging, we have an army to fight" Thor says
	"I always love that smell of possible imminent death in the morning" Iron Man Says
	"HULK SMASH PUNY ALIENS!" Hulk said
	Your fight begins and it starts out well but is gets chaotic. You get separated from the others and the Xenomorphs are closing ranks. You need to make a decision now or never.
				""") #tell scenario
				choice=input(name+""", your death is near unless a decision is made!
	Type 1 to call Colonel Fury
	
	Type 2 to bring all the Avengers to you
	
	Type 3 to summon Spider-Man
	
	Type 4 to quit
				""") #ask for choice
				if choice=="1":
						print("You bring in Fury, and he's great at combat, but it seems his skills won't be able to save you this time. You go down fighting with Fury.")
						time.sleep(7)
						newyork() #tell them they died and restart
				elif choice=="2":
						print("All the Avengers come to your aid and the fight seems to be improving, but you are soon overwhelmed and cannot continue")
						time.sleep(7)
						newyork() #tell them they died and restart
				elif choice=="3":
						print("All of a sudden, a red blur swings by and all of the Xenomorph all tangled in webs. You are picked up by this blur and you see it is Spider-Man! ""This is my city!"" he says. You rejoin the fight with this new ally. The battle soon turns and you are victorious!")
						time.sleep(9) #move on
				elif choice=="4":
						print("Your password is shield")
						time.sleep(5)
						quit() #tell them the password and quit
				else:
						print("Your input is invalid, try again")
						time.sleep(5)
						newyork() #tell them the choice is wrong and restart
				os.system('clear') #clear the screen
				print("""
	You return to Zelda and tell her that the mission is a success.
	"Well done, boy"
	"Thank you, but I don't think we're done here, are we?"
	"You would be right in assuming that"
	"What's next, then?
	"You have two options. You can either head to Washington D.C. with Robert Langdon or you can go to Sydney with Indiana Jones"
				""") #print scenario
				choice2=input(name+""", another crossroads is here! Where do you want to go?
	Type 1 to go to Washington D.C. with Langdon, the conspriacy master
	
	Type 2 to go to Sydney, Australia with Indiana Jones, the original adventurer
				""") #ask for their choice
				if choice=="1":
						print("You decide to go to D.C., the capital of the free world. You hop onto a jet and you know you are in for a ride of historical proportions!")
						time.sleep(7)
						dc() #move on
				elif choice=="2":
						print("You decide to head to Sydney, the one place that has an opera house strangely everyone remembers. You take a boat and know soon your adventures will be sung in that same opera house.")
						time.sleep(9)
						sydney() #move on
				else:
						choice2=input("That is not a choice, type 1 for Washington D.C. and 2 for Sydney ") #tell them the choice is invalid and ask again
						if choice=="1":
								print("You decide to go to D.C., the capital of the free world. You hop onto a jet and you know you are in for a ride of historical proportions!")
								time.sleep(7)
								dc() #move on
						elif choice=="2":
								print("You decide to head to Sydney, the one place that has an opera house strangely everyone remembers. You take a boat and know soon your adventures will be sung in that same opera house.")
								time.sleep(9)
								sydney() #move on
						else:
								print("You typed in the wrong answer again.")
								time.sleep(5)
								newyork() #if they screwed up again restart
		def tokyo():
				global name
				os.system('clear') #clear screen and get name
				print("""
	You arrive in Tokyo and meet Dr. Grant
	"Hello, doctor, any dinosaurs native here?"
	"Hello, Creativity Boy, and yes there were"
	Just then Xenomorphs start crowding the streets. You look at a satellite map and see that they are all over the place.
	"Creativity Boy, the only army on this Earth that could hold this city are..."
	"ROOOOAAARRRRRR"
	"Dinosaurs, I know. Let's just say the world's greatest fighting force is back from the dead"
	Out of nowhere, Xenomorph appear and you need to decide which dinosaur to use!
				""") #print scenario
				choice=input(name+"""! You need to select a dinosaur ally!
	Type 1 to summon Godzilla
	
	Type 2 to summon a T-Rex
	
	Type 3 to summon a Triceratops
	
	Type 4 to quit
				""") #ask for their choice
				if choice=="1":
						print("""
	"ROAR!"
	"Creativity Boy, I've never seen that dinsosaur!"
	"I bet you you have, it's Godzilla"
	"What? But that's not a dinosaur!"
	"Apparently he is, I summoned dinosaurs and he came"
	Godzilla starts to do what he does best, defend and all around wreck Tokyo. Xenomorph are killed in droves and none escape. Godzilla rallies the other dinosaurs and run down every one of the Xenomorph. Tokyo is saved.""")
						time.sleep(20) #move on
				elif choice=="2":
						print("A T-Rex appears and starts to attack the Xenomorph. However, he is soon overwhelmed and dies. You know your death is soon to follow")
						time.sleep(7)
						tokyo() #tell them they died and restart
				elif choice=="3":
						print("A Triceratops materializes and starts to graze. It's not the ferocious in the slightest and the Xenomorph kill it quickly. Your death is imminent.")
						time.sleep(7)
						tokyo() #tell them they died and restart
				elif choice=="4":
						print("Your password is jurassic park")
						time.sleep(7)
						quit() #tell them the password and quit
				else:
						print("Your choice was invalid, try again")
						time.sleep(5)
						tokyo() #tell them the choice is invalid and restart
				print("""
	You have saved Tokyo! You return Zelda to tell her the mission was a success!
	"You have done well in the short time we have known you, Creativity Boy"
	"Thank you, but this is far from over, isn't it?"
	"You are correct"
	"Then what is my next mission?"
	"You have two choices: you can go to Washington D.C. with Robert Langdon or you can head to Sydney, Australia with Indiana Jones"
				""") #print scenario
				choice2=input(name+""", time to choose again! What is your path?
	Type 1 to head to D.C. with conspiracy master Prof. Robert Langdon
	
	Type 2 to head to Sydney with the original swashbuckling adventurer, Indiana Jones
				""") #ask for their choice
				if choice2=="1":
						print("You hop on a plane to Washington and you know your in for a ride of historical proportions")
						time.sleep(7)
						dc() #move on
				elif choice2=="2":
						print("You hop on a boat to Sydney. You know, the city with the huge opera house that was in Finding Nemo. This mission, you know, will someday be sung in that opera house")
						time.sleep(7)
						sydney() #move on
				else:
						choice2=input(name+""", your input was invalid. 
	Type 1 for Washington D.C.
	
	Type 2 for Syndey, Australia
						""") #ask again, if not given a valid answer
						if choice2=="1":
								print("You hop on a plane to Washington and you know your in for a ride of historical proportions")
								time.sleep(7)
								dc() #move on
						elif choice2=="2":
								print("You hop on a boat to Sydney. You know, the city with the huge opera house that was in Finding Nemo. This mission, you know, will someday be sung in that opera house")
								time.sleep(7)
								sydney() #move on
						else:
								print("You're doing this on purpose now. We're restarting the area.")
								time.sleep(7)
								tokyo() #restart if continues
		def mothership():
				os.system('clear')
				global name #clear screen and get name
				print("""
	Link waves and doesn't say a word. You know this is normal, he is a silent type. He brings out an instrument called an ocarina. He starts playing a tune that you know does a lot more than sound nice. You feel time being reset and space moved. The three days end and you find yourself in the mothership three days ago.
	You start to head towards the core of the mothership where you will destroy it with the bomb you have been given. Just then, you see two hurt Xenomorphs lying on the floor. "Heal my woes" they say.
				""") #print scenario
				choice=input(name+""", it is time to make a pity decision. What do you want to do?
	Type 1 to ask Link to play the Song of Healing
	
	Type 2 to kill it
	
	Type 3 to interrogate it
	
	Type 4 to quit
				""") #ask for their choice
				if choice=="1":
						print("You ask Link to help this poor thing and Link once again plays a song. This time it is sadder, yet it washes away all your worries. The two Xenomorphs turn into masks. You both know what to do. Each of you put on a mask and turn magicall into Xenomorph. With this disguise, you quickly make it to the center and blow up the ship")
						time.sleep(15) #move on
				elif choice=="2":
						print("You have no mercy for these invaders. You immediately chop off their heads without thought or remorse. Then the Xenomorph cry out with their dying breath. Xenomorph start flowing out of the corridors. You know that your greedy move cost you your life")
						time.sleep(9)
						mothership() #tell them they died and restart
				elif choice=="3":
						print("You decide to press these two for information. You try to make them talk but you get no useful information. Then the Xenomorph surround you and kill you. You know should not have stayed in one place for so long.")
						time.sleep(9)
						mothership() #tell them they died and move on
				elif choice=="4":
						print("Your password is romani ranch")
						time.sleep(7)
						quit() #tell them the password and quit
				else:
						print("That input was invalid, try again")
						time.sleep(7)
						mothership() #if it is invalid, restart
				print("""
	You get out of the ship just as the third day ends. You head back to Zelda to talk about it.
	"Even time travel does not stop you, it seems"
	"Well, a true hero can't let something as simple as time them"
	"True"
	"On to business, what is my next mission?"
	"You can either head to Washington D.C. with Prof. Langdon or go to Sydney with Indiana Jones"
				""") #tell scenario
				choice2=input(name+""", it is a crossroads. Where do you want to go?
	Type 1 to head to Washington D.C. with Professor Langdon
	
	Type 2 to head to Sydney, Australia with Indiana Jones
				""") #ask for their choice
				if choice2=="1":
						print("You fly to D.C. and you know that anything history has got is not going to top this adventure")
						time.sleep(7)
						dc() #move on
				elif choice2=="2":
						print("You sail to Sydney and you know this adventure will be sung one day in its opera house")
						time.sleep(7)
						sydney() #move on
				else:
						choice2=input("""Your input was not a choice, try again.
	Type 1 to go to Washington D.C.
	
	Type 2 to go to Sydney, Australia
	
						""") #tell them the option is invalid and ask again
						if choice2=="1":
								print("You fly to D.C. and you know that anything history has got is not going to top this adventure")
								time.sleep(7)
								dc() #move on
						elif choice2=="2":
								print("You sail to Sydney and you know this adventure will be sung one day in its opera house")
								time.sleep(7)
								sydney() #move on
						else:
								print("You are making too many mistakes. It's time to restart.")
								time.sleep(7)
								mothership() #tell them they failed and move on
		def dc():
				os.system('clear')
				global name #clear screen and get name
				print("""
	You arrive in the middle of Washington D.C., the capital of the free world. You meet Robert Langdon, treasure hunter extraordinare and conspircacy theorist.
	"Hello, Professor, nice city to be fighting in today, eh?"
	"I wish we weren't doing it here, too much history to be lost"
	"Yeah but that history could help us"
	"Yeah I guess, if you wanted to revive people from the dead"
	"Anyhow, it is time to defend the Earth from the Xenomorph, how is our position?"
	"We got the White House and Smithsonian, but the Xenomorph and have taken the Congress building"
	You take up positions at the Smithsonian and the Xenomorph start to come in waves. You fight them off but there is far too many. You need an army, not a professor and a bunch of old stuff.
				""") #tell scenario
				time.sleep(20)
				choice=input(name+""", time to use your surroundings to your advantage!
Type 1 to revive the Presidents to life

Type 2 to summon the tablet of Akmun-Ra to bring the museum to life

Type 3 to retreat

Type 4 to quit
				""") #ask for their choice
				if choice=="1":
						print("Presidents start to rise from the ground. They try to join the fight, but most of them were political leaders, not military. They would be good to lead the battle, not fight it. Even with the reinforcements, you fall. This, you know, will soon include the world")
						time.sleep(9)
						dc() #tell them they died and restart
				elif choice=="2":
						print("The tablet appears and you also call the artifacts from New York, too. Everyone awakens and you rally them. You tell them to defend their city, their museum, their country, and their world. They push back the Xenomorph and take back over Congress and the Xenomorph retreat.")
						time.sleep(9) #move on
				elif choice=="3":
						print("You retreat back to the White House. The Xenomorph quickly take over the Smithsonian and soon they are at the front gates of the White House. This may be the most secure building in the world, but it could stand only so long before an alien invasion. You know it is only a matter of time before you surrender and then they will execute you.")
						time.sleep(9)
						dc() #tell them they died and restart
				elif choice=="4":
						print("Your password is magic")
						time.sleep(7)
						quit() #tell them the password and quit
				else:
						print("Your input was invalid, try again.")
						time.sleep(5)
						dc() #restart if option is invalid
				print("""
You return to headquarters to Zelda, confident. You have delt a terrible blow and the war's end is near.
"You saved that city fast."
"I had some help from some OLD friends"
"Creativity Boy, it is time for the final battle."
"Where?"
"Here"
"Why?"
"They are at our front doors, if not for my magic, we would not be able to leave. Besides, this is where our and therefore, your magic is strongest. However if we fall, the world is doomed"
"Let's do this"
				""") #print story
				time.sleep(20)
				endgame() #move on
		def sydney():
				global name
				os.system('clear') #clear screen and get name
				print("""
You arrive in Sydney with Indiana Jones.
"Hello, Indy"
"Hello, Boy"
"I see your hand is hovering over your famous whip"
"This is a dangerous city at the moment"
"How are we doing here?"
"We have the land, but the Xenomorph have the sea. We are surrounded."
"So, a challenge, then. This is going to be fun"
You start defending the land. It gets pretty hard, because not only do you have to stop the Xenomorph trying to climb onto land, but you are getting fired at by the boats. You can keep them from the land, but you need someone to take care of the sea.
				""") #tell scenario
				choice=input(name+""", who will be your aquatic friend?
Type 1 to summon Aquaman

Type 2 to summon the cast of Finding Nemo

Type 3 to summon all the Pokemon

Type 4 to quit
				""") #ask for their choice
				if choice=="1":
						print("You bring Aquaman. He may be useless on land, but in water, he's useful, right? He does well at first, but all can really do is summon fish and you could do that yourself. In the end, all you can do is prevent the inevitable by keeping the Xenomorph off the land.")
						time.sleep(9)
						sydney() #tell them they died and restart
				elif choice=="2":
						print("Everyone from Finding Nemo comes in. They are fish, so they are at home in the sea. They rock the boats and all around cause choas. However, there is only so much fish can do against an alien race. They keep fighting the good fight but are soo overwhelmed.")
						time.sleep(9)
						sydney() #tell them they died and restart
				elif choice=="3":
						print("All 718 Pokemon come in and start to fight. The ones that can Mega Evolve do and it is a big help. The ones that can fly and swim take the boats and the rest help you out. This tag team helps and the boats are sinking rapidly. Soon, the boats are sunk before Xenomorph can attack")
						time.sleep(9) #move on
				elif choice=="4":
						print("Your password is crystal skull")
						time.sleep(7)
						quit() #tell them password and move on
				else:
						print("Your input was invalid, try again")
						time.sleep(5)
						sydney() #tell them it is invalid and restart
				print("""
	You return to Zelda for the debriefing of the mission. In other words, you are there to brag about it and talk about it in a boasting way.
	"Well done, boy"
	"Thank you"
	"I believe it is time for the final battle"
	"OK, where?"
	"Here"
	"Why here?"
	"The Xenomorph have surrounded us here. If not for my magic, you would not have been able to even get in here. Besides, this place is where ours, and therefore, your magic is strongest. It is best that the final battle is here."
	"Then let us fight as allies"
				""") #print story 
				time.sleep(25)
				endgame() #move on
		def endgame():
				os.system('clear')
				global name #clear screen and get name
				print("""
	"How should we prepare?" you ask
	"I shall teach you a new technique. As the hero, you can get energy from the creativity that already exists in the world"
	"Huh?"
	"People already have creative thoughts and ideas. You can harness this as energy and use it for your own methods."
	"That is so cool!"
	"Try it and summon us an army!"
	You do so and it is like a convention with the real people. Everyone from Eragon to Buzz Lightyear, from Mario to Shrek, from Harry Potter to Sonic the Hedgehog is here to fight. To defend the Earth from the Xenomorph. The final battle has come. Months of training has paid off, you are ready. You rally the armies of Creativity and open the doors ready to give any Xenomorph a piece of you!
				""") #tell scenario
				choice=input(name+"""! Time to fight! Who do you want to take the front?
Type 1 to send Mario to the front

Type 2 to send Shrek

Type 3 to send Harry Potter

Type 4 to quit
				""") #ask for their choice
				if choice=="1" or choice=="2" or choice=="3":
						print("The fight gets futile. Even with the new technique, you don't have enough power!")
						time.sleep(7) #move on
				elif choice=="4":
						print("Your password is princess zelda")
						time.sleep(7)
						quit() #tell them the password and quit
				else:
						print("Your choice is invalid, try again")
						time.sleep(7)
						endgame() #tell them the option is invalid and restart		
				os.system('clear')
				print("""
"I have an idea!" a man called Prof. E Gadd yells
"What is it?"
"Follow me to the back room!"
You follow him there.
"What is the plan?"
"This broadcasting equipment will allow you to speak with every person on Earth, even if they don't have a TV! You will speak to them rallying them to new ideas and therefore, giving you new power"
He turns on the equipment and you get ready.
"Hello," you say, "I am Creativity Boy. You likely don't know me, but I was once like you a boy with great ideas but no way to share them. However, I was given the chance to make a difference and now, by helping me, so can you! People of Earth, forget your quarrels. Today, there is no such things as an American, a Russian, a Chinese, a French, only an Earthling. Today, we face a threat known as the Xenomorph, an alien race bent on killing our race. My army of your ideas are currently locked in battle against the Xenomorph. But, I, and they, need help. You, the average person, is more than average. Your ideas can change the world, your creativty can make this world better. So get thinking, world, because if our minds can't save our world, nothing can"
E Gadd shuts off the equipment.
"It is done"
"How do you feel?"
"Not all tha... Hold on I feel it. The people have risen from their slumber! I have power, I have ideas! Let us return!"
				""") #tell scenario
				realchoice=input(name+"""! Time for the real final battle!
Type 1 to fight the Xenomorph head on

Type 2 to flank them

Type 3 to trick them
			""") #ask for their choice
				if realchoice=="1":
						print("You jump into the fray without thought. These people attacked your home and now it is time to repay them. Your newfound power allows you to push them back. However, there is too many, soon your are pushed back and your army falls. You know you should have strategy instead of brawn.")
						time.sleep(13)
						endgame() #tell them they died and restart
				elif realchoice=="2":
						print("You send part of your army to attack head on but take a section to flank them on the right. This will force them to face you or get slaughtered. This will allow the main force to run them down. You set the plan in motion and it goes smoothly. No Xenomorph survives.")
						time.sleep(13) #move on
				elif realchoice=="3":
						print("You try to trick the Xenomorph but are unable to and the fight starts to turn against. Their cunning is too strong. Instead of calculating, you knew you needed to be creative. This battle was lost and so is the world")
						time.sleep(13)
						endgame() #tell them they died and restart
				else:
						realchoice=input("""That input was invalid, try again.
Type 1 to fight them head on

Type 2 to flank them

Type 3 to trick them
					""") #if the choice is invalid, ask them again
						if realchoice=="1":
								print("You jump into the fray without thought. These people attacked your home and now it is time to repay them. Your newfound power allows you to push them back. However, there is too many, soon your are pushed back and your army falls. You know you should have strategy instead of brawn.")
								time.sleep(13)
								endgame() #tell them they died and restart
						elif realchoice=="2":
								print("You send part of your army to attack head on but take a section to flank them on the right. This will force them to face you or get slaughtered. This will allow the main force to run them down. You set the plan in motion and it goes smoothly. No Xenomorph survives.")
								time.sleep(13) #move on
						elif realchoice=="3":
								print("You try to trick the Xenomorph but are unable to and the fight starts to turn against. Their cunning is too strong. Instead of calculating, you knew you needed to be creative. This battle was lost and so is the world")
								time.sleep(11)
								endgame() #tell them they died and restart
						else:
								print("You made too many mistakes. Starting over...")
								time.sleep(7)
								endgame() #tell them they keep making mistakes and restart
				print("""
"Creativity Boy, you did it!" Zelda cried
"I guess I did"
"The world and us will be forever in your debt"
"Come on, I just provided the leadership, you guys actually did all the work"
"All the same, the world will not soon forget what you did here"
"What do we do now?"
"I will send you back to Earth. You will still have your powers. Your job will be to keep an eye out, and when the next apocalypse happens, you and us will be there."
"Then I guess it is time to say good-bye until the next disaster"
"Until then, Creativity Boy
"I'll be waiting, Princess Zelda"
She sends you home. You sometimes wonder if it was all a dream, but you know that if the world ever needs another hero, you will be waiting in the wings. This is where we part ways. May we meet again in another time and place...""")
				time.sleep(25)
				credits() #move on
		def credits():
				os.system('clear') #clear screen
				print("""
Storyboard..........................................................Matteo James
Coding..............................................................Matteo James
Editing and Debug...................................................Matteo James, Zane James, and Mr. Davis
Marketing...........................................................Matteo James
This game was coded in Python, Matteo's preferred software provider
This game was programmed on an ASUS tablet, Matteo's preferred hardware provider
Special Thanks to:
Stephen A. James for naming the Xenomorph
Zane M. James for testing
Mr. H. Davis for instruction
Chaparral Star Academy for providing materials
Creativity Boy, the general, Jesse, and the story are hereby declared property of Matteo James
All other characters, ideas, and icons belong to their respective owners
This game is based off fictional characters. Any similarites between anything owned by me as above stated and any other game, movie, book, etc., is purely coincidental
Copyright 2015
Thank You So Much For Playing! Use the password creativity boy next time you play this game!
				""") #print the credits
				time.sleep(25)
				quit() #quit
		def greeting():
				print("Welcome! You have just started a choose your own path game. This is going to be so much fun! Solve this code for help: uzqf phsft bsf mjlf pojpot. If you have a code from a previous game, type code")
				name=input("But first, what is your name? ") #print the hello message and ask for their names
				name=name.title()
				if name=="Miyamoto":
						print("How are you even understanding this? This game is in English!")
						time.sleep(7)
						global name
						greeting() #give an easter egg and move on
				elif name=="Captain Falcon":
						print("You Falcon Punch your way through the entire game and get to the end!")
						time.sleep(7)
						global name
						endgame() #give an easter egg and move on to the final area
				elif name=="Code":
						code() #send them to the password system
				elif name=="Strong Bad":
						print("But you can't get ye flask!")
						time.sleep(7)
						global name
						beginning() #give an easter egg and move on
				elif name=="East":
						print("East? I thought you said weast!")
						time.sleep(7)
						global name
						greeting()	#give an easter egg and move on	
				elif name=="Ogres Are Like Onions":
						print("You have solved the code and opened the help!")
						choice=input("Do you want a walkthrough or the list of passwords? Type 1 for walkthrough and 2 for passwords") #ask if they want the walkthrough or the passwords
						if choice=="1":
								infile=open('/storage/sdcard0/Download/walkthrough.txt','r')
								walkthrough=infile.read()
								print(walkthrough)
								infile.close() #open, print, and close the walkthrough
								x=input(" ")
								if x=="continue":
										greeting()
								else:
										print("We're just starting you over anyway.")
										time.sleep(5)
										greeting() #move them on regardless
						elif choice=="2":
								infile=open('/storage/sdcard0/Download/password.txt','r')
								password=infile.read()
								print(password)
								infile.close() #open, close, and print the passwords
								x=input(" ")
								if x=="continue":
										greeting()
								else:
										print("We're just starting you over anyway.")
										time.sleep(5)
										greeting() #move them forward
				else:
						print("It is really nice to meet you, "+name)
						global name
						print(name+", it's time to start this grand adventure...")
						time.sleep(5)
						os.system('clear')
						beginning() #print their name, global their name, and clear the screen, and move on
		def code():
				os.system('clear') #clear screen
				global check1
				global check2 #get the two variables so it can change the levels and send it to the correct level
				print("""
	Welcome to the choose your own path adventure game, Creativity Boy. This game has no save system, but rather a password system.""")
				password=input("Put in the password that was given to you when you quit the game. If you do have one, type it in lowercase EXACTLY as you saw it. If you don't, type nothing ") #ask for their password
				password=password.title() #title the password
				if password=="Thunder":
						name=input("First, what is your name? ")
						name=name.title()
						global name 
						beginning() #ask for their name and move on
				elif password=="Xenomorph":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						story() #ask for their name and move on
				elif password=="Barrel Roll":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						check1=="true"
						hood() #ask for their name, change the variable, and move on
				elif password=="Death Star":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						hood() #ask for their name and move on
				elif password=="Artemis Fowl":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						paris() #ask for their name and move on
				elif password=="Brisingr":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						check2=="true"
						paris() #ask for their name, change the variable, and move on
				elif password=="Crossroad":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						zelda() #ask for their name and move on
				elif password=="Shield":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						newyork() #ask for their anme and move on
				elif password=="Jurassic Park":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						tokyo() #ask for their name and move on
				elif password=="Romani Ranch":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						mothership() #ask for their name and move on
				elif password=="Magic":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						dc() #ask for their name and move on
				elif password=="Crystal Skull":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						sydney() #ask for their name and move on
				elif password=="Princess Zelda":
						name=input("First, what is your name? ")
						name=name.title()
						global name
						endgame() #ask for their name and move on
				elif password=="Creativity Boy":
						name=input("First, what is your name? ")
						name=name.title()
						global name #ask for their name
						level=input(name+""", which level do you want to do?
Type 1 to go to the beginning

Type 2 to go to the meeting

Type 3 to go to Hood with Paris not done

Type 4 to go to Hood with Paris done

Type 5 to go to Paris with Hood not done

Type 6 to go to Paris with Hood done

Type 7 to go to the strategy meeting

Type 8 to go to New York

Type 9 to go to Tokyo

Type 10 to go to the mothership

Type 11 to go to Washington D.C.

Type 12 to go to Sydney

Type 13 to go to the end

Type 14 to go to the credits
						""") #ask which level they want to go to
						if level=="1":
								beginning()
						elif level=="2":
								story()
						elif level=="3":
								hood()
						elif level=="4":
								check1="true"
								hood()
						elif level=="5":
								paris()
						elif level=="6":
								check2="true"
								paris()
						elif level=="7":
								zelda()
						elif level=="8":
								newyork()
						elif level=="9":
								tokyo()
						elif level=="10":
								mothership()
						elif level=="11":
								dc()
						elif level=="12":
								sydney()
						elif level=="13":
								endgame()
						elif level=="14":
								credits() #direct them to the correct level
						else:
								print("That was not a choice, we are restarting")
								time.sleep(7)
								code() #restart the level
				elif password=="Nothing":
						print("All right")
						time.sleep(5)
						greeting() #move them back to the greeting
				else:
						print("That is not a password, try again")
						time.sleep(7)
						code() #tell them that is not a password and restart
		greeting()
main() #do everything