from cryptography.fernet import Fernet

def main():
    print("Welcome to Password Manager")
    user = input("Do you want to add password or view saved ones: ").lower().strip()
    if user == "add":
        user_name = input("Enter your username : ")
        password = input("Enter your Password : ")
        add_pass(user_name,password)
    elif user == "view":
        user_name = input("Enter your username : ")
        view_pass(user_name)
    else:
        print('Enter valid option!')

def view_pass(user_name: str):
    num = 0
    with open("password.txt",'r') as Souce:
        for line in Souce.readlines():
            num += 1
            if line.startswith(user_name):
                _, passw,key = line.split("|")
                fernet = Fernet(key)
                print(f"#{num} Username: {user_name} Password: {fernet.decrypt(passw).decode()}")

def add_pass(user_name: str, password:str):
    
    with open("password.txt",'a') as Source:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        Source.write(user_name + "|" + fernet.encrypt(password.encode()).decode()+ "|" + key.decode() + "\n")
        print("the details has been added succesfully!")

main()