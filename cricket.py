print("\n >>>>>>>>>------ BOOK CRICKET------>>>>>>>>>\n")
print(""" 
 
Instructions:
 
1. You have to select any random number from 1 to 6.
2. The computer will also select a number.
3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
   If the number selected by you and computer is same, then you will lose your wicket.
4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
   If the number selected by you and computer is same, then the computer will lose its wicket.
5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.
6. The innings will end after either the three wickets fell or the overs end.
7. The player with maximum runs wins. """)
 
print("\n---------- Start Game ----------")
 
import random
rand_o=random.randint(1,2)
rand_toss=random.randint(1,2)




print("""\nWe all have played that book cricket game in our childhood. This game works just like that. Play it and relive your childhood.
      """)
#start
a=input("\n \nPress 's' to start this game\n").lower()


#toss and team declaration
  
if 's' in a:
    u=" "
    c=" "
    u=input("\nEnter the name of your team : \n").upper()
    u_batsman1=input("Enter the name of batsman 1 : \n").upper()
    u_batsman2=input("Enter the name of batsman 2 : \n").upper()           
    u_bowler1=input("Enter the name of bowler 1 : \n").upper()
    u_bowler2=input("Enter the name of bowler 2 : \n").upper()
    
    

    c="WORLD XI" 
    print(f"\nYour team is {u} and computer is playing with team {c} \n ")      
    print(f"\n>Your team have {u_batsman1} and {u_batsman2} as Batsman , {u_bowler1} and {u_bowler2} as Bowlers\n")

    c_batsman1=(random.choice(('Steve Waugh','Virendra Sehwag','Sachin Tendulkar'))).upper()
    c_batsman2=(random.choice(("Ricky Ponting","Ms Dhoni","Jaque kallis"))).upper()
    c_bowler1=(random.choice(("Glenn McGrath","Dale Steyn","Brett lee"))).upper()
    c_bowler2=(random.choice(("Harbhajan Singh","Mutiah Mulitharan","Shane Warne"))).upper()
    print(f"\n>{c} have {c_batsman1} and {c_batsman2} as Batsman , {c_bowler1} and {c_bowler2} as Bowlers\n")

    print("\n")

    Toss=False
  
    toss=input("Here comes the toss.\nChoose 'head' or 'tail' : \n").lower()
    if "head" in toss and rand_toss==1:
               print("Congratulations!You won the toss.")  
               Toss=True                  
    elif "tail" in toss and rand_toss==2:
               print("Congratulations!You won the toss.")      
               Toss=True     
    else:
               print("Opponent won the toss.")
               Toss=False


   

    if Toss==True:
      a=input("Choose what you want to do : Batting or Bowling \n").lower()
      if 'batting' in a:
           print("\nYou are batting first.\n")
         
           
      elif 'bowling' in a:
              print("\nYou are bowling first\n")
              
    else:
        if rand_o==1:
                print("\nOpposition is batting\n")
                
                
        elif rand_o==2:
                print("\nOpposition is bowling\n")
                
    


           
    print("\n")
    print("******************************")
    print("_____FIRST INNINGS BEGIN_____")
    print("******************************")


    runs1=0
    wickets1=0
    balls1=0
    while (wickets1 !=2 and balls1 !=12):
           user=int(input("\nEnter a number in between 1 to 6 : "))
           comp=random.randint(1,6)
           if user in range(1,7):
                  print(f"\nYour input was {user} and computer goes with {comp} ")
                  if user == comp:
                        wickets1+=1
                        print("-------------------------------------")
                        print("\n!!!OUT!!!\nAnother Batsman on Strike\n")
                        print("-------------------------------------")
                        
                  else:
                    if "batting" in a or rand_o==2:
                           Bat_first=u
                           Ball_first=c
                           runs1+=user 
                    elif "bowling" in a or rand_o==1:
                           Bat_first=c
                           Ball_first=u
                           runs1+=comp 
           print(f"\nScore={runs1}/{wickets1}")
           balls1+=1
           
           if balls1==6:
                         print("-------------------------------------")
                         print("Over 1 completed")
                         print("Bowler Changes")
                         print("-------------------------------------")
           elif balls1==12:
                         print("-------------------------------------")
                         print("Over 2 completed")
                         print("-------------------------------------")
           print("Balls remaining: ",12-balls1)
    print("\nFinal Score: \n")        
    print("Runs=",runs1)
    print("wickets=",wickets1)
    
                       
           
    print(f"\nThe Score of {Bat_first} is {runs1}, wickets lost were {wickets1} in {balls1} balls\n")       
    print("-------------------------------------")
    print("_____END OF FIRST INNINGS_____")
    print("-------------------------------------")
    print(f"\n{Ball_first} needs {runs1} in 12 balls with 2 wickets in hand\n")
    
         
    print("*********************************")
    print("_____SECOND INNINGS BEGIN_____")
    print("**********************************")
    runs2=0
    wickets2=0
    balls2=0
    while (wickets2 !=2 and balls2 !=12 and runs2<=runs1):
           user=int(input("\nEnter a number in between 1 to 6 : "))
           comp=random.randint(1,6)
           if user in range(1,7):
                  print(f"\nYour input was {user} and computer goes with {comp} ")
                  if user == comp:
                        wickets2+=1
                        print("-------------------------------------")
                        print("\n!!!OUT!!!\nAnother Batsman on Strike\n")
                        print("-------------------------------------")
                  else:
                    if "batting" in a or rand_o==2:
                           Bat_second=c
                           Ball_second=u
                           runs2+=comp 
                    elif "bowling" in a or rand_o==1:
                           Bat_second=u
                           Ball_second=c
                           runs2+=user 
           print(f"\nScore={runs2}/{wickets2}")
           balls2+=1
           
           if balls2==6:
                         print("-------------------------------------")
                         print("Over 1 completed")
                         print("Bowler changes")
                         print("-------------------------------------")
           elif balls2==12:
                         print("-------------------------------------")
                         print("Over 2 completed")
                         print("-------------------------------------")
           print("Balls remaining: ",12-balls2)
           
           if runs2 <= runs1 and balls2 <= 11 and wickets2 != 2:
             print(f"{Bat_second} needs {runs1-runs2 +1} run to win in {12-balls2} balls")


    print("\nFinal Score: \n")        
    print("Runs=",runs2)
    print("wickets=",wickets2)
    
                       
           
    print(f"\nThe Score of {Bat_second} is {runs2}, wickets lost were {wickets2} in {balls2} balls\n")       
    print("-------------------------------------")              
    print("_____END OF SECOND INNINGS_____")
    print("-------------------------------------")
    
    print("\n     ______RESULT______     \n")

    if runs1 > runs2:
 
      if Bat_first == u: 
        print(f" Congratulations! {u} won the Match by {runs1 - runs2} runs.")
 
      else:
        print(f" Better luck next time! The {c} won the Match by {runs1 - runs2} runs.") 
 
    elif runs2 > runs1:
 
     if Bat_second == u: 
        print(f" Congratulations! {u} won the Match by {2 - wickets2} wickets.")
 
     else:
        print(f" Better luck next time! The {c} won the Match by {2 - wickets2} wickets.")
 
    else:
      print("The Match is a Tie.","\nNo one Wins.")
 



    



    
else:
        print("Sorry,You entered wrong input!")



x=input("")#using so that terminal stay awake always





    