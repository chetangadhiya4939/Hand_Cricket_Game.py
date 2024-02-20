import random
import sys

print("\n* JAY SWAMINARAYAN *")
# local run varialbles for each matches.r1=player hitted, r2=player score.
print("\n***  Welcome to Hand Cricket World!  ***\n")


def random_run():#random run for system
    return random.randint(1, 10)


def tie1():
    tr1, tr2 = 0, 0#tie variables
    tn1, tn2, tn3 = 0, 0, 0
    
    for ball in range(1, 7):

        tr1 = int(input("\nYou Hitted : "))
        trun = random_run()
        print("System Hitted : ", trun)

        if tr1 < 1 or tr1 > 10:#invalid input error message.
            print("Enter the valid number (1-10).")
            break

        elif tr1 != trun:#number hitted by system and player is not matched then increment of run of player.
            tr2 += tr1
            print(f"\nYour run is : {tr2}")

        if tr1 == trun or ball == 6:#if runs are same or balls over then out of inning over.
            if tr1==trun:
                print("\nYou are out.")
                print(f"*** Your total score : {tr2} in {ball} balls. ***")
                print("Target of System is : ", tr2 + 1)
                print("\n\n ***System Turns to Bat***\n\n")

                for b in range(1, 7):#Inning 2.

                    try:
                        tn1 = int(input("You hitted : "))
                        tn2 = random_run()
                        print("System Hitted : ", tn2)

                        if tn1 != tn2:
                            tn3 += tn2
                            print(f"\nSystem Scored : {tn3}")
                            
                        if tn1 == tn2:
                            print("\nSystem is out.")
                            print(f"*** Total score of syestem : {tn3} in {ball} balls. ***")
                            
                            if tr2 > tn3:
                                print(f"System Scored {tn3} and Your Scored {tr2}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit()

                            elif tr2 < tn3:
                                print(f"You Scored {tr2} and System Scored {tn3}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit() 
                            
                            elif tr2 == tn3:
                                print("Match tied !")
                                print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                                tie2()
                            
                        if b == 6:
                            print("\nInning is Over.")
                            print(f"*** Total score of syestem : {tn3} in {ball} balls. ***")
                            
                            if tr2 < tn3:
                                print(f"You Scored {tr2} and System Scored {tn3}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit() 
                            
                            elif tr2 == tn3:
                                print("Match tied !")
                                print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                                tie2()
                        
                            elif tr2 > tn3:
                                print(f"System Scored {tn3} and Your Scored {tr2}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit()
  
                    except ValueError:
                        print("Enter a valid Number (1-10).")
                        sys.exit()

            elif ball == 6:
                print("\nInning is Over.")
                print(f"*** Your total score : {tr2} in {ball} balls. ***")
                print("Target of System is : ", tr2 + 1)
                print("\n\n ***System Turns to Bat***\n\n")

                for b in range(1, 7):

                    try:
                        tn1 = int(input("You hitted : "))
                        tn2 = random_run()
                        print("System Hitted : ", tn2)

                        if tn1 != tn2:
                            tn3 += tn2
                            print(f"\nSystem Scored : {tn3}")
                            
                        if tn1 == tn2:
                            print("\nSystem is out.")
                            print(f"*** Total score of syestem : {tn3} in {ball} balls. ***")
                            
                            if tr2 > tn3:
                                print(f"System Scored {tn3} and Your Scored {tr2}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit()

                            elif tr2 < tn3:
                                print(f"You Scored {tr2} and System Scored {tn3}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit() 
                            
                            elif tr2 == tn3:
                                print("Match tied !")
                                print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                                tie2()
                            
                        if b == 6:
                            print("\nInning is Over.")
                            print(f"*** Total score of syestem : {tn3} in {ball} balls. ***")
                            
                            if tr2 < tn3:
                                print(f"You Scored {tr2} and System Scored {tn3}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit() 
                            
                            elif tr2 == tn3:
                                print("Match tied !")
                                print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                                tie2()
                        
                            elif tr2 > tn3:
                                print(f"System Scored {tn3} and Your Scored {tr2}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit()
  
                    except ValueError:
                        print("Enter a valid Number (1-10).")
                        sys.exit()

def tie2():
    tr3, tr4, trun = 0, 0, 0#tie2 variables
    tn4, tn5, tn6 = 0, 0, 0
    

    for ball in range(1, 7):#Inning 1

        trun = random_run()
        tr3 = int(input("\nYou Hitted : "))
        print("System Hitted : ", trun)

        if trun != tr3:#both number are not same then increment of run of player
            tr4 += trun
            print(f"\nSystem Scored : {tr4}")

        if trun == tr3 or ball ==  6:#if runs are same or balls over then out of inning over.
            if trun == tr3:
                print("\nSystem is out.")
                print(f"*** Total score of syestem : {tr4} in {ball} balls. ***")
                print("Your target is : ", tr4 + 1)
                print("\n\n ***You Turns to Bat***\n\n")

                for b in range(1, 7):#Inning 2.

                    try:
                        tn4 = random_run()
                        tn5 = int(input("You Hitted : "))
                        print("System Hitted : ", tn4)

                        if tn4 != tn5:
                            tn6 += tn5
                            print(f"\nYou Scored : {tn6}")

                        if tn5 == tn4:
                            print("\nYou are out.")
                            print(f"*** Total score of You : {tn6} in {ball} balls. ***")
                            
                            if tn6 > tr4:
                                print(f"System Scored {tr4} and Your Scored {tn6}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit(0)
                                    
                            elif tn6 < tr4:
                                print(f"You Scored {tn6} and System Scored {tr4}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit()
                                
                            elif tr4 == tn6:
                                print("Match tied !")
                                print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                                tie1()
                                
                        if b == 6:
                            print("\nInning is Over.")
                            print(f"*** Total score of You : {tn6} in {ball} balls. ***")
                           
                            if tn6 < tr4:
                                print(f"You Scored {tn6} and System Scored {tr4}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit()
                            
                            elif tr4 == tn6:
                                print("Match tied !")
                                print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                                tie1()
                                
                                
                            elif tn6 > tr4:
                                    print(f"System Scored {tr4} and Your Scored {tn6}")
                                    print("\n\nYou won the match.\n\n")
                                    sys.exit(0)
                        
                    except ValueError:
                        print("Enter a valid Number (1-10).")
                        sys.exit()
  
                        
            elif ball == 6:
                print("\nInning Over.")
                print(f"*** Total score of syestem : {tr4} in {ball} balls. ***")
                print("Your target is : ", tr4 + 1)
                print("\n\n ***You Turns to Bat***\n\n")

                for b in range(1, 7):

                    try:
                        tn4 = random_run()
                        tn5 = int(input("You Hitted : "))
                        print("System Hitted : ", tn4)

                        if tn4 != tn5:
                            tn6 += tn5
                            print(f"\nYou Scored : {tn6}")

                        if tn5 == tn4:
                            print("\nYou are out.")
                            print(f"*** Total score of You : {tn6} in {ball} balls. ***")
                            
                            if tn6 > tr4:
                                print(f"System Scored {tr4} and Your Scored {tn6}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit(0)
                                    
                            elif tn6 < tr4:
                                print(f"You Scored {tn6} and System Scored {tr4}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit()
                                
                            elif tr4 == tn6:
                                print("Match tied !")
                                print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                                tie1()
                                
                        if b == 6:
                            print("\nInning is Over.")
                            print(f"*** Total score of You : {tn6} in {ball} balls. ***")
                           
                            if tn6 < tr4:
                                print(f"You Scored {tn6} and System Scored {tr4}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit()
                            
                            elif tr4 == tn6:
                                print("Match tied !")
                                print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                                tie1()
                                
                                
                            elif tn6 > tr4:
                                    print(f"System Scored {tr4} and Your Scored {tn6}")
                                    print("\n\nYou won the match.\n\n")
                                    sys.exit(0)
                        
                    except ValueError:
                        print("Enter a valid Number (1-10).")
                        sys.exit()

def match1():
    r1, r2 = 0, 0
    n1, n2, n3 = 0, 0, 0
    over = int(input("\nHow many overs will this match have? : "))

    for ball in range(1, (over * 6) + 1):

        r1 = int(input("\nYou Hitted : "))
        run = random_run()
        print("System Hitted : ", run)

        if r1 < 1 or r1 > 10:
            print("Enter the valid number (1-10).")
            sys.exit()

        elif r1 != run:
            r2 += r1
            print(f"\nYour run is : {r2}")

        if r1 == run or ball == (over*6):
            if r1==run:
                print("\nYou are out.")
                print(f"*** Your total score : {r2} in {ball} balls. ***")
                print("Target of System is : ", r2 + 1)
                print("\n\n ***System Turns to Bat***\n\n")

                for b in range(1, (over * 6) + 1):

                    try:
                        n1 = int(input("You hitted : "))
                        n2 = random_run()
                        print("System Hitted : ", n2)

                        if n1 != n2:
                            n3 += n2
                            print(f"\nSystem Scored : {n3}")
                            
                        if n1 == n2:
                            print("\nSystem is out.")
                            print(f"*** Total score of syestem : {n3} in {ball} balls. ***")
                            
                            if r2 > n3:
                                print(f"System Scored {n3} and Your Scored {r2}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit()

                            elif r2 < n3:
                                print(f"You Scored {r2} and System Scored {n3}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit() 
                            
                            elif r2 == n3:
                                print("Match tied !")
                                print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                                tie2()
                            
                        if b == (over * 6):
                            print("\nInning is Over.")
                            print(f"*** Total score of syestem : {n3} in {ball} balls. ***")
                            
                            if r2 < n3:
                                print(f"You Scored {r2} and System Scored {n3}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit() 
                            
                            elif r2 == n3:
                                print("Match tied !")
                                print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                                tie2()
                        
                            elif r2 > n3:
                                print(f"System Scored {n3} and Your Scored {r2}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit()
  
                    except ValueError:
                        print("Enter a valid Number (1-10).")
                        sys.exit()
                        
            elif ball == (over * 6):
                print("\nInning is Over.")
                print(f"*** Your total score : {r2} in {ball} balls. ***")
                print("Target of System is : ", r2 + 1)
                print("\n\n ***System Turns to Bat***\n\n")

                for b in range(1, (over * 6) + 1):

                    try:
                        n1 = int(input("You hitted : "))
                        n2 = random_run()
                        print("System Hitted : ", n2)

                        if n1 != n2:
                            n3 += n2
                            print(f"\nSystem Scored : {n3}")
                            
                        if n1 == n2:
                            print("\nSystem is out.")
                            print(f"*** Total score of syestem : {n3} in {ball} balls. ***")
                            
                            if r2 > n3:
                                print(f"System Scored {n3} and Your Scored {r2}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit()

                            elif r2 < n3:
                                print(f"You Scored {r2} and System Scored {n3}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit() 
                            
                            elif r2 == n3:
                                print("Match tied !")
                                print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                                tie2()
                            
                        if b == (over * 6):
                            print("\nInning is Over.")
                            print(f"*** Total score of syestem : {n3} in {ball} balls. ***")
                            
                            if r2 < n3:
                                print(f"You Scored {r2} and System Scored {n3}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit() 
                            
                            elif r2 == n3:
                                print("Match tied !")
                                print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                                tie2()
                        
                            elif r2 > n3:
                                print(f"System Scored {n3} and Your Scored {r2}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit()
  
                    except ValueError:
                        print("Enter a valid Number (1-10).")
                        sys.exit()

    
def match2():
    r3, r4, run = 0, 0, 0
    n4, n5, n6 = 0, 0, 0
    over = int(input("\nHow many overs will this match have? : "))

    for ball in range(1, (over * 6) + 1):

        r3 = int(input("\nYou Hitted : "))
        run = random_run()
        print("System Hitted : ", run)
        
        if r3 < 1 or r3 > 10:
            print("Enter the valid number (1-10).")
            sys.exit()

        elif run != r3:
            r4 += run
            print(f"\nSystem Scored : {r4}")

        if run == r3 or ball == (over * 6):
            if run == r3:
                print("\nSystem is out.")
                print(f"*** Total score of syestem : {r4} in {ball} balls. ***")
                print("Your target is : ", r4 + 1)
                print("\n\n ***You Turns to Bat***\n\n")

                for b in range(1, (over * 6) + 1):

                    try:
                        n4 = random_run()
                        n5 = int(input("You Hitted : "))
                        if n5 < 1 or n5 > 10:
                            print("Enter the valid number (1-10).")
                            sys.exit()
                            
                        print("System Hitted : ", n4)

                        if n4 != n5:
                            n6 += n5
                            print(f"\nYou Scored : {n6}")

                        if n5 == n4:
                            print("\nYou are out.")
                            print(f"*** Total score of You : {n6} in {ball} balls. ***")
                            
                            if n6 > r4:
                                print(f"System Scored {r4} and Your Scored {n6}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit(0)
                                    
                            elif n6 < r4:
                                print(f"You Scored {n6} and System Scored {r4}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit()
                                
                            elif r4 == n6:
                                print("Match tied !")
                                print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                                tie1()
                                
                        if b == (over * 6):
                            print("\nInning is Over.")
                            print(f"*** Total score of You : {n6} in {ball} balls. ***")
                           
                            if n6 < r4:
                                print(f"You Scored {n6} and System Scored {r4}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit()
                            
                            elif r4 == n6:
                                print("Match tied !")
                                print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                                tie1()
                                
                                
                            elif n6 > r4:
                                    print(f"System Scored {r4} and Your Scored {n6}")
                                    print("\n\nYou won the match.\n\n")
                                    sys.exit(0)
                        
                    except ValueError:
                        print("Enter a valid Number (1-10).")
                        sys.exit()
                        
            elif ball == (over * 6):
                print("\nInning Over.")
                print(f"*** Total score of syestem : {r4} in {ball} balls. ***")
                print("Your target is : ", r4 + 1)
                print("\n\n ***You Turns to Bat***\n\n")

                for b in range(1, (over * 6) + 1):

                    n4 = random_run()

                    try:
                        n5 = int(input("You Hitted : "))
                        if n5 < 1 or n5 > 10:
                            print("Enter the valid number (1-10).")
                            sys.exit()
                            
                        print("System Hitted : ", n4)

                        if n4 != n5:
                            n6 += n5
                            print(f"\nYou Scored : {n6}")

                        if n5 == n4:
                            print("\nYou are out.")
                            print(f"*** Total score of You : {n6} in {ball} balls. ***")
                            
                            if n6 > r4:
                                print(f"System Scored {r4} and Your Scored {n6}")
                                print("\n\nYou won the match.\n\n")
                                sys.exit(0)
                                    
                            elif n6 < r4:
                                print(f"You Scored {n6} and System Scored {r4}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit()
                                
                            elif r4 == n6:
                                print("Match tied !")
                                print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                                tie1()
                                
                        if b == (over * 6):
                            print("\nInning is Over.")
                            print(f"*** Total score of You : {n6} in {ball} balls. ***")
                           
                            if n6 < r4:
                                print(f"You Scored {n6} and System Scored {r4}")
                                print("\n\nYou lose the match.\n\n")
                                sys.exit()
                            
                            elif r4 == n6:
                                print("Match tied !")
                                print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                                tie1()
                                
                                
                            elif n6 > r4:
                                    print(f"System Scored {r4} and Your Scored {n6}")
                                    print("\n\nYou won the match.\n\n")
                                    sys.exit(0)
                                
                    except ValueError:
                        print("Enter a valid Number (1-10).")
                        sys.exit()

# for toss : and over decisions :
def toss():
    toss_random = random.randint(0, 1)  # random from pc for toss.
    toss_choose = int(input("Choose 0 for Head and 1 for Tail : "))  # choose from player for head and tail

    try:
        if toss_choose == 0 or toss_choose == 1:
            pass

        elif toss_choose < 0 or toss_choose > 1:
            raise ValueError("Enter the valid number: 0 or 1 only.")

    except ValueError as ve:
        print(ve)
        sys.exit()

    except TypeError:
        print("Enter the valid number: 0 or 1 only.")
        sys.exit()
    # choose from player for please enter a valid number and bowl
    if toss_choose == toss_random:
        print("You won the toss !")
        role_choose = int(input("Choose 0 for bat and 1 for bowl : "))

        try:
            if role_choose == 0:
                print("Your turn to bat!")
                match1()

            elif role_choose == 1:
                print("\nSystem turns to Bat !\n")
                print("Your turn to bowl!")
                match2()
            #raising of value error for invalid input.
            else:
                raise ValueError("Enter a valid number: 0 or 1 only.")

        except ValueError as ve:
            print(ve)

    elif toss_choose != toss_random:
        print("System won the toss !")
        role_random = random.randint(0, 1)

        try:
            if role_random == 0:
                print("\nSystem turns to bat !\n")
                print("Your turn to bowl!")
                match2()

            elif role_random == 1:
                print("\nSystem turns to bowl !\n")
                print("Your turn to bat!")
                match1()
            #raising of value error for invalid input.
            else:
                raise ValueError("Enter a valid number: 0 or 1 only.")

        except ValueError as ve:
            print(ve)
            sys.exit(0)


toss()
