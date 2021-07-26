
from modules.classes.monster import Monster
from modules.classes.avatar import Avatar
from modules.classes.pick_up import PickUp

from modules.extractors.constants import global_vars
import modules.extractors.avatars as avatar_data
import modules.extractors.monsters as monster_data
import modules.extractors.pick_ups as pick_up_data

import modules.functions.helpers as helpers
import modules.functions.graphics as display_functions
import modules.functions.checks as pick_up_functions

import random
import re


'''
--------------------------------------------------------------------
Code for the adventure game
--------------------------------------------------------------------
'''

def choose_avatar():  
    helpers.reset_display()
    valid_input = False
    while not valid_input:
        user_choice = display_functions.display_avatar_options().lower()
        if re.search('[tlbf]',user_choice):
            valid_input = True
            avatar_obj = get_chosen_avatar_details(user_choice)
            return avatar_obj
        else:
            print(f"\nPlease enter from the following only: t, l, b, f\n")


def get_chosen_avatar_details(user_choice):
    for avatar_obj in global_vars.AVATAR_LIST:
        if avatar_obj.name.lower().startswith(user_choice):
            input(f"\nYou have chosen to be a {avatar_obj.img}\n\
                    \nPress enter to continue\n\
                 ")
            return avatar_obj


def choose_random_monster(avatar):
    monster = random.choice(global_vars.MONSTERS_LIST)
    while monster.name in avatar.monsters_encountered:
        if len(avatar.monsters_encountered) == len(global_vars.MONSTERS_LIST):
            monsters_encountered = [] 
        monster = random.choice(global_vars.MONSTERS_LIST)

    avatar.monsters_encountered.append(monster.name)
    return monster


def react_to_monster(avatar, monster):
    avatar.moved_forward = False
    action = display_functions.display_message_on_monster_approach(monster)
    while  monster.hit_points > 0:
        assign_actions(action,avatar,monster)
        if avatar.HP <= 0 or avatar.moved_forward == True or avatar.quit_game == True:
            break
        if monster.hit_points <= 0:
            avatar.monsters_killed += 1
            avatar.score += 10
            break
        action = display_functions.display_message_on_same_monster_still_lurking(monster)


def assign_actions(action,avatar,monster):
    if action == "1":
        avatar.decide_to_attack(monster)
    elif action == "2":
        avatar.decide_to_view_stats(monster)
    elif action == "3":
       pick_up_functions.display_pick_ups_to_be_used_menu(avatar)
    elif action == "4":
        avatar.decide_to_run_away(monster)
    elif action == "5":
        avatar.quit_game = True


def game_menu():
    avatar = global_vars.AVATAR_LIST[0]   #take a default value for avatar
    user_choice = ''
    while user_choice != '4':
        user_choice = display_functions.display_game_menu()

        if user_choice == '1':
            display_functions.display_game_instructions()
        elif user_choice == '2':
            avatar = choose_avatar()
        elif user_choice == '3':
            display_functions.display_game_route(avatar)
        elif user_choice == '4':
            start_game_journey(avatar)
        else:
            exit_game()
            break
    return True


def start_game_journey(avatar):
    while avatar.moved_forward == True:
        monster = choose_random_monster(avatar)
        react_to_monster(avatar,monster)
        avatar_lost_or_quit = check_if_avatar_lost_or_quit(avatar)
        
        if avatar_lost_or_quit == True:
            break
        
        if avatar.moved_forward == False:
            roll_dice_to_move_forward(avatar)
        
        pick_up_functions.check_if_pick_ups_available(avatar)
        
        if avatar.steps >= global_vars.TOTAL_NO_OF_STEPS_TILL_FINISH:
            display_functions.display_end_of_journey_message(avatar)
            break


def roll_dice_to_move_forward(avatar):
    helpers.reset_display()
    no_of_steps_forward = random.randint(global_vars.MIN_STEPS_WHILE_ROLLING_DICE, global_vars.MAX_STEPS_WHILE_ROLLING_DICE)
    avatar.steps += no_of_steps_forward
    avatar.moved_forward = True
    input(f"You moved {no_of_steps_forward} steps. 🐾\n\
            \nPress enter to continue\n\
         ")


def check_if_avatar_lost_or_quit(avatar):
    if avatar.HP <= 0 or avatar.quit_game == True:
        display_functions.display_incomplete_journey_message(avatar)
        return True
    else:
        return False


def wrong_input():
    print(f"\nPlease enter from the following only: y or n\n")
    return False


def exit_game():
    helpers.reset_display()
    print(f"\nUntil next time, goodbye!")
    return True
    

def load_monster_avatar_and_pick_up_data_into_lists():
    monster_data.get_extract_and_load_monster_data_from_api_to_list()
    avatar_data.load_avatar_data_from_csv_to_list()
    pick_up_data.load_pick_up_data_from_csv_to_list()


def main():
    helpers.reset_display()
    load_monster_avatar_and_pick_up_data_into_lists()
    if len(global_vars.MONSTERS_LIST) == 0:
        print(f"\nThere was a error loading monster data from the API endpoint!")
    else:
        valid_input = False
        while not valid_input:
            user_choice = display_functions.display_start_menu().lower()
            commands = {
                        'y': game_menu,
                        'n': exit_game
                        }
            valid_input = commands.get(user_choice, wrong_input)()


if __name__ == "__main__":
    main()