import os
os.system('clear') 
import string, time 

def intro(): 
    welcome="Welcome to the Box Office Predictor!"
    program="This program will predict the box office for any film of your choice!\n" 
    print("" + welcome.center(125) + "")
    print("" + program.center(125) + "") 
    
    exp1="So this is how it works:" 
    print("" + exp1.center(125) + "") 
    exp2="There are 5 things that you need to know about a movie to predict the box office...\n"
    print("" + exp2.center(125) + "") 
    
    print("--------------------------------------------------------------------------------------------------------------------------------\n")
    
    rating='''
1. Rating- This uses the rating for a film (from Rotten Tomatoes) between 1-100. The reason its used in the equation is simple, the higher the rating, the more money its making.\n'''
    print(rating) 
    
    budget='''
2. Budget- This is the listed production budget in millions of dollars. This does not include the marketing budget for a film, which should have a direct impact on the box office.\n'''
    print(budget) 
    
    theater='''
3. Theater- This is the theater count at widest release. The reason its used is also super simple, The wider the release, the greater accessibility to the audience, both in terms of geography and available showtimes.\n'''
    print(theater)
    
    sequel='''
4. Sequel- This is a binary variable (meaning it is either 0 or 1) that indicates whether or not the film is a sequel. Because sequels are normally the continuation of a previously successful film, they have an advantage in the box office.\n''' 
    print(sequel) 
    
    pg13='''
5. PG13- This is another binary variable that indicates whether or not the film is rated PG-13. There is no age limit on who can see the film but the rating also attracts the attention of the older audience.\n'''
    print(pg13) 
    
    print("--------------------------------------------------------------------------------------------------------------------------------\n") 
    time.sleep(5) 
intro() 


moviefile=open('/storage/sdcard0/Download/moviedb.txt','r',)  
file=moviefile.readlines() 
global file 
 
def entry():    
    movielist=[] 
    print('\nWhat movie would you like to find the box office for?\nYour options are:\n')   
    for info in file:
        info=info.split(';')        #Entering movie 
        title=info[0]
        movielist.append(title) 
        print('-'+title+'\n')          
    movie=input('Movie: ') 
    movie=movie.title()
    global movie   
    if movie in movielist: 
        print('''
The formula that will be used to predict the box office is:  

               -80 + 0.6(rating) + 0.5(budget) + 0.025(theater) + 50(sequel) + 20(PG-13)''')  #equation 
        calc()  
    elif movie not in movielist: 
        print('Movie not found. Please try again.\n')  
        entry() 
            
def calc(): 
        
    def rt():    #rating calculation 
        for lines in file: 
            lines=lines.split(';') 
            if lines[0]==movie: 
                oldrt=lines[1] 
                oldrt=int(oldrt) 
                newrt=(oldrt*0.6)  
        print('\nStep 1- Find the rating of the film which in this case is: %i\n Then multiply it by 0.6 which gives you %i\n'%(oldrt,newrt)) 
        return newrt
   
        
    def bgt():      #production budget calculation 
        for lines in file: 
            lines=lines.split(';') 
            if lines[0]==movie: 
                oldbgt=lines[2]
                oldbgt=int(oldbgt) 
                newbgt=(oldbgt*0.5) 
        print('Step 2- Find the production budget of the film (in millions) which in this case is: $%i\n Then multiply it by 0.5 which gives you %i\n'%(oldbgt,newbgt)) 
        return newbgt
    
            
    def thtr():        #theater count calculation 
        for lines in file: 
            lines=lines.split(';') 
            if lines[0]==movie: 
                oldthtr=lines[3] 
                oldthtr=int(oldthtr) 
                newthtr=(oldthtr*0.025) 
        print('Step 3- Find the theater count at the widest release for the film which in this case is: %i theaters\n Then multiply it by 0.025 which gives you %i\n'%(oldthtr,newthtr)) 
        return newthtr
     
        
    def sequel():      #sequel calculation 
        for lines in file:
            lines=lines.split(';') 
            if lines[0]==movie: 
                if lines[4]=='sequel': 
                    sequel=50
                    print("Step 4- Determine if the film is a sequel or not. Since this is a binary variable it works a little bit differently. If it is a sequel then it equals to 1. If it is not a sequel then it equals to 0. After determining if it is or isn't a sequel, you multiply it by 50 so you automatically get either 50 or 0 depending on whether it is or isn't a sequel. In this case it is a sequel so sequel=50.\n") 
                else: 
                    sequel=0
                    print("Step 4- Determine if the film is a sequel or not. Since this is a binary variable it works a little bit differently. If it is a sequel then it equals to 1. If it is not a sequel then it equals to 0. After determining if it is or isn't a sequel, you multiply it by 50 so you automatically get either 50 or 0 depending on whether it is or isn't a sequel. In this case it is not a sequel so sequel=0.\n")
        return sequel
    
      
    def pg13():         #pg13 calculation 
        for lines in file: 
            lines=lines.split(';') 
            if lines[0]==movie: 
                if lines[5]=='pg13': 
                    pg13=20
                    print('Step 5- Determine if the film is PG-13. This is another binary variable. But this time you multiply by 20 so it is automatically either 20 or 0 depending on whether the film is PG-13 or not. In this case it is PG-13 so PG-13=20\n') 
                else: 
                    pg13=0
                    print('Step 5- Determine if the film is PG-13. This is another binary variable. Instead this time you multiply by 20 so it is automatically either 20 or 0 depending on whether the film is PG-13 or not. In this case it is not PG-13 so PG-13=0\n') 
        return pg13 
    
        
    def pbo():       #predicted box office calculation 
        for lines in file: 
            lines=lines.split(';') 
            if lines[0]==movie: 
                rbo=lines[6] 
                rbo=int(rbo) 
        total=(rt()+bgt()+thtr()+sequel()+pg13()) 
        pbo=(total-80)  
        x='The Hunger Games Mockingjay Part 1' 
        if movie==x: 
            print('''Step 6- Now the last step is to add them all together and subtract the total by 80. So after doing the calculations the results for %s is: 
                
Predicted Box Office: $%i
Real Box Office: $%i Million'''%(movie,total,rbo)) 

        elif movie!=x: 
            print('''Step 6- Now the last step is to add them all together and subtract the total by 80. So after doing the calculations the results for %s is: 

Predicted Box Office: $%i Million 
Real Box Office: $%i Million '''%(movie,pbo,rbo))  
        time.sleep(5) 
    pbo()  
    
    def tryagain():      #if they want to try again 
        retry=input('\nWould you like to try another movie? ') 
        retry=retry.title() 
        if retry=='Yes': 
            entry() 
        elif retry=='No': 
            print('\nThank you for using this program! Have a nice day!') 
            quit() 
        else: 
            print('\nPlease enter yes or no.') 
            tryagain()                                
    tryagain() 
    
entry()  
              