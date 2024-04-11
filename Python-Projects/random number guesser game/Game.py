import random

number = random.randint(1, 25)

while True:
    for lives in range(4):
        guess = int(input("Enter a wild guess : "))

        if guess > 25:
            print("The guess should be in range {1,25}")
            break

    #At last lives , GAME OVER
        while lives == 3 and guess != number:
            print(f"HAHA!😂, LOOOSER😒 could not even guess it , the answer was {number}")
            break

    #IF the answer is correct , it'll break the loop
        if number == guess:
            print(f"Congratulations 😄! , You Guessed it right , Obviously the number is {number}")
            break

        elif number != guess:
            if number > guess:
                print(f"The Number is Greater than your Guess {guess}, should have tried a higher value")

            elif number < guess:
                print(f"The Number is Greater than your Guess {guess} , should have tried a lower value")
        #A indication of the number of lives {chances} left
        while lives != 3 :
            print(f"You have {3 - lives} lives left ")
            break


    re_start = input("Type R to restart ").lower()
    if re_start != "r":
        break
    else:
        continue

print("\n Thank you for Playing")
