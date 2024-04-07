from cryptography.fernet import Fernet

def main():
    master_key = "Lucifer"
    for i in range(4):
        master_pass = input("Enter the master password : ").strip()
        if master_pass == "EX":
            print("You are exiting now ....")
            break
        elif master_pass != master_key: 
            print(f"WRONG PASSWORD !! ")
            if i != 3:
                print(f"PLEASE TRY A DIFFERENT OPTION \nyou have {3 - int(i)} chances left")
            else:
                print("GET THE FCK OUT OF HERE")
        else:
            run(master_key)

def run(master_key):
    genrate_key()
    key = load_key()
    fer = Fernet(key)
    user_wants = input("Do you want to add a password or view your saved passwords ? (view/add) ").lower()
    if user_wants == "add":
        add_pass(fer)
    elif user_wants == "view":
        view_pass(fer)
    else:
        print("Invalid option")

def view_pass(fer):
    '''
    this block of code is not working
    and I have no more clue in how to
    actually solve it. So I'll just leave it
    here for now, I'll come back on it later 
    in the future.Goodbye
                          ~ the-coder-devil
                            07 Apr 2024 16:37 
    '''

    print("Welcome to Password Manager")
    num = 0
    with open("password.txt",'r') as Souce:
        for line in Souce.readlines():
            num += 1
            username , passw = line.split("|")
            print(f"#{num} Username: {username} Password: {fer.decrypt(passw.encode()).decode()}")

def add_pass(fer):
    print("Welcome to Password Manager")
    user_name = input("Enter your username : ")
    password = input("Enter your Password : ")
    
    with open("password.txt",'a') as Source:
        Source.write(user_name+"|"+fer.encrypt(password.encode()).decode()+"\n")
        print("the details has been added succesfully!")
        print("Enter 'EX' to exit")

def genrate_key():
    key = Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key",'rb')
    key = file.read()
    file.close()
    return key

main()