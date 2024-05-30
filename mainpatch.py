import random
import asciihands

i = 1
while i < 2:
    userchoice = int(input(
        "Let's play rock paper scissors. Press 1 for rock, 2 for paper, and 3 for scissors. "
    ))

    cpuchoice = random.randint(1, 3)

    if userchoice == cpuchoice:
        if userchoice == 1:
            print(f"""We both chose rock:
                  {asciihands.rock}""")
            print("It's a tie.")
        elif userchoice == 2:
            print(f"""We both chose paper:
                  {asciihands.paper}""")
            print("It's a tie.")
        elif userchoice == 3:
            print(f"""We both chose scissors:
                  {asciihands.scissors}""")
            print("It's a tie.")
    elif userchoice == 3 and cpuchoice == 1:
        print(f"""You've chosen scissors:
              {asciihands.scissors}""")
        print(f"""And I chose rock:
              {asciihands.rock}""")
        print("I win.")
    elif userchoice == 1 and cpuchoice == 3:
        print(f"""You've chosen rock:
              {asciihands.rock}""")
        print(f"""And I chose scissors:
              {asciihands.scissors}""")
        print("I win.")
    elif userchoice > cpuchoice:
        if userchoice == 2:
            print(f"""You chose paper:
                  {asciihands.paper}""")
            print(f"""And I chose rock:
                  {asciihands.rock}""")
            print("You win.")
        elif userchoice == 2:
            print(f"""You chose scissors:
                  {asciihands.scissors}""")
            print(f"""And I chose paper:
                  {asciihands.paper}""")
            print("You win.")
    elif userchoice < cpuchoice:
        if userchoice == 1:
            print(f"""You chose rock:
                  {asciihands.rock}""")
            print(f"""And I chose paper:
                  {asciihands.paper}""")
            print("I win.")
        elif userchoice == 2:
            print(f"""You chose paper:
                  {asciihands.paper}""")
            print(f"""And I chose scissors:
                  {asciihands.scissors}""")
            print("I win.")
    else:
        print("""Either, you didn't choose a valid input, or my programming is failing.
               If you chose a valid input, please contact arcticsnakeyt@gmail.com to report a bug.""")
    playagain = input("Play again? Y/N\n")
    if playagain.lower() == "y":
        i = 1
    else:
        i += 1
