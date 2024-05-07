import os

class User:
    def __init__(self, username, password, score):
        self.username = username
        self.password = password
        self.score = score

    def load_users(self):
        if self.user_file.exists:
            with open(self,user_file, 'r') as file:
                return file.read()
    
    def 

