import requests
import csv
import random
import re

class Monster:

    def __init__(self, img, name, description, hit_points, attack_style):
        self.img = img
        self.name = name
        self.description = description
        self.hit_points = hit_points
        self.attack_style = attack_style

    def case_hit(self,avatar):
        print('\033c')
        print(f"You hit the monster! 👊  ✨ \n")
        self.hit_points = self.hit_points - avatar.HP
        if self.hit_points <= 0:
            input(f"Bravo! Monster Slayed! ✨\n\
                    \nPress enter to roll a dice & move forward that many steps!  🎲  🐾 \n\
                ")
        else:
            input (f"✨  Monster took {avatar.HP} damage. Remaining health = {self.hit_points}! Need another blow to be slayed! \n\
                    \nPress enter to continue!\n\
                ")
      

response = requests.get('https://api.osrsbox.com/monsters?where={"duplicate":false}')
monsters_api_data = response.json()
monster_images = ['👾','👻','👹','🎃','👣 👣','👺','💀','☠ 💀','👻','🦀','👀 🐕','👿 🐺','👽 🐺','👿 👽 🐺']
MONSTERS_LIST = []
i = 0
for monster_item in monsters_api_data["_items"]:
    monster_data = {k:v for k,v in monster_item.items() if k=="name" or k=="hitpoints" or k=="attack_type" or k=="examine"}
    duplicate = False
    
    for element in MONSTERS_LIST:
        if element.name == monster_data["name"]:
            duplicate = True
            break

    if duplicate == False:
        index_of_images = i % 14
        monster_details = Monster(monster_images[index_of_images], monster_data["name"],monster_data["examine"],monster_data["hitpoints"],monster_data["attack_type"])
        MONSTERS_LIST.append(monster_details)
        i += 1



class Avatar:
    def __init__(self, name,img, HP, signature_move='', steps = 0, monsters_killed=0, monsters_encountered=[], pick_ups_collected=[], pick_ups_used=[], moved_forward = True, score = 0, quit_game = False):
        self.name = name
        self.img = img
        self.HP = HP
        self.signature_move = signature_move
        self.monsters_killed = monsters_killed
        self.monsters_encountered = monsters_encountered
        self.pick_ups_collected = pick_ups_collected
        self.pick_ups_used = pick_ups_used
        self.moved_forward = moved_forward
        self.score = score
        self.quit_game = quit_game
        self.steps = steps

    
    def decide_to_view_stats(self,monster):
        print('\033c')
        input(f"{'STATS'.center(70)}\n\
                \n{'-'*70}\
                \nYou:{self.img.center(24)}{'| Health:'.center(10)}{self.HP}\n\
                \nMonster:{monster.img.center(5)}{monster.name.center(15)}{'| Health:'.center(10)}{monster.hit_points}\n\
                \nPress enter to continue!\n\
                ")
    

    def decide_to_attack(self,monster):
        print('\033c')
        print(f"You decided to attack! 🗡\n")
        result = random.choice(ATTACK_RESULTS)
        if result == "Hit":
            monster.case_hit(self)
            self.score += 2
        elif result == "Miss":
            input(f"Oops, you missed the monster! 😨 \n\
            \nPress enter to continue!\n\
            ")
        else:
            self.case_hurt(monster)


    def decide_to_run(self,monster):
        print('\033c')
        print(f"You decided to run! 🐾 🐾\n")
        action = random.randint(0,1)
        if action == 0:
            no_of_steps_forward = random.randint(1,5)
            self.steps += no_of_steps_forward
            self.moved_forward = True
            input(f"You escaped, phew! 😰  You managed to run {no_of_steps_forward} steps away from the monster!\n\
                    \nPress enter to continue!\n\
                ")
        else:
            self.case_hurt(monster)
            self.moved_forward = False


    def decide_to_use_pick_ups(self,user_choice):
        print('\033c')
        if user_choice > 0:
            pick_up_obj = PICK_UP_LIST[user_choice - 1]
            pick_up_obj.action(self)
        else:
            print(f"\nYou decided to not use any pick-ups!\n\
                    \nGoing Back!\n\
                ")


    def case_hurt(self,monster):
        print('\033c')
        print(f"Oops, The monster attacked you! You got hurt! 🤕 \n")
            
        self.HP = self.HP - monster.hit_points
        if self.HP <= 0:
            input(f"You have 0 health! You lost!  👎\n\
                \nPress enter to continue!\n\
                ")
        else:
            input(f"You lost {monster.hit_points} health points 😰\n\
            \nPress enter to continue!\n\
            ")

    
