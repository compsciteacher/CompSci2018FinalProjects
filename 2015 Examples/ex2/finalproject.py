import os,time,random
os.system("clear")

def greeting():
    print("Hello!!")
    name=input("What is your name? ")       #Greeting function
    name=name.title()
    print("Hi "+name+"!")
    global name

greeting()

def race():
    print('''
The classes are:
    
=====================================================
Human - special ability - Agile, Sneaky
-----------------------------------------------------
Brute - special ability - Strong, Scary
-----------------------------------------------------      
Bandito - special ability - Manipulator, Pickpocket
-----------------------------------------------------
Plebian - special ability - Average guy, Normal
=====================================================
 ''')
    
    
    pick=input("what class would you like too play? ")
    pick=pick.title()
    races=open("/storage/sdcard0/Download/finalproject1.txt", "r")     #asks and checks a class
    list1=races.readlines() 
    list1=[item.strip() for item in list1]
    player=open("/storage/sdcard0/Download/finalprojectplayer.txt", "w")
    if pick in list1:
        player.write(pick + '\n')
    else:
        print("That is not in the class list!  (be sure to spell correctly!)")
        time.sleep(1)
        os.system("clear")
        race()
    global player, pick
    time.sleep(1)
    os.system("clear")
  
     
def checking():   
    if pick=="Human":
       print("You picked Human! Hi, "+name+"!")
       print("What starting weapon would you like to choose?")
       fweapon=input("Your options are: Chopping axe(1) or Wooden baseball bat(2) ")   #asks for a starting weapon
       if fweapon=="1":
           player.write("Chopping axe"+ '\n')
       elif fweapon=='2':
           player.write("Wooden baseball bat"+ '\n')
       else:
           print("That is not a option!")
           time.sleep(1)
           os.system("clear")
           checking()

    elif pick=="Brute":
       print("You picked Brute! Hi, "+name+"!")
       print("What starting weapon would you like to choose?")
       fweapon=input("Your options are: Sledgehammer(1) or Rock(2) ")      #asks for a starting weapon
       if fweapon=="1":
           player.write("Sledgehammer"+ '\n')
       elif fweapon=='2':
           player.write("Rock"+ '\n')
       else:
           print("That is not a option!")
           time.sleep(1)
           os.system("clear")
           checking()


    elif pick=="Bandito":
       print("You picked Bandito! Hi, "+name+"!")
       print("What starting weapon would you like to choose?")
       fweapon=input("Your options are: Switchblade(1) or Spikey gloves(2) ")    #asks for a starting weapon
       if fweapon=="1":
           player.write("Switchblade"+ '\n')
       elif fweapon=='2':
           player.write("spikey gloves"+ '\n')
       else:
           print("That is not a option!")
           time.sleep(1)
           os.system("clear")
           checking()

    
    elif pick=="Plebian":
       print("You picked Plebian! Hi, "+name+"!")
       print("What starting weapon would you like to choose?")
       fweapon=input("Your options are: Fists(1) or Fists(2) ")          #asks for a starting weapon
       
       if fweapon=="1":
           player.write("Fists"+ '\n')
       elif fweapon=='2':
           player.write("Fists"+ '\n')
       else:
           print("That is not a option!")
           time.sleep(1)
           os.system("clear")
           checking()

    elif pick=="Can Of Baked Beans":
        print("You are a can of baked beans...")
        time.sleep(2)
        quit()
     
  

race()
checking()

def story():
    

    os.system("clear")
    print('''You were a farmer until one day the evil Spartals came to your farm to collect taxes. You grabbed the nearest weapon, and fended off the Spartals because you had enough of their repressive ways!
''')
    print("You swear to destroy the evil regime and bring justice to the land!!")
    print("And with that you set off to destroy down the evil king, Turtus.")
    time.sleep(10)
    os.system("clear")

#story()

def first():
    town=input("Would you like to go to the city(1), or to the small town(2)?")       #asks to go to the city or town
    if town=="1":
        print("You decided to go towards the city.")
    elif town=="2":
        print("You decided to go towards the town.")
    else:
        print("That is not an option")
        time.sleep(2)
        os.system('clear')
        first()
    global town
    time.sleep(2)
    os.system("clear")    
first()

            


num11=100           
           
