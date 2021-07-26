from modules.extractors.constants import global_vars
from modules.classes.avatar import Avatar

import modules.functions.helpers as helpers
import modules.functions.graphics as display_functions

import re


def display_pick_ups_to_be_used_menu(avatar):
    helpers.reset_display()
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


def accept_user_choice_of_pick_up(avatar):
    valid_input = False
    while not valid_input:
        user_choice,regex_exp = display_list_of_pick_ups_which_can_be_used(avatar)
        valid_input = check_if_user_input_of_pick_up_is_valid(regex_exp,user_choice)
    
    return user_choice


def display_list_of_pick_ups_which_can_be_used(avatar):
    print(f"Select a pick-up to use it now: \n")
    regex_exp = check_if_pick_up_has_been_used_then_display(avatar)  
    print(f"Press 0: To go back \n")
    user_choice = input("\n")
    return user_choice, regex_exp


def check_if_pick_up_has_been_used_then_display(avatar):
    no_of_pick_ups_collected = len(avatar.pick_ups_collected)
    regex_exp = '0'
    for i  in range(no_of_pick_ups_collected):
        if avatar.pick_ups_collected[i].name.lower() not in avatar.pick_ups_used:
            print(f"Press {i+1}: {avatar.pick_ups_collected[i].name} {avatar.pick_ups_collected[i].img}\n")
            regex_exp += str(i+1)
    return regex_exp


def check_if_user_input_of_pick_up_is_valid(regex_exp,user_choice):
    if re.search(rf"[{regex_exp}]",user_choice):
        return True
    else:
        display_regex_exp = ",".join(list(regex_exp))
        print(f"\nPlease enter from the following only: {display_regex_exp}\n")
        return False



def check_if_pick_ups_available(avatar):
    helpers.reset_display()
    no_of_pick_ups_collected = len(avatar.pick_ups_collected)
    if no_of_pick_ups_collected < global_vars.TOTAL_NO_OF_PICK_UPS:
        if avatar.steps >= global_vars.MILESTONES_FOR_PICK_UP_LIST[no_of_pick_ups_collected]:
            latest_pick_up = global_vars.PICK_UP_LIST[no_of_pick_ups_collected]

            update_avatar_details_on_collecting_pick_up(avatar,latest_pick_up)

            display_functions.display_message_on_collecting_pick_up(latest_pick_up)
    

def update_avatar_details_on_collecting_pick_up(avatar,latest_pick_up):
    avatar.add_pick_up_to_collected_list(latest_pick_up)
    avatar.score += 5
