import requests
import random
import re


response = requests.get("https://api.osrsbox.com/monsters")
monsters_api_data = response.json()
MONSTERS_LIST = []

#https://api.osrsbox.com/monsters?where={%20%22duplicate%22:%20false%20}
#MONSTERS = list({monster["name"]: monster for monster in monsters_api_data["_items"]}.values())

for monster in monsters_api_data["_items"]:
    monster_data = {k:v for k,v in monster.items() if k=="name" or k=="hitpoints" or k=="attack_type"}
    duplicate = False
    for element in MONSTERS_LIST:
        if element["name"] == monster_data["name"]:
            duplicate = True
            break

    if duplicate == False:
        MONSTERS_LIST.append(monster_data)



AVATAR_DICT = {
                't': {
                        'img': '🐯' ,
                        'HP' : 110,
                        'signature_move':''
                     },
                'l': {
                        'img': '🦁' ,
                        'HP' : 110,
                        'signature_move':''
                     },
                'b': {
                        'img': '🐻' ,
                        'HP' : 110,
                        'signature_move':''
                     },
                'f': {
                        'img': '🐱' ,
                        'HP' : 110,
                        'signature_move':''
                     } 
              }



GOODIES_LIST = ['⏳ Time Saver - Jump 3 steps forward', '🍯  Magic Potion  - Increase your HP by 30','💰  Treasure  - Increase your score by 20 points']

MILESTONES_FOR_PICK_UPS = [3,9,12]

ATTACK_RESULTS = ['Hit','Miss','Hurt']


def create_divider(num_of_asterix):
    return '*' * num_of_asterix



def display_start_menu():
    return input(f"\n{create_divider(75)}\
                    \n{'✨ 🔥  Play Adventure Game? 🗡 ✨'.center(70)}\n\
                    \n{'Yes: Press y'.center(70)}\
                    \n{' No: Press n'.center(70)}\n\
                    \n{create_divider(75)}\
                ")


def display_game_instructions():
    input(f"\n{'📜  Instructions: 📜'.center(70)}\
            \n{'📕  Game ends when HP decreases to 0'.ljust(70)}\n\
            \n{'📗  Potion helps to increase HP by 30'.ljust(70)}\n\
            \n{'📙  Need to keep moving till the end point to win.'.ljust(70)}\n\
            \n{'📘  Collect as many goodies & kill as many lurking monsters to ⬆  your score.'.ljust(70)}\n\
            \n\n{'Press any key to continue'.ljust(70)}\n\
        ")


def display_avatar_options():
    return input(f"\n\n{'Choose Your Avatar:'.center(40)}\n\
               \n{'🐯'.center(10)}|{'🦁'.center(10)}|{'🐻'.center(10)}|{'🐱'.center(10)}\n\
               \n{'Tiger'.center(10)}|{'Lion'.center(10)}|{'Bear'.center(10)}|{'Fox'.center(10)}\n\
               \n{'Press t'.center(10)}|{'Press l'.center(10)}|{'Press b'.center(10)}|{'Press f'.center(10)}\n\
            ")
    
def display_first_line_route():
    return 'T  ' + '➡'* 3 + '🌳' * 4 + '🐞' + '🌳' * 2 + '➡'* 10 + '⏳' + '➡'* 5 + '🌲' * 4 + '🐊' + '🌲' * 5 + '➡'* 6 +'🌺' * 3 + '➡'* 3 + ' ' * 5 + 'E'

def display_second_line_route():
     return 'A  ' + '➡'* 2 + '🌳' * 4 + '🐍' + '🌳' * 2 + '➡'* 4 + '👽' + '➡'* 6 +'🍯' + '➡'* 5 + '🌴' * 4 + '🐙' + '🌲' * 5 + '➡'* 6 + '👾' + '➡'* 5 + ' ' * 5 + 'N'

def display_third_line_route():
     return 'R  ' + '➡'* 7 + '🌳' * 8 + '🐝 ' + '🌳' * 2 + '➡'* 10 + '👺' + '➡'* 5 + '🌴' * 4 + '🐸' + '🌴' * 5 + '➡'* 2 + '💰' + '➡'* 1 + ' ' * 4 + 'D'

def display_game_route(avatar):
    input(f"\n{'Game Route:'.center(70)}\n\
            \n{'S'.center(13)}\n\
            \n{display_first_line_route().center(70)}\n\
            \n{avatar['img']}{display_second_line_route().center(68)}\n\
            \n{display_third_line_route().center(70)}\n\
            \n{'T'.center(13)}\n\
            \n\n{'Press any key to continue'.ljust(70)}\n\
        ")

