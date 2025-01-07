import random

def snake_water_gun():
    computer_choice = random.choice(['s','w','g'])
    user_choice = input('''Enter your choice
s: for snake
w: for water
g: for gun
''').lower()
    if user_choice not in (['s','w','g']):
        print("Something Wrong Please Enter valid choice")
        return
    values = {'s':"snake",'w':"water",'g':"gun"}
    print(f"computer Choice {values[computer_choice]} And Your Choice is {values[user_choice]}")

    if(computer_choice == user_choice): print("Draw")
    elif((computer_choice=='s' and user_choice == 'w') or (computer_choice=='w' and user_choice == 'g')
         or (computer_choice=='g' and user_choice == 's')):
        print("You Loose")
    else:
        print("You Win")
            
if __name__ == '__main__':
    snake_water_gun()