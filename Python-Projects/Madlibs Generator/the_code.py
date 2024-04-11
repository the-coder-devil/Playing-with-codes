def main():
    with open('story.txt','r') as s :
        story = s.read()

    #Creating a set to store the "<words>" inside, set so that only unquie ones are there
    words = set()

    #using enumerate to get the index and character value
    for i,char in enumerate(story):
        if char == "<":
            char_index ,end_ind = i, i
            while True:
                end_ind += 1
                if story[end_ind] == ">":
                    #Finally adding the word to the set
                    words.add(story[char_index:end_ind+1])
                    break

    #Asking user to assign their own desirable values
    for word in words:
        answer = input(f"Enter your own word for {word}: ")
        story = story.replace(word,answer)

    print(story)

main()