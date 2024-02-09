import random
import sys

def hand_crk_game():
# Greetings and Rules :
    print("\n***  Welcome to Hand Cricket World!  ***\n")
    print("Please Read the Rules :")
    print("1. Batsman can hit max 6 runs in a ball.\n2. If the Number of bawler and batman is matched, Batsman is out. \n3. If not matched, then batsman scores run.")
    print("4. The Match will continue until the both player have batted.")


    # for toss : and over decisions :
    def toss():
        toss_random = random.randint(0,2) #random from pc for toss.
        toss_choose = int(input("Choose 0 for Head and 1 for Tail : ")) # choose from player for head and tail
        # choose from player for bat and bowl
        if toss_choose == toss_random :
            print("You won the toss !")
            role_choose = int(input("Choose 1 for bat and  2 for bowl : "))
            
            if role_choose == 1:
                print ("You selected to bat first!")
                bat()
            elif role_choose == 2:
                print ("You selected to bat first!")
                bowl()
        
        elif toss_choose != toss_random :
            print("System won the toss !")
            role_random = random.randint(1,3)
            
            if role_random == 1:
                print ("System wants to bat first!")
                bat()
            elif role_random == 2:
                print ("System wants to bowl first!")
                bowl()
        sys.exit(0)    
    toss()       
    
            
    def random_run():
        return random.randint(0,7)
        

    def bat():
        run_bat = 0
        over = int(input("How many over will this match have? : "))
        for ball in range (1, (over*6) + 1):
            if run_bat != random_run():
                run_bat +=1
                print(f"your run is : {run_bat} in {ball} balls.")
            else:
                print("You are out.")
                print(f"You have scored {run_bat} in {ball} balls.")
        sys.exit(1) 
              
    def bowl():
        run_bowl = 0
        over = int(input("How many over will this match have? : "))
        for ball in range (1, (over*6) + 1):
            if run_bowl != random_run():
                run_bowl +=1
                print(f"System made {run_bowl} runs in {ball} balls.")
            else:
                print("System is out.")
                print(f"System have scored {run_bowl} in {ball} balls.")
        sys.exit(2)
    #def tie_game():
    #   if run_bat == run_bowl:
    #      print("You are tied..")
    
    # jo pc bat karatu hoy to your score ni jagyae PC's score is : em ane e pramane bowl ma pan..
            # two option : pc vla mate nava 2 funcn. banavo or bat() ane bowl () ma j slice string ma replce no use karvo.
hand_crk_game()
