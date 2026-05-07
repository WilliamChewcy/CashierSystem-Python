def login():
    try:
        with open("Login/Login.txt", "r", encoding="UTF-8") as file:
            login_file = file.readlines()
        count = 0
        while count < 3 :
            user = input("Enter User Name: ").strip()
            password = input("Enter Password: ").strip()
            for login in login_file:
                name = login.strip().split("=")
                user_name = name[0].strip()
                user_password = name[1].strip()

                if user_name == user and user_password == password:
                    return True

            count += 1
            print("Try Again".center(150))

        return False
    except:
        print("Error".center(150))
        return False

def Main():
    try:
        while True:
            if login():
                print(f"{"Login Successfully":^{150}}\n{("-"*25).center(150)}\n{"Welcome to PWP Restaurant":^{150}}")
                # Cashier()
            else:
                print("Login Failed".center(150))
    except:
        print("Error")

if __name__ == "__main__":
    Main()