# 2. The game() function in a program lets a user play a game and returns the score as a
# integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
# previous Hi-score. You need to write a program to update the Hi-score whenever the
# game() function breaks the Hi-score.
# 
import random

def snake_water_gun():
    highscore = score = 0
    try:
        with open("Chapter_09_File_(I-O)/highscore.txt") as f:
            content = f.read().strip()
            highscore = int(content) if content else 0
    except FileNotFoundError:
        highscore = 0
    except ValueError:
        highscore = 0
    while True:
        computer_choice = random.choice(['s','w','g'])
        user_choice = input('''Enter your choice
s: for snake
w: for water
g: for gun
''').lower()
        if user_choice not in ['s','w','g']:
            print("Something Wrong Please Enter valid choice")
            continue
        values = {'s':"snake",'w':"water",'g':"gun"}
        print(f"computer Choice {values[computer_choice]} And Your Choice is {values[user_choice]}")

        if(computer_choice == user_choice): print("Draw")
        elif((computer_choice=='s' and user_choice == 'w') or (computer_choice=='w' and user_choice == 'g')
            or (computer_choice=='g' and user_choice == 's')):
            print("You Loose")
        else:
            print("You Win")
            score += 1

        go = input("you want to continue (y/n)")
        if(go != 'y'):
            print("Thank you for Playing")
            print(f"Your Score {score}")
            if(score > highscore):
                print(f"New Highscore! previous High Score {highscore}")
                with open("Chapter_09_File_(I-O)/highscore.txt",'w') as f:
                    f.write(str(score))
            break
    
    
                
if __name__ == '__main__':
    snake_water_gun()