def third(): 																																	#random function for enemy attacking
    enemy=random.choice(open("/storage/sdcard0/Download/finalenemys.txt").readlines())
    
    enemy=enemy.strip("\n")
    random1=random.randrange(1,3)
    if random1==1:
        print("You were attacked by a "+ enemy+"!")
        global enemy
       
        print("What would you like to do?")
        action=input("Attack (1), or run(2): ")
        global action
        
        enemyhealth=75
        num11=int(num11)

        if action=="1":
            while enemyhealth>=0:
                enemyattack=random.randrange(1,9)
                playerattack=random.randrange(1,26)
                print("You attacked for",playerattack,"damage")
                enemyhealth=(enemyhealth-playerattack)
                time.sleep(2)
                print("The",enemy,"attacked you for",enemyattack,"damage !")
                num11=(num11-enemyattack)
                time.sleep(2)
                if num11<=0:
                    print("You died")
                    quit()
                time.sleep(1)
                os.system("clear")
             
                print(num11,"is your remaining health.")
             
            time.sleep(1)
            os.system("clear")
            print("You killed the "+enemy+"!")
            print(num11,"is your remaining health.")
            
        elif action=="2":
            print("You ran away!")
        else:
            print("Thats not an option!")
            third()
        
        global num11
    
    
    if random1==2:
        return  
    
    
        
                
third()
time.sleep(1)

third()
global num11
def fourth():                  #asks to heal or move on, also random attack
    time.sleep(2)
    os.system("clear")
    enemyhealth=(120)
    if town=="1":
        print("You made it to the city!")
        num12=input("Would like to heal(1), or move on towards the Spartal outpost Beta(2): ")
      
    elif town=="2":
        print("You made it to the town!")      
        num12=input("Would like to heal(1), or move on towards the Spartal outpost Beta(2): ")
      
    else:
        print("Thats not an option!")
        time.sleep(1)
        fourth()
        
    global num12
        
    if num12=="1":
        global num12
        print("You go to the local doctor and regained all your health! You also received a strength boost from the doctor.")
        num11=(100)
        time.sleep(2)
        os.system("clear")
        global num11
     
        print("You start going towards the Spartal outpost Beta.")
        num13=random.randrange(1,3)
        if num13==1:
            print("On you way to the outpost, you were ambushed by a group of spartal hitmen sent by King Turtus!")
            time.sleep(5)
            while enemyhealth>=0:
                enemyattack=random.randrange(1,11)
                playerattack=random.randrange(1,51)
                print("You attacked for",playerattack,"damage")
                enemyhealth=(enemyhealth-playerattack)
                time.sleep(2)
                print("The spartals attacked you for",enemyattack,"damage !")
                num11=(num11-enemyattack)
                time.sleep(2)
                if num11<=0:
                    print("You died")
                    quit()
                time.sleep(1)
                os.system("clear")
             
                print(num11,"is your remaining health.")
                global num11
             
            print("You killed the Spartals!")
            time.sleep(2)
            os.system("clear")
       
        if num13==2:
            print("You made it to the outpost without being attacked.")       
            time.sleep(3)
   
   
   
   
   
   
    elif num12=='2':   
       
        print("You start going towards the Spartal outpost Beta.")
        num13=random.randrange(1,3)
        if num13==1:
            print("On you way to the outpost, you were ambushed by a group of spartal hitmen sent by King Turtus!")
            time.sleep(5)
            while enemyhealth>=0:
                enemyattack=random.randrange(1,11)
                playerattack=random.randrange(1,51)
                print("You attacked for",playerattack,"damage")
                enemyhealth=(enemyhealth-playerattack)
                time.sleep(2)
                print("The spartals attacked you for",enemyattack,"damage !")
                num11=(num11-enemyattack)
                time.sleep(2)
                if num11<=0:
                    print("You died")
                    quit()
                time.sleep(1)
                os.system("clear")
             
                print(num11,"is your remaining health.")
                global num11
             
            print("You killed the Spartals!")
            time.sleep(2)
            os.system("clear")
       
        if num13==2:
            print("You made it to the outpost without being attacked.")       
            time.sleep(3)
     
    else:
        print("That is not an option!")
        fourth()   

fourth()

