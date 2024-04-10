import random

def main():
    answer = math_problem()
    if input("Answer? ") == str(answer):
        print("You are correct!!")
    else: 
        print("You wrong fool")
    re()

def re():
    wish = input("Wanna do one more? (yes)").lower()
    if wish == 'yes':
        main()
    else:
        print("Thanks for Playing\nPlease come back")

def math_problem():
    operators = random.choice(["+","-","*"])
    left , right = random.randint(2,42), random.randint(5,34)
    expression = str(left) + operators + str(right)
    print(expression)
    return eval(expression)

main()