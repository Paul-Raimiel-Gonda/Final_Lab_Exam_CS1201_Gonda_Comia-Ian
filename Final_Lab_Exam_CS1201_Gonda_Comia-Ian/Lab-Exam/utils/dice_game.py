from utils.user import user
import random
import os

class DiceGame:
    def __init__(self):
        pass

    def load_scores():
        pass

    def save_scores():
        pass

    def play_game(self, User):
        score = 0

        stages = 3

        won = 0

        game = True
        while game:
            User = random.randint(1, 6)
            cpunum = random.randint(1,6)

            if usernum > cpunum:
                print(f"{user} Won")
                stages -= 1
                score += 1
                if stages == 0
                    game = False
                else:
                    continue   
            elif usernum < cpunum:
                print(f"{user} Lost")
                stages -= 1
                if stages == 0
                    game = False  
                else:
                    continue             
            elif usernum == cpunum:
                print("Draw")
                stages -= 1
                if stages == 0
                    game = False  
                else:
                    continue  

        if won > 2:
            score += 3

        print(f"User Score: {score}") 


    def show_top_scores():
        pass

    def logout():
        pass

    def menu():
        while True:

