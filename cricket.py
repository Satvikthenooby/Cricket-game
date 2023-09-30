 

import random
rand_o=random.randint(1,2)
rand_toss=random.randint(1,2)
print("\n >>>>>>>>>------ BOOK CRICKET------>>>>>>>>>\n")

print("""\nWe all have played that book cricket game in our childhood. This game works just like that. Play it and relive your childhood.
      """)



#start
a=input("\n \n Press 's' to start this game__").lower()


#toss
  
if 's' in a:
    Toss=False
    
    u=" "
    c=" "
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


    Team=False
    if Toss==True:
      a=input("Choose what you want to do : Batting or Bowling \n").lower()
      if 'batting' in a:
           print("You are batting first.")
           Team=True
      elif 'bowling' in a:
              print("You are bowling first")
      else:
            Team=True
    else:
        if rand_o==1:
                print("Opposition is batting")
                Team=True
        elif rand_o==2:
                print("Opposition is bowling")
                Team=True
    
    if Team==True:
           u=input("Enter the name of your team : ")
           
           c=input("Enter the team whom you wish to defeat: ")
           print(f"\nYour team is {u} and computer is playing with team {c}  ")
    print("\n")

    print("_____FIRST INNINGS BEGIN_____\n")
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
                         print("Over 1 completed")
           elif balls1==12:
                         print("Over 2 completed")
           print("Balls remaining: ",12-balls1)
    print("\nFinal Score: \n")        
    print("Runs=",runs1)
    print("wickets=",wickets1)
    
                       
           
    print(f"\nThe Score of {Bat_first} is {runs1}, wickets lost were {wickets1} in {balls1} balls")       
                  
    print("_____END OF FIRST INNINGS_____")
    print(f"\n{Ball_first} needs {runs1} in 12 balls with 2 wickets in hand")
    
         

    print("\n_____SECOND INNINGS BEGIN_____")
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
                         print("Over 1 completed")
           elif balls2==12:
                         print("Over 2 completed")
           print("Balls remaining: ",12-balls2)
           
           if runs2 <= runs1 and balls2 <= 11 and wickets2 != 2:
             print(f"{Bat_second} needs {runs1-runs2 +1} run to win in {12-balls2} balls")


    print("\nFinal Score: \n")        
    print("Runs=",runs2)
    print("wickets=",wickets2)
    
                       
           
    print(f"\nThe Score of {Bat_second} is {runs2}, wickets lost were {wickets2} in {balls2} balls")       
                  
    print("\n_____END OF SECOND INNINGS_____")
    
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
        print(f" Better luck next time! The Computer won the Match by{2 - wickets2} wickets.")
 
    else:
      print("The Match is a Tie.","\nNo one Wins.")
 



    



    
else:
        print("Sorry,You entered wrong input!")



x=input("")#using so that terminal stay awake always





    