AVATAR_LIST = []
with open('avatar_data.csv','r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader, "")                 
    for row in csv_reader:
        AVATAR_LIST.append(Avatar(row[0],row[1],int(row[2]),row[3]))



class PickUp:
    def __init__(self,name,img,description):
        self.name = name
        self.img = img
        self.description = description


    def action(self,avatar):
        if self.name.lower().startswith("time saver"):
           avatar.steps += 3
           input(f"\nYou've moved forward 3 steps 🐾 \n\
                    \nPress enter to continue!\n\
                ")
           avatar.moved_forward = True
           
        elif self.name.lower().startswith("magic potion"):
            avatar.HP += 30
            input(f"\nYour health has been increased by 30! 💚\n\
                    \nPress enter to continue!\n\
                ")
            
        elif self.name.lower().startswith("treasure"):
            avatar.score +=20
            input(f"\nYour score has been increased by 20!\n\
                    \nPress enter to continue!\n\
                ")
            
        avatar.pick_ups_used.append(self.name.lower())


PICK_UP_LIST = []
with open('pick_up_data.csv','r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader, "")    
    for row in csv_reader:
        PICK_UP_LIST.append(PickUp(row[0],row[1],row[2]))



MILESTONES_FOR_PICK_UP = {
                            'first_pick_up_after' : 5,
                            'second_pick_up_after': 10
                            #'third_pick_up_after' : 12
                          }

MILESTONES_FOR_PICK_UP_LIST = list(MILESTONES_FOR_PICK_UP.values())


ATTACK_RESULTS = ['Hit','Miss','Hurt']



def create_divider(num_of_asterix):
    return '*' * num_of_asterix


def display_start_menu():
    print('\033c')
    return input(f"\n{create_divider(75)}\
                    \n{'✨ 🔥  Play Adventure Game? 🗡 ✨'.center(70)}\n\
                    \n{'Yes: Press y'.center(70)}\
                    \n{' No: Press n'.center(70)}\n\
                    \n{create_divider(75)}\
                \n")


def display_game_instructions():
    print('\033c')
    input(f"\n{'📜  Instructions: 📜'.center(70)}\
            \n{'-'*75}\
            \n{'📕  Game ends when health decreases to 0'.ljust(70)}\n\
            \n{'📗  Magic Potion helps to increase health by 30'.ljust(70)}\n\
            \n{'📙  Need to reach the end point to complete any level.'.ljust(70)}\n\
            \n{'📘  Collect pick-ups, hit & slay as many lurking monsters to ⬆  your score.'.ljust(70)}\n\
            \n\n{'Press enter to continue'.ljust(70)}\n\
        \n")


def display_avatar_options():
    print('\033c')
    return input(f"\n\n{'Choose Your Avatar:'.center(40)}\n\
               \n{'🐯'.center(10)}|{'🦁'.center(10)}|{'🐻'.center(10)}|{'🐱'.center(10)}\n\
               \n{'Tiger'.center(10)}|{'Lion'.center(10)}|{'Bear'.center(10)}|{'Fox'.center(10)}\n\
               \n{'Press t'.center(10)}|{'Press l'.center(10)}|{'Press b'.center(10)}|{'Press f'.center(10)}\n\
            \n")


def display_first_line_route():
    path1 = '➡'* 2 + '🌳' + '🐞' + '🌳' + ' ' + '➡' + '✨' +'⏳' + '✨' + ' ' + '~'* 5 + '🌲' * 4 + '🐊' + '🌲' * 5 + ' ' + '➡'* 6 +'🌺' * 2 + '🌋'+ '🌺' + ' ' + '➡'* 3 + '👿' + ' ' + '➡' * 2 + '🌳'* 4 + '💩' + '🌳'* 3 + ' ' + '➡'* 5 + ' ' 
    return path1

def display_second_line_route():
    path2 = '➡'* 2 + '🌳' * 4 + '🐍' + '🌳' * 2 + ' '+ '➡'* 4 + '👽' + ' ' + '➡'* 5 + '🌳' + '🦀' + '🌳' + ' ' + '✨' + '🍯' + '✨' + ' ' + '➡'* 5 + '🌴' * 4 + '🐙' + '🌲' * 5 +  ' ' + '~'* 5 + '👾' + ' ' + '➡'* 3 + '🌋' + ' ' + '➡'* 2 + ' '
    return path2

def display_third_line_route():
    path3 = '➡'* 7 + '🌳' * 3 + '🌹' * 2 + '🌳' * 2 + '🐝' + '🌳' * 2 + ' ' + '~'* 10 + '👺' + ' ' + '➡'* 3 + '🌲' * 4 + '👀' + '🎋' + '🌲' + ' ' + '➡' + '✨' + '💰' + '✨' + ' ' + '➡' + '🌲' * 2 + '🌸' * 3 + '🐸' + '🌺' * 2 + ' ' + '➡'* 3  + ' '
    return path3


def display_game_route(avatar):
    print('\033c')
    input(f"\n{'Game Route:'.center(70)}\
            \n{'~'*70}\
            \n   S\n\
            \n   T{display_first_line_route()} E\n\
            \n{avatar.img}  A{display_second_line_route()} N\n\
            \n   R{display_third_line_route()} D\n\
            \n   T\n\
            \n\n{'Press enter to continue'.ljust(70)}\n\
        \n")
   
    
def display_menu():
    print('\033c')
    valid_input = False
    while not valid_input:
        user_choice = input(f"\n 🎮  Game Menu  📜\
                              \n{'-'*70}\
                              \n Press 1 - How to Play ⁈\n\
                              \n Press 2 - Choose an Avatar 🐯  🐻  🦁  🐱\n\
                              \n Press 3 - Display Game Route 🗺 \n\
                              \n Press 4 - Start Game  👍\n\
                              \n Press 5 - Exit game  👎\n\
                              \n{'-'*70}\n\
                            \n")
        if re.search('[12345]',user_choice):
            valid_input = True
            return user_choice
        else:
            print(f"\nPlease enter from the following only: 1,2,3,4,5\n")


def choose_avatar():  
    valid_input = False
    while not valid_input:
        user_choice = display_avatar_options().lower()
        if re.search('[tlbf]',user_choice):
            valid_input = True
            for avatar_obj in AVATAR_LIST:
                if avatar_obj.name.lower().startswith(user_choice):
                    input(f"\nYou have chosen to be a {avatar_obj.img}\n\
                            \nPress enter to continue\n\
                        ")
                    return avatar_obj
        else:
            print(f"\nPlease enter from the following only: t, l, b, f\n")


def display_action_menu(monster):
    print('\033c')
    input(f"\nMonster Approaching Grrr!\n\
                \n {monster.img}  {monster.name} - {monster.description}\n\
                \n{'-'*70}\n\
                \nWhat would you like to do?\n\
                \nPress enter to continue\n\
            ")
    valid_input = False
    while not valid_input:
        user_choice =  input(f"\nPress 1 - Attack  🗡 \n\
                               \nPress 2 - View stats  🖥 \n\
                               \nPress 3 - Use pick ups 🎁 \n\
                               \nPress 4 - Run away/Move forward 👣 \n\
                               \nPress 5 - Exit game  👋 \n\
                            \n")
        if re.search('[12345]',user_choice):
            valid_input = True
            return user_choice
        else:
            print(f"\nPlease enter from the following only: 1,2,3,4,5\n")


def display_repeat_action_menu(monster):
    print('\033c')
    valid_input = False
    while not valid_input:
        print(f"\n{monster.img}  {monster.name} Turning Nasty! groWWRR! 👿 😡 👿 \
                \n{'-'*70}\
                \nWhat would you like to do next?\n\
             ")
        user_choice =  input(f"\nPress 1 - Attack  🗡 \n\
                               \nPress 2 - View stats  🖥 \n\
                               \nPress 3 - Use pick ups 🎁 \n\
                               \nPress 4 - Run away/Move forward 👣 \n\
                               \nPress 5 - Exit game  👋 \n\
                               \n")
        if re.search('[12345]',user_choice):
            valid_input = True
            return user_choice
        else:
            print(f"\nPlease enter from the following only: 1,2,3,4,5\n")


def display_incomplete_journey_message(avatar):
    print('\033c')
    print(f"{'Journey Incomplete! '.center(20)}\
          \n{'Score: '.ljust(20)}{avatar.score}\
          \n{'Monsters Killed: '.ljust(20)}{avatar.monsters_killed}\
          \n{'Pick-Ups collected: '.ljust(20)}{len(avatar.pick_ups_collected)}\n\
         ")


def accept_user_choice_of_pick_up(avatar):
    valid_input = False
    regex_exp = '0'
    no_of_pick_ups_collected = len(avatar.pick_ups_collected)
    while not valid_input:
        print(f"Select a pick-up to use it now: \n")
        for i  in range(no_of_pick_ups_collected):
            if avatar.pick_ups_collected[i].name.lower() not in avatar.pick_ups_used:
                print(f"{avatar.pick_ups_collected[i].name} : To use press {i+1}\n")
                regex_exp += str(i+1)
                
        print(f"To go back : press 0\n")
        user_choice = input("\n")
        if re.search(rf"[{regex_exp}]",user_choice):
            valid_input = True
        else:
            display_regex_exp = ",".join(list(regex_exp))
            print(f"\nPlease enter from the following only: {display_regex_exp}\n")

    return user_choice


def display_pick_ups_to_be_used_menu(avatar):
    print('\033c')
    no_of_pick_ups_collected = len(avatar.pick_ups_collected)
    if no_of_pick_ups_collected == 0:
        input(f"Oops! No pick-ups collected yet!\n\
                \nPress enter to go Back!\n\
            ")
    elif len(avatar.pick_ups_collected) == len(avatar.pick_ups_used):
        input(f"Gosh! All pick-ups have been used up!\n\
                \nPress enter to go Back!\n\
            ")
    else:
        user_choice = int(accept_user_choice_of_pick_up(avatar))
        avatar.decide_to_use_pick_ups(user_choice)
                

def assign_actions(action,avatar,monster):
    if action == "1":
        avatar.decide_to_attack(monster)
    if action == "2":
        avatar.decide_to_view_stats(monster)
    if action == "3":
       display_pick_ups_to_be_used_menu(avatar)
    if action == "4":
        avatar.decide_to_run(monster)
    if action == "5":
        avatar.quit_game = True
    

def react_to_monster(avatar, monster):
    action = display_action_menu(monster)
    while  monster.hit_points > 0:
        assign_actions(action,avatar,monster)
        if avatar.HP <= 0 or avatar.moved_forward == True or avatar.quit_game == True:
            break
        if monster.hit_points <= 0:
            avatar.monsters_killed += 1
            avatar.score += 10
            break
        action = display_repeat_action_menu(monster)


def check_if_pick_ups_available(avatar):
    print('\033c')
    no_of_pick_ups_collected = len(avatar.pick_ups_collected)
    if no_of_pick_ups_collected < 2:
        if avatar.steps >= MILESTONES_FOR_PICK_UP_LIST[no_of_pick_ups_collected]:
            latest_pick_up = PICK_UP_LIST[no_of_pick_ups_collected]
            avatar.pick_ups_collected.append(latest_pick_up)
            avatar.score += 5
            input(f"Well Done! You've collected a {latest_pick_up.img}  {latest_pick_up.name}\n\
                   \n✨ When used will help to - {latest_pick_up.description} ✨\n\
                   \nPress enter to continue\n\
                 ")
    
 
def roll_dice_to_move_forward(avatar):
    print('\033c')
    no_of_steps_forward = random.randint(1,6)
    avatar.steps += no_of_steps_forward
    avatar.moved_forward = True
    input(f"You moved {no_of_steps_forward} steps. 🐾\n\
            \nPress enter to continue\n\
         ")
    
   
def end_of_journey(avatar):
    print('\033c')
    print(f"✨  Hurrah! ✨  You've made it through the maze of monsters!  🎇 \n\
            \n{'Score:'.ljust(20)} {avatar.score}  ✨\n\
            \n{'Monsters Slayed:'.ljust(20)} {avatar.monsters_killed}  🗡\n\
            \n{'Pick-Ups Collected:'.ljust(20)} {len(avatar.pick_ups_collected)}  🎁\n\
        ")
    if avatar.monsters_killed == 1:
        print(f"\nLevel 1: Lucky to be alive!  😰\n")
    elif avatar.monsters_killed == 2 and avatar.monsters_killed <= 4:
        print(f"\nLevel 2: Future awaits you! 😎\n")
    elif avatar.monsters_killed > 2:
        print(f"\nLevel 3: Brave Warrior, Salutations! 🙇\n")


def choose_random_monster(avatar):
    monster = random.choice(MONSTERS_LIST)
    while monster.name in avatar.monsters_encountered:
        if len(avatar.monsters_encountered) == len(MONSTERS_LIST):
            monsters_encountered = [] 
        monster = random.choice(MONSTERS_LIST)
    
    return monster


def play_game():
    avatar = AVATAR_LIST[0]
    user_choice = ''
    while user_choice != '4':
        user_choice = display_menu()
        if user_choice == '1':
            display_game_instructions()
        elif user_choice == '2':
            avatar = choose_avatar()
        elif user_choice == '3':
            display_game_route(avatar)
        elif user_choice == '4':
            start_game(avatar)
        else:
            exit_game()
            break
    return True


def start_game(avatar):
    while avatar.moved_forward == True:
        monster = choose_random_monster(avatar)
        avatar.monsters_encountered.append(monster.name)
        avatar.moved_forward = False
        react_to_monster(avatar,monster)
        
        if avatar.HP <= 0 or avatar.quit_game == True:
            display_incomplete_journey_message(avatar)
            break
        
        if avatar.moved_forward == False:
            roll_dice_to_move_forward(avatar)
        check_if_pick_ups_available(avatar)

        if avatar.steps >= 12:
            end_of_journey(avatar)
            break
    

def exit_game():
    print('\033c')
    print(f"\nUntil next time, goodbye!")
    return True
    

def wrong_input():
    print(f"\nPlease enter from the following only: y or n\n")
    return False
   

def main():
    valid_input = False
    while not valid_input:
        user_choice = display_start_menu().lower()
        commands = {
                    'y': play_game,
                    'n': exit_game
                   }
        valid_input = commands.get(user_choice,wrong_input)()


if __name__ == "__main__":
    main()