def display_menu():
    valid_input = False
    while not valid_input:
        user_choice = input(f"\n Game Menu\
                              \n{'-'*35}\
                              \n Press 1 - How to Play\n\
                              \n Press 2 - Choose an Avatar\n\
                              \n Press 3 - Display Game Route\n\
                              \n Press 4 - Start Game\n\
                              \n Press 5 - Exit game\n\
                              \n{'-'*35}\n\
                            ")
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
            return AVATAR_DICT[user_choice] 
        else:
            print(f"\nPlease enter from the following only: t, l, b, f\n")


def display_action_menu(monster):
    valid_input = False
    while not valid_input:
        user_choice =  input(f"A Monster Spotted! {monster['name']}\nWhat would you like to do?\n\
                               Press 1 - Attack\n\
                               Press 2 - View stats\n\
                               Press 3 - Use goodies\n\
                               Press 4 - Run away/Move forward\n\
                               Press 5 - Exit game\n\
                            ")
        if re.search('[12345]',user_choice):
            valid_input = True
            return user_choice
        else:
            print(f"\nPlease enter from the following only: 1,2,3,4,5\n")


def use_time_saver_gizmo(steps):
    steps += 3
    print(f"\nYou've moved forward 3 steps\n")
    return steps


def use_magic_potion(avatar):
    avatar['HP'] += 30
    print(f"\nYour HP has been increased by 30!\n")
    return avatar


def use_treasure_gizmo(score):
    score += 20
    print(f"\nYour score has been increased by 20!\n")
    return score


def case_monster_hit(monster, avatar):
    print(f"You hit the monster!\n")
    monster['hitpoints'] = monster['hitpoints'] - avatar['HP']
    if monster['hitpoints'] <= 0:
        print(f"Hurray! Monster lost the fight!")
    else:
        print (f"Monster took {avatar['HP']} damage. Remaining health = {monster['hitpoints']}\n")
    return monster


def case_you_got_hit(monster, avatar):
    print(f"Oops, The monster attacked you! You got hurt!\n")
    avatar['HP'] = avatar['HP'] - monster['hitpoints']
    if avatar['HP'] <= 0:
        print(f"You have 0 health! You lost!")
    else:
        print (f"You lost {monster['hitpoints']} health\n")
    return avatar


def attack(monster,avatar,score):
    print(f"You decided to attack!\n")
    result = random.choice(ATTACK_RESULTS)
    #print(result)
    if result == "Hit":
        monster = case_monster_hit(monster,avatar)
        score += 2
    elif result == "Miss":
        print(f"Oops, you missed the monster!\n")
    else:
        avatar = case_you_got_hit(monster,avatar)

    return monster, avatar, score

        
def view_stats(monster,avatar):
    print (f"Your stats: {avatar['img']}  - Health: {avatar['HP']}, Signature Move: {avatar['signature_move']}\n\
            \nMonster stats: {monster['name']} - Health: {monster['hitpoints']}, Attack Type: {monster['attack_type'][0]}\n\
          ")


def use_goodies(steps,goodies_collected, avatar, score,goodies_used):
    moved_forward = False
    
    if len(goodies_collected) == 0:
        print(f"Oops, No gizmos collected yet!\n")
    else:
        valid_input = False
        while not valid_input:
            print(f"Select a Gizmo to use it now: \n")
            for i, item in enumerate(goodies_collected):
                gizmo_to_be_used = False
                if item not in goodies_used:
                    print(f"{item} : To use press {i+1}\n")
                    gizmo_to_be_used = True
            if gizmo_to_be_used == False:
                print(f"Sorry, all gizmos have been used up!\n")
            print(f"To go back : press 0\n")
            user_choice = input("\n")
            if re.search('[0123]',user_choice):
                valid_input = True
            
            else:
                print(f"\nPlease enter from the following only: 0,1,2,3\n")
        user_choice = int(user_choice)
        if user_choice == 1:
            steps = use_time_saver_gizmo(steps)
            goodies_used.append(goodies_collected[user_choice - 1])
            moved_forward = True
        elif user_choice == 2:
            avatar = use_magic_potion(avatar)
            goodies_used.append(goodies_collected[user_choice - 1])
        elif user_choice == 3:
            score = use_treasure_gizmo(score)
            goodies_used.append(goodies_collected[user_choice - 1])
        else:
            if gizmo_to_be_used == True:
                print(f"\nYou decided to not use any pick-ups - Going Back!\n")
            else:
                print(f"\nGoing Back!\n")
    return steps, avatar, score, moved_forward


def move_forward(monster, avatar, steps):
    print(f"You decided to run!\n")
    action = random.randint(0,1)
    if action == 0:
        no_of_steps_forward = random.randint(1,5)
        steps += no_of_steps_forward
        moved_forward = True
        print(f"You escaped, phew!\n")
        print(f"You managed to run {no_of_steps_forward} steps away from the monster!\n")
    else:
        avatar = case_you_got_hit(monster, avatar)
        moved_forward = False
    
    return avatar, steps, moved_forward


def assign_actions(action,monster,avatar,steps,goodies_collected,score,goodies_used):
    moved_forward = False
    quit_game = False
    if action == "1":
        monster, avatar, score = attack(monster,avatar,score)
    if action == "2":
        view_stats(monster,avatar)
    if action == "3":
        steps,avatar,score, moved_forward = use_goodies(steps,goodies_collected,avatar,score,goodies_used)
    if action == "4":
        avatar, steps, moved_forward = move_forward(monster, avatar, steps)
    if action == "5":
        quit_game = True
        #exit_game()

    return monster, avatar, steps, score, moved_forward, quit_game
    

def react_to_monster(monster,avatar,steps,score,goodies_collected,monsters_killed,goodies_used):
    moved_forward = False
    quit_game  = False
    while  monster['hitpoints'] > 0:
            action = display_action_menu(monster)
            monster, avatar, steps, score, moved_forward,quit_game = assign_actions(action,monster,avatar,steps,goodies_collected, score,goodies_used)
            if avatar['HP'] <= 0:
                #exit_game()
                break
            if monster['hitpoints'] <= 0:
                monsters_killed += 1
                score += 10
                break
            if moved_forward == True or quit_game == True:
                break

    return monster, avatar, steps, score, moved_forward,monsters_killed, quit_game



def check_if_pick_ups_available(steps, goodies_collected,score):
    if len(goodies_collected) <= 3:
        if steps >= MILESTONES_FOR_PICK_UPS[len(goodies_collected)]:
            goodies_collected.append(GOODIES_LIST[len(goodies_collected)])
            score += 5
            print(f"Well Done! You've collected a {goodies_collected[len(goodies_collected)-1]}\n")
    
    return score, goodies_collected



def roll_dice_to_move_forward(steps):
    input(f"\nMove forward - \n\
            \nTread slowly!\
            \nPay attention to the tangled vines, lest they gobble you!\
            \nRoll a dice to move forward that many steps.\
            \nPress any key to roll now:\n\
         ")
    no_of_steps_forward = random.randint(1,6)
    steps += no_of_steps_forward
    print(f"\nYou moved {no_of_steps_forward} steps.\n")
    moved_forward = True
    return steps, moved_forward



def end_of_journey(monsters_killed, score, goodies_collected):
    print(f"Hurrah! You've made it through the maze of monsters!\n\
            \nYour score is {score}\n\
            \nYou slayed {monsters_killed} monsters\n\
            \nYou collected {len(goodies_collected)} items\n\
        ")
    if monsters_killed <= 2:
        print(f"Lucky to be alive!")
    elif monsters_killed > 2 and monsters_killed <= 5:
        print(f"On your way to being a warrior!")    #change the phrase
    elif monsters_killed > 5:
        print(f"Brave Warrior, our Salutations!")



def play_game():
    avatar = AVATAR_DICT['t']
    user_choice = '0'
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
    goodies_collected = []
    goodies_used = []
    monsters_encountered = []
    monsters_killed = 0
    score = 0
    steps = 0
    moved_forward = True
    while moved_forward == True:
        monster = random.choice(MONSTERS_LIST)
        while monster['name'] in monsters_encountered:
           monster = random.choice(MONSTERS_LIST)
        
        monsters_encountered.append(monster['name'])
    
        moved_forward = False
        monster, avatar, steps, score, moved_forward,monsters_killed,quit_game = react_to_monster(monster,avatar,steps,score,goodies_collected,monsters_killed,goodies_used)
        
        if avatar['HP'] <= 0 or quit_game == True:
            print(f"\nYour score is {score}\n\
                    \nYou killed {monsters_killed} monsters\n\
                    \nYou collected {len(goodies_collected)} items\n\
                 ")
            exit_game()
            break

        if moved_forward == True:
            score, goodies_collected = check_if_pick_ups_available(steps, goodies_collected,score)
        else:
            steps, moved_forward = roll_dice_to_move_forward(steps)
            score, goodies_collected = check_if_pick_ups_available(steps, goodies_collected,score)

        if steps >= 15:
            end_of_journey(monsters_killed, score, goodies_collected)
            break
    
    return True


def exit_game():
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