def sixth():  #boss battle with more health
    
    num18=(150)
    enemyhealth=(200)
    print("You made it to King Turtus's evil lair!")
    time.sleep(2)
    while enemyhealth>=0:
        enemyattack=random.randrange(1,16)
        playerattack=random.randrange(1,51)
        print("You attacked for",playerattack,"damage")
        enemyhealth=(enemyhealth-playerattack)
        time.sleep(2)
        print("King Turtus attacked you for",enemyattack,"damage !")
        num18=(num18-enemyattack)
        time.sleep(2)
        if num18<=0:
            print("You died")
            time.sleep(1)
            quit()    
       
        os.system("clear")
             
        print(num18,"is your remaining health.")
             
                
    time.sleep(2)
    print("You defeated the evil King Turtus and brought justice to the land!!!!")
    time.sleep(4)
    print("YOU WIN!!!!!!!")
    time.sleep(2)
    quit()
                
            
def seventh():           #boss battle with more damage
    global num11
    enemyhealth=(200)
    print("You made it to King Turtus's evil lair!")
    time.sleep(2)
    os.system("clear")
    while enemyhealth>=0:
        enemyattack=random.randrange(1,16)
        playerattack=random.randrange(25,51)
        print("You attacked for",playerattack,"damage")
        enemyhealth=(enemyhealth-playerattack)
        time.sleep(2)
        print("King Turtus attacked you for",enemyattack,"damage !")
        num11=(num11-enemyattack)
        time.sleep(2)
        
        os.system("clear")
             
        print(num11,"is your remaining health.")     
        if num11<=0:
            print("You died")
            time.sleep(1)
            quit()
                
    time.sleep(2)
    print("You defeated the evil King Turtus and brought justice to the land!!!!")
    time.sleep(4)
    print("YOU WIN!!!!!!!")
    time.sleep(2)
    quit()
            





def fifth():                    #attacking function, asks to steath or loud random chance
    global num11 
    enemyhealth=(175)
    random3=random.randrange(1,7)
   
    sf=input("would you like to attempt stealth(1), or go loud(2): ")
    time.sleep(2)
    os.system('clear')
    if sf=='1':
        print("You are attemptng stealth.")
        if random3<=2:
            print("You were able to quietly retrieve the location of Turtus!")
            
        else:
            print("You were spotted! You must fight the remaining Spartals!")
            while enemyhealth>0:
                enemyattack=random.randrange(1,16)
                playerattack=random.randrange(1,51)
                print("You attacked for",playerattack,"damage")
                enemyhealth=(enemyhealth-playerattack)
                time.sleep(2)
                print("The spartals attacked you for",enemyattack,"damage !")
                num11=(num11-enemyattack)
                time.sleep(2)
                if num11<=0:
                    print("You died")
                    quit()
                time.sleep(1)
                os.system("clear")
             
                print(num11,"is your remaining health.")
             
    
    elif sf=='2':
        print("Youre going in loud!")
        time.sleep(2)    
        while enemyhealth>0:
            enemyattack=random.randrange(1,16)
            playerattack=random.randrange(1,51)
            print("You attacked for",playerattack,"damage")
            enemyhealth=(enemyhealth-playerattack)
            time.sleep(2)
            print("The spartals attacked you for",enemyattack,"damage !")
            num11=(num11-enemyattack)
            time.sleep(2)
            if num11<=0:
                print("You died")
                quit()
            time.sleep(1)
            os.system("clear")
             
            print(num11,"is your remaining health.")
             
        print("You retrieved the location of Turtus!")
        print("You killed the Spartals!")
    else:
        print("That is not an option!")
        time.sleep(2)
        fifth()
               
    time.sleep(1)
    os.system("clear")
    global num11
def ten():                     #function that asks to improve health or improve damage
    
    print(num11,"is your remaining health.")
    wh=input("would you like to regain and increase all you health(1), or improve damage by taking a special spartal sword(2): ")
    random4=random.randrange(1,3)
    if wh=="1":
     
        global num11
        print("You regained your health, and increased your health by 50%!")
        time.sleep(2)
        sixth()
                
    
   
    
    elif wh=="2":
        print("You took the Special Spartal Sword! You have a higher chance of striking with more power!")
        time.sleep(2)
        seventh()
    else:
        print("Thats not an option!")
        time.sleep(2)
        ten()      
    
        
    

fifth()
global num11
ten()
os.system("clear")

