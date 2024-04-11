def main():
    print("Welcome to the Program!")
    msg = input("Please enter your passage:")
    conveter(msg)
    counter(msg.lower())

def counter(msg):
    character , vowels , const , spaces , special_char , numerical_char, dots = 0,0,0,0,0,0,0
    for i in msg:
        character += 1
        if i in ['a','i','e','o','u']:
            vowels += 1
        elif i == ' ':
            spaces += 1
        elif i == '.':
            dots += 1
        elif i in ['!','`','~','@','#','$',"%","^",'&','*','(',')','-','_','+','=','<','>',',','?','/','"',"'",";",":"]:
            special_char += 1
        elif i in ["0","1","2","3",'4','5','6','7','8','9']:
            numerical_char += 1
        else :
            const += 1  
    print(f'''number of characters: {character}\nnumber of vowels: {vowels}\nnumber of consonants: {const}\nnumber of dots: {dots}
    number of spaces: {spaces}\nnumber of special characters: {special_char}\nnumber of numerical values:{numerical_char}''')
    print("Thank you for using me")

def conveter(message):
    words = 0
    for i in message:
        if i.isspace():
            words += 1
    print(f"number of words are: {words}")

main()