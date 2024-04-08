import random

def main():
    num_players = num_playrs()
    scores = starting_score(num_players)
    max_score = 50
    the_game(scores,max_score,num_players)
    replay()

def replay():
    ask = input("Do you want to play again (y): ")
    if ask.lower() == "y":
        main()

def roll():
    #min value , max value
    return random.randint(1,6)

def num_playrs():
    while True:
        num = input("Enter the number of Players (2-4): ")
        if num.isdigit():
            if 2 <= int(num) <= 4:
                print(f"numbers of Players are {num}🙂")
                return int(num)
                break
            else:
                print("Please enter a number between 2-4")
        else:
            print("Invalid Input. Try Again!")

def starting_score(num):
    players = num
    return [0 for _ in range(players)]

def the_game(scores,max_score,num_players):
    print("Welcome to the game !!")
    while True:
        for player_ind in range(num_players):
            print(f"\n It's Player {player_ind + 1}'s turn \n")
            value = 0
            while True:
                rolls = input("Do you want to roll the dice (y)🥺?")
                if rolls.lower() != 'y':
                    print("OK.")
                    break
                dice = roll()
                print(f"You rolled an {dice}!")
                if dice == 1:
                    print(f"Sed man🥲. You got a 1. Everything you earned in this round is now 0")
                    value = 0
                    break
                value += dice
                print(f"Congratulations on getting an {dice},your score is now {value}😎")
            scores[player_ind] += value
            print(f"\nHello Player {player_ind+1}, you current total score is {scores[player_ind]}\n")
            if max(scores) > max_score :
                print(f"Congratulations 🎉🎊🥳 to Player {scores.index(max(scores))+1} on winning the game!!")
                break
        if max(scores) > max_score :
            break

main()