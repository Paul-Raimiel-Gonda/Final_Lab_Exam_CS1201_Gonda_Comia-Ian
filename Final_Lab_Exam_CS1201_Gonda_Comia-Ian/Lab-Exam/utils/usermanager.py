from user import User

class UserManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = {}

    def load_users():
        pass

    def save_users():
        pass

    def validate_username():
        pass

    def validate_password():
        pass

    def register(self, username, password):
        while True:
            try:
                if not username:
                    print("Usename cannot be empty")
                    break
                if len(username) < 5:
                    print("Username cannot be less than 4 characters")
                    break
                if len(username) > 5:
                    if len(password) < 8:
                        print("Username cannot be less than 4 characters")
                        break                   
                    if len(password) > 8:
                        print("Sucessfully registered user") 
                        self.user[username] = {"password": password} 
            except ValueError:
                print(f"Invalid input")
            


    def login(self, username, password):  
        while True:
            try:
                if username in self.user:
                    self.user[username] and self.user[username]["password"] == password
                    print("Login Successful")
                
                
            except ValueError:
                print(f"Invalid input")

            

        
         