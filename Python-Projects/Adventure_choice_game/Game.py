from random import choice

name = input("Welcome to the game \nhow may I adress you ?").title().strip()
print(f"Hello there, {name} WELCOME TO THE TRUTH!\n")

def main():
    the_game()
    print("\nNo one can escape the truth")
    replay()
    
    
def the_game():
    print("You are suddenly awoken in the middle of nowhere, after travelling for about 5 minutes you found 2 ways : a village and a forest")
    choice_one = input("1. Enter the village \n2. Enter the forest\n")
    wild_animals = ["Lion","Tiger","Bear","Gorilla"]
    if choice_one == "2":
        choice_two = input(f"in the forest after walking for few minutes you unexpextly met a {choice(wild_animals)}, you either fight or flee ! \n")
        if choice_two.lower() == "fight" :
            print("YOU LOST THE FIGHT , YOU ARE DEAD!")
        elif choice_two.lower() == "flee" :
            print("YOU CAN'T OUTRUN IT , YOU ARE DEAD !")
        else:
            print("Invalid choice , YOU LOST")

    elif choice_one == "1":
        choice_three = input("You met an old man inside the village all alone , after seeing you he offers you a place to stay\nyou either accept or reject his offer\n").lower() 
        if choice_three == "accept":   
            print("you ware led to an old house by the man , and were asked to stay there for the night")
            choice_four = input("You heard an errie voice in the house , you decided to either Investigate , hide in the house or run outside the village\n")
            if choice_four.lower() == "investigate":
                print("YOU FOUND A GHOST OUTSIDE , HE KILLED YOU")
            elif choice_four.lower() == "hide":
                print("IN FEW HOURS, THE GHOST CAME INSIDE AND KILLS YOU")
            elif choice_four.lower() == "run":
                choice_five = input(f"in the forest after running for few minutes you unexpextly met a {choice(wild_animals)}, you either fight or flee ! ")
                if choice_five.lower() == "fight" :
                    print("YOU LOST THE FIGHT , YOU ARE DEAD!")
                elif choice_five.lower() == "flee" :
                    print("YOU CAN'T OUTRUN IT , YOU ARE DEAD !")
                else:
                    print("Invalid choice , YOU LOST")
            else:
                print("Invalid Choice , YOU LOST")
        elif choice_three.lower() == "reject":
            print("The old man got offended and decides to kill you anyway , YOU DIED")
        else:
            print("Invalid choice, YOU LOSE!")
    
def replay():
    if input("Wanna Play again?(yes/no)") == "yes":
        main()
    else:
        print("Thank you for playing this game")

main()