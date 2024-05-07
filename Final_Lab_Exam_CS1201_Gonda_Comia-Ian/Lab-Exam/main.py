from utils.usermanager import UserManager

class Main:
    def __init__(self):
     self.usermanager = UserManager

    def main(self):
        while True:
            print("""
                Welcome to DICE GAME
                1. User Sign up
                2. User Log in
                3. Exit
            """)
            choice = int(input("Enter choice: "))
            if choice == 1:
                username = input("Enter Username")
                password = input("Enter your password")
                self.usermanager.register(self, username, password)
                
            elif choice == 2:
                username = input("Input your username")
                password = input("Input your password")
                username = self.usermanager.login(self, username, password)
            elif choice == 3:
                exit()
            else:
                print("Invalid choice, try again")

if __name__ == "__main__":
    user = Main()
    user.main()

