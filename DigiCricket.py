import random
import sys

print("\n* JAY SWAMINARAYAN *")
# local run varialbles for each matches.r1=player hitted, r2=player score.
print("\n***  Welcome to Hand Cricket World!  ***\n")


def random_run():
    return random.randint(1, 10)


def tie1():
    tr1, tr2 = 0, 0
    tn1, tn2, tn3 = 0, 0, 0

    for ball in range(1, 7):

        tr1 = int(input("\nYou Hitted : "))
        run = random_run()
        print("System Hitted : ", run)

        if tr1 < 1 or tr1 > 10:
            print("Enter the valid number (1-10).")
            break

        elif tr1 != run:
            tr2 += tr1
            print(f"\nYour run is : {tr2}")

        elif tr1 == run:
            print("\nYou are out.")
            print(f"*** Your total score : {tr2} in {ball} balls. ***")
            print("Target of System is : ", tr2 + 1)
            print("\n\n ***System Turns to Bat***\n\n")

        if ball == 6:
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

            elif tn1 == tn2:
                print("\nSystem is out.")
                print(f"*** Total score of syestem : {tn3} in {ball} balls. ***")

            if tr2 > tn3:
                    print(f"System Scored {tn3} and Your Scored {tr2}")
                    print("\n\nYou won the match.\n\n")

            if b == 6:
                print("\nInning is Over.")
                print(f"*** Total score of syestem : {tn3} in {ball} balls. ***")

                if tr2 == tn3:
                    print("Match tied !")
                    print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                    tie2()

                elif tr2 < tn3:
                    print(f"You Scored {tr2} and System Scored {tn3}")
                    print("\n\nYou lose the match.\n\n")

        except ValueError:
            print("Enter a valid Number (1-10).")


def tie2():
    tr3, tr4, trun = 0, 0, 0
    tn4, tn5, tn6 = 0, 0, 0

    for ball in range(1, 7):

        trun = random_run()
        tr3 = int(input("\nYou Hitted : "))
        print("System Hitted : ", trun)

        if trun != tr3:
            tr4 += trun
            print(f"\nSystem Scored : {tr4}")

        elif trun == tr3:
            print("\nSystem is out.")
            print(f"*** Total score of syestem : {tr4} in {ball} balls. ***")
            print("Your target is : ", tr4 + 1)
            print("\n\n ***You Turns to Bat***\n\n")

        if ball == 6:
            print("\nInning Over.")
            print(f"*** Total score of syestem : {tr4} in {ball} balls. ***")
            print("Your target is : ", tr4 + 1)
            print("\n\n ***You Turns to Bat***\n\n")

    for b in range(1, 7):

        tn4 = random_run()

        try:
            tn5 = int(input("You Hitted : "))

            print("System Hitted : ", tn4)

            if tn5 != tn4:
                tn6 += tn4
                print(f"\nSystem Scored : {tn6}")

            elif tn5 == tn4:
                print("\nSystem is out.")
                print(f"*** Total score of syestem : {tn6} in {ball} balls. ***")

            if tr4 > tn6:
                    print(f"System Scored {tn6} and Your Scored {tr4}")
                    print("\n\nYou won the match.\n\n")

            if b == 6:
                print("\nInning is Over.")
                print(f"*** Total score of syestem : {tn6} in {ball} balls. ***")

                if tr4 == tn6:
                    print("Match tied !")
                    print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                    tie1()

                elif tr4 < tn6:
                    print(f"You Scored {tr4} and System Scored {tn6}")
                    print("\n\nYou lose the match.\n\n")

        except ValueError:
            print("Enter a valid Number (1-10).")


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
            break

        elif r1 != run:
            r2 += r1
            print(f"\nYour run is : {r2}")

        elif r1 == run:
            print("\nYou are out.")
            print(f"*** Your total score : {r2} in {ball} balls. ***")
            print("Target of System is : ", r2 + 1)
            print("\n\n ***System Turns to Bat***\n\n")

        if ball == (over * 6):
            print("\nInning is Over.")
            print(f"*** Your total score : {r2} in {ball} balls. ***")
            print("Target of System is : ", r2 + 1)
            print("\n\n ***System Turns to Bat***\n\n")

    for b in range(1, (over * 6) + 1):

        try:
            n1 = int(input("You hitted : "))
            n2 = random_run()
            print("System Hitted : ", n2)

            if n2 != n1:
                n3 += n1
                print(f"\nSystem Scored : {n3}")

            elif n2 == n1:
                print("\nSystem is out.")
                print(f"*** Total score of syestem : {n3} in {ball} balls. ***")

            if r2 > n3:
                    print(f"System Scored {n3} and Your Scored {r2}")
                    print("\n\nYou won the match.\n\n")

            if b == (over * 6):
                print("\nInning is Over.")
                print(f"*** Total score of syestem : {n3} in {ball} balls. ***")

                if r2 == n3:
                    print("Match tied !")
                    print("\n\n**SYESTEM TURNS TO BAT AGAIN.**\n\n")
                    tie2()

                elif r2 < n3:
                    print(f"You Scored {r2} and System Scored {n3}")
                    print("\n\nYou lose the match.\n\n")

        except ValueError:
            print("Enter a valid Number (1-10).")


def match2():
    r3, r4, run = 0, 0, 0
    n4, n5, n6 = 0, 0, 0
    over = int(input("\nHow many overs will this match have? : "))

    for ball in range(1, (over * 6) + 1):

        run = random_run()
        r3 = int(input("\nYou Hitted : "))
        print("System Hitted : ", run)

        if run != r3:
            r4 += run
            print(f"\nSystem Scored : {r4}")

        elif run == r3:
            print("\nSystem is out.")
            print(f"*** Total score of syestem : {r4} in {ball} balls. ***")
            print("Your target is : ", r4 + 1)
            print("\n\n ***You Turns to Bat***\n\n")

        if ball == (over * 6):
            print("\nInning Over.")
            print(f"*** Total score of syestem : {r4} in {ball} balls. ***")
            print("Your target is : ", r4 + 1)
            print("\n\n ***You Turns to Bat***\n\n")

    for b in range(1, (over * 6) + 1):

        n4 = random_run()

        try:
            n5 = int(input("You Hitted : "))
            n4 = random_run
            print("System Hitted : ", n4)

            if n5 != n4:
                n6 += n4
                print(f"\nSystem Scored : {n6}")

            elif n5 == n4:
                print("\nSystem is out.")
                print(f"*** Total score of syestem : {n6} in {ball} balls. ***")

            if r4 > n6:
                    print(f"System Scored {n6} and Your Scored {r4}")
                    print("\n\nYou won the match.\n\n")

            if b == (over * 6):
                print("\nInning is Over.")
                print(f"*** Total score of syestem : {n6} in {ball} balls. ***")
            
                if r4 == n6:
                    print("Match tied !")
                    print("\n\n**YOUR TURN TO BAT AGAIN**\n\n")
                    tie1()

                elif r4 < n6:
                    print(f"You Scored {r4} and System Scored {n6}")
                    print("\n\nYou lose the match.\n\n")

        except ValueError:
            print("Enter a valid Number (1-10).")


# for toss : and over decisions :
def toss():
    toss_random = random.randint(0, 1)  # random from pc for toss.
    toss_choose = int(
        input("Choose 0 for Head and 1 for Tail : ")
    )  # choose from player for head and tail

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
    # choose from player for balease enter a valid numbet and bowl
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

            else:
                raise ValueError("Enter a valid number: 0 or 1 only.")

        except ValueError as ve:
            print(ve)
            sys.exit(0)


toss()
