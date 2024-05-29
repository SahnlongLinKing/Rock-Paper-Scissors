import random
import asciihands

i = 1
while i < 2:
    userchoice = input(
        "Let's play rock paper scissors. Press 1 for rock, 2 for paper, and 3 for scissors. "
    )

    random_integer = random.randint(1, 3)

    if random_integer == 1:
        print(f"""I chose rock:
    {asciihands.rock}
    """)
        if userchoice == "1":
            print(f"""And you also chose rock:
      {asciihands.rock}
      """)
            print("It's a tie.")
        elif userchoice == "2":
            print(f"""And you chose paper:
      {asciihands.paper}
      """)
            print("You win.")
        elif userchoice == "3":
            print(f"""And you chose scissors:
      {asciihands.scissors}
      """)
            print("I win.")
        else:
            print("You didn't choose a valid option. You lose.")
    elif random_integer == 2:
        print(f"""I chose paper:
    {asciihands.paper}
    """)
        if userchoice == "1":
            print(f"""And you chose rock:
      {asciihands.rock}
      """)
            print("I win.")
        elif userchoice == "2":
            print(f"""And you also chose paper:
      {asciihands.paper}
      """)
            print("It's a tie.")
        elif userchoice == "3":
            print(f"""And you chose scissors:
      {asciihands.scissors}
      """)
            print("You win.")
        else:
            print("You didn't choose a valid option. You lose.")
    elif random_integer == 3:
        print(f"""I chose paper:
    {asciihands.paper}
    """)
        if userchoice == "1":
            print(f"""And you chose rock:
      {asciihands.rock}
      """)
            print("You win.")
        elif userchoice == "2":
            print(f"""And you also chose paper:
      {asciihands.paper}
      """)
            print("I win.")
        elif userchoice == "3":
            print(f"""And you also chose scissors:
      {asciihands.scissors}
      """)
            print("It's a tie.")
        else:
            print("You didn't choose a valid option. You lose.")

    playagain = input("Play again? Y/N\n")
    if playagain == "Y":
        i = 1
    elif playagain == "N":
        i += 1
