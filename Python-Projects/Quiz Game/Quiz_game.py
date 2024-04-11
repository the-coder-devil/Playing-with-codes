
print("Welcome to the quiz")

def main():
    marks = question(score=0)
    print(f"your score is {marks} ")
    
def question(score):
    quest_one,ans_one = "What's the capital of India? ","new delhi"
    score = check_quest(quest_one,ans_one,score)

    quest_two,ans_two = "Name of first person to set foot on moon ","neil armstrong"
    score = check_quest(quest_two,ans_two,score)

    quest_three,ans_three  = "India got it's independence on year? ","1947"
    score = check_quest(quest_three,ans_three,score)
    
    quest_four, ans_four = "Name the largest Continent ","asia"
    score = check_quest(quest_four,ans_four,score)
    
    quest_five,ans_five = "which is the largest country in world ? ","russia"
    score = check_quest(quest_five,ans_five,score)
    
    quest_six,ans_six = "Which country has the strongest Military ? ","usa"
    score = check_quest(quest_six,ans_six,score)

    return score

def correct(score):
    print("Your answer is correct!!")
    score += 1
    return score

def wrong():
    print("Your answer is wrong buddy")

def check_quest(question,answer,score):
    if input(question).lower() == answer:
        score = correct(score)
    else:
        wrong()
    return score

main()