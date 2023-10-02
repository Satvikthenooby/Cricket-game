#creating previous project with the help of oops...
import random

class Toss:

    
    def __init__(self,toss):
        
        self.toss=toss
        rand_toss=random.randint(1,2)
        rand_opt=random.randint(1,2)

        
        if ("heads" in self.toss and rand_toss==1) or ("tails" in self.toss and rand_toss==2):

            a=input("\n!!!--You have won the toss--!!!.\nChoose Bat or Bowl : ").lower()
            
            if "bat" in a:
                print("~~~~Gear up! You are batting first. Type 'w' to start the innings~~~~")
                
            elif "bowl" in a:
                print("~~~~Get Ready! You are bowling first. Type 's' to start the innings~~~~")
        elif ("head" in self.toss and rand_toss==2) or ("tail" in self.toss and rand_toss==1):
            if rand_opt==1:
                print("\n!!!---Opponent has won the toss---!!!\n--And elected to Bat first.Type 'd' to start the innings..\n")
            elif rand_opt==2:
                print("\n!!!---Opponent has won the toss---!!!\n--And elected to Bowl first.Type 'a' to start the innings..\n")

class Team():
    def __init__(self,team1,p1,p2,p3,p4,o1,o2,o3,o4):
        
       
        self.team1=team1
        
        self.o1=o1
        self.o2=o2
        self.o3=o3
        self.o4=o4
        
    
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
  
        print(f"\n--{(self.p1)}-- captaining Team --{(self.team1)}-- and other three players are --{(self.p2)}-- , --{(self.p3)}-- and --{(self.p4)}--")
        
        print(f"\nThe opposition is --WORLD XI-- which have --{o2}-- as captain and other three players are --{o1}-- , --{o3}-- and --{o4}--\n")

class Score():
    

    def __init__(self,who,playerteam):
        self.playerteam=playerteam
        self.who=who
        print("\n\n||||||||BEGINNING OF FIRST INNINGS||||||||\n\n")
        print(f"\nBatsman are on the crease. Bowlers are ready. Here comes the First ball.....\n")
        computer="WORLD XI"
        run1=0
        wickets1=0
        balls1=0
        while wickets1 !=2 and balls1 != 12:
          
          user=int(input("\nEnter A digit between 1 and 6: "))
          comp=random.randint(1,6)
          if user in range(1,7):
            print(f"Your input was {user} and computer played {comp}")
            if user==comp:
                wickets1+=1
                print("\n!!!!!That's Out.!!!!!!\n")
                print("Another batter is at the crease.\n")
            else:
                if "w" in self.who or "a" in self.who :
                    Bat_first=self.playerteam
                    bowl_first=computer
                    run1+=user
                elif "s" in self.who or "d" in self.who:
                    Bat_first=computer
                    bowl_first=self.playerteam
                    run1+=comp
            print(f"\nScore={run1}/{wickets1}")
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
        print("Runs=",run1)
        print("wickets=",wickets1)
    
                       
           
        print(f"\nThe Score of {Bat_first} is {run1}, wickets lost were {wickets1} in {balls1} balls\n") 

        print("-------------------------------------")
        print("_____END OF FIRST INNINGS_____")
        print("-------------------------------------")
        print(f"\n{bowl_first} needs {run1} in 12 balls with 2 wickets in hand\n")
    
         
        print("*********************************")
        print("_____SECOND INNINGS BEGIN_____")
        print("**********************************")

        run2=0
        wickets2=0
        balls2=0
        while wickets2!=2 and balls2!=12 and run2<run1:
            user=int(input("\nEnter A digit between 1 and 6: "))
            comp=random.randint(1,6)
            if user in range(1,7):
             print(f"Your input was {user} and computer played {comp}")
             if user==comp:
                wickets2+=1
                print("\n!!!!!That's Out.!!!!!!\n")
                print("Another batter is at the crease.\n")
             else:
                  if "w" in self.who or "a" in self.who :
                    Bat_second=computer
                    run2+=comp

                  elif "s" in self.who or "d" in self.who:
                    Bat_second=computer
                    run2+=user
                    
            print(f"\nScore={run2}/{wickets2}")
            balls2+=1
            if balls2==6:
                         print("-------------------------------------")
                         print("Over 1 completed")
                         print("Bowler Changes")
                         print("-------------------------------------")
            elif balls2==12:
                         print("-------------------------------------")
                         print("Over 2 completed")
                         print("-------------------------------------")
            print("Balls remaining: ",12-balls2)

            if run2 <= run1 and balls2 <= 11 and wickets2 != 2:
              print(f"{Bat_second} needs {run1-run2 +1} run to win in {12-balls2} balls")

        print("\nFinal Score: \n")        
        print("Runs=",run2)
        print("wickets=",wickets2)


        print(f"\nThe Score of {Bat_second} is {run2}, wickets lost were {wickets2} in {balls2} balls\n")       
        print("-------------------------------------")              
        print("_____END OF SECOND INNINGS_____")
        print("-------------------------------------")
    
        print("\n     ______RESULT______     \n")
        
        if run1 > run2:
 
          if Bat_first ==self.playerteam : 
           print(f" Congratulations! {self.player} won the Match by {run1 - run2} runs.")
 
          else:
           print(f" Better luck next time! The WORLD XI won the Match by {run1 - run2} runs.") 
 
        elif run2 > run1:
 
          if Bat_second == self.playerteam: 
            print(f" Congratulations! {self.playerteam} won the Match by {2 - wickets2} wickets.")
 
          else:
            print(f" Better luck next time! The WORLD XI won the Match by {2 - wickets2} wickets.")
 
        else:
         print("The Match is a Tie.","\nNo one Wins.")
                

     
     



yourteam=input("\nEnter the name of your team : \n").upper()
name=input("\nEnter your name : \n").upper()
player2=input("\nEnter Second player's name : \n").upper()
player3=input("\nEnter third player's name : \n").upper()
player4=input("\nEnter fourth player's name : \n").upper()

op1=(random.choice(('Steve Waugh','Virendra Sehwag','Sachin Tendulkar'))).upper()
op2=(random.choice(("Ricky Ponting","Ms Dhoni","Shane Warne"))).upper()
op3=(random.choice(("Glenn McGrath","Dale Steyn","Brett lee"))).upper()
op4=(random.choice(("Harbhajan Singh","Mutiah Mulitharan","Jaque kallis"))).upper()

toss=input("****Its Toss time****\n \nChoose Heads or Tails\n").lower()

team=Team(yourteam,name,player2,player3,player4,op1,op2,op3,op4)

t=Toss(toss) 
score=input("_")
sc=Score(score,yourteam)


x=input("  ")