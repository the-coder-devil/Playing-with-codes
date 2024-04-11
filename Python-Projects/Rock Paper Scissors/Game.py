import random
win_count = 0

while True:
    choices = ["rock", "paper", "scissor"]
    bot_choice = random.choice(choices)
    player_choice = input("Please Input what you choose rock , paper or Scissor ").lower()

    while player_choice not in choices:
        player_choice = input("Input what you choose rock , paper or Scissor ").lower()

    print("your choice is :", player_choice)
    print("the bot chose :", bot_choice)

    if player_choice == bot_choice:
        print("It is a tie 🤷‍♂️ ")

    elif player_choice == "rock":
        if bot_choice == "paper":
            print("The bot won 🤣!")
        if bot_choice == "scissor":
            print("Congratulations! 🎉, You won")
            win_count = win_count + 1

    elif player_choice == "scissor":
        if bot_choice == "rock":
            print("The bot won 🤣!")
        if bot_choice == "paper":
            print("Congratulations! 🎉, You won")
            win_count = win_count + 1

    elif player_choice == "paper":
        if bot_choice == "scissor":
            print("The bot won 🤣!")
        if bot_choice == "rock":
            print("Congratulations! 🎉, You won")
            win_count += 1

    else:
        print("How did you do it? This was not supposed to be possible")

    re_start = input('''Do you want to re-play ? If yes , Press 'R' ... else , Type any other KEY ''').upper()
    if re_start == "R":
        continue
    else:
        break

print("Thanks for Playing")
print(f"You have won {win_count} times ")
