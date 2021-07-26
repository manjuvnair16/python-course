from modules.extractors.constants import global_vars
import modules.functions.helpers as helpers
import re


def display_start_menu():
    return input(f"\n{helpers.create_divider('*', 75)}\
                    \n{'✨ 🔥  Play Adventure Game? 🗡 ✨'.center(70)}\n\
                    \n{'Yes: Press y'.center(70)}\
                    \n{' No: Press n'.center(70)}\n\
                    \n{helpers.create_divider('*', 75)}\
                \n")


def display_game_menu():
    helpers.reset_display()
    valid_input = False
    while not valid_input:
        user_choice = input(f"\n 🎮  Game Menu  📜\
                              \n{helpers.create_divider('-', 70)}\
                              \n Press 1 - How to Play ⁈\n\
                              \n Press 2 - Choose an Avatar 🐯  🐻  🦁  🐱\n\
                              \n Press 3 - Display Game Route 🗺 \n\
                              \n Press 4 - Start Game  👍\n\
                              \n Press 5 - Exit game  👎\n\
                              \n{helpers.create_divider('-', 70)}\n\
                            \n")
        if re.search('[12345]',user_choice):
            valid_input = True
            return user_choice
        else:
            print(f"\nPlease enter from the following only: 1,2,3,4,5\n")


def display_game_instructions():
    helpers.reset_display()
    input(f"\n{'📜  Instructions: 📜'.center(70)}\
            \n{helpers.create_divider('-', 75)}\
            \n{'📕  Game ends when your health decreases to 0'.ljust(70)}\n\
            \n{'📗  Magic Potion helps to increase your health by 30'.ljust(70)}\n\
            \n{'📙  Need to move till the end point to complete any level.'.ljust(70)}\n\
            \n{'📘  Collect pick-ups, hit & slay as many lurking monsters to ⬆ your score.'.ljust(70)}\n\
            \n\n{'Press enter to continue'.ljust(70)}\n\
        \n")


def display_first_line_of_game_route():
    path1 = '➡'* 2 + '🌳' + '🐞' + '🌳' + ' ' + '➡' + '✨' +'⏳' + '✨' + ' ' + '~'* 5 + '🌲' * 4 + '🐊' + '🌲' * 5 + ' ' + '➡'* 6 +'🌺' * 2 + '🌋'+ '🌺' + ' ' + '➡'* 3 + '👿' + ' ' + '➡' * 2 + '🌳'* 4 + '💩' + '🌳'* 3 + ' ' + '➡'* 5 + ' ' 
    return path1

def display_second_line_of_game_route():
    path2 = '➡'* 2 + '🌳' * 4 + '🐍' + '🌳' * 2 + ' '+ '➡'* 4 + '👽' + ' ' + '➡'* 5 + '🌳' + '🦀' + '🌳' + ' ' + '✨' + '🍯' + '✨' + ' ' + '➡'* 5 + '🌴' * 4 + '🐙' + '🌲' * 5 +  ' ' + '~'* 5 + '👾' + ' ' + '➡'* 3 + '🌋' + ' ' + '➡'* 2 + ' '
    return path2

def display_third_line_of_game_route():
    path3 = '➡'* 7 + '🌳' * 3 + '🌹' * 2 + '🌳' * 2 + '🐝' + '🌳' * 2 + ' ' + '~'* 10 + '👺' + ' ' + '➡'* 3 + '🌲' * 4 + '👀' + '🎋' + '🌲' + ' ' + '➡' + '✨' + '💰' + '✨' + ' ' + '➡' + '🌲' * 2 + '🌸' * 3 + '🐸' + '🌺' * 2 + ' ' + '➡'* 3  + ' '
    return path3


def display_game_route(avatar):
    helpers.reset_display()
    input(f"\n{'Game Route:'.center(70)}\
            \n{helpers.create_divider('~', 70)}\
            \n   S\n\
            \n   T{display_first_line_of_game_route()} E\n\
            \n{avatar.img}  A{display_second_line_of_game_route()} N\n\
            \n   R{display_third_line_of_game_route()} D\n\
            \n   T\n\
            \n\n{'Press enter to continue'.ljust(70)}\n\
        \n")
   
    
def display_avatar_options():
    return input(f"\n\n{'Choose Your Avatar:'.center(40)}\n\
               \n{'🐯'.center(10)}|{'🦁'.center(10)}|{'🐻'.center(10)}|{'🐱'.center(10)}\n\
               \n{'Tiger'.center(10)}|{'Lion'.center(10)}|{'Bear'.center(10)}|{'Fox'.center(10)}\n\
               \n{'Press t'.center(10)}|{'Press l'.center(10)}|{'Press b'.center(10)}|{'Press f'.center(10)}\n\
            \n")


def display_message_on_monster_approach(monster):
    helpers.reset_display()
    input(f"\nMonster Approaching Grrr!\n\
                \n {monster.img}  {monster.name} - {monster.description}\n\
                \n{helpers.create_divider('-', 70)}\n\
                \nWhat would you like to do?\n\
                \nPress enter to continue\n\
            ")
    user_choice = display_and_accept_user_action_on_monster_approach(monster)
    return user_choice


def display_message_on_same_monster_still_lurking(monster):
    helpers.reset_display()
    print(f"\n{monster.img}  {monster.name} still around!!  It's Turning Nasty! groWWRR! 👿 😡 👿 \
                \n{helpers.create_divider('-', 70)}\
                \nWhat would you like to do next?\n\
                \nPress enter to continue\n\
            ")
    user_choice = display_and_accept_user_action_on_monster_approach(monster)
    return user_choice


def display_message_on_collecting_pick_up(latest_pick_up):
    input(f"Well Done! You've collected a {latest_pick_up.img}  {latest_pick_up.name}\n\
            \n✨ When used will help to - {latest_pick_up.description} ✨\n\
            \nPress enter to continue\n\
         ")


def display_incomplete_journey_message(avatar):
    helpers.reset_display()
    print(f"{'Journey Incomplete! 👎'.center(20)}\
          \n{'Score: '.ljust(20)}{avatar.score}\
          \n{'Monsters Killed: '.ljust(20)}{avatar.monsters_killed}\
          \n{'Pick-Ups collected: '.ljust(20)}{len(avatar.pick_ups_collected)}\n\
         ")      


def display_end_of_journey_message(avatar):
    helpers.reset_display()
    print(f"✨  Hurrah! You've made it through the maze of monsters!  🎇 \n\
            \n{'Score:'.ljust(20)} {avatar.score}  ✨\n\
            \n{'Monsters Slayed:'.ljust(20)} {avatar.monsters_killed}  🗡\n\
            \n{'Pick-Ups Collected:'.ljust(20)} {len(avatar.pick_ups_collected)}  🎁\n\
        ")

    if avatar.monsters_killed <= global_vars.NO_OF_MONSTERS_TO_BE_KILLED_MAX_FOR_LEVEL_ONE:
        print(f"\nLevel 1: Lucky to be alive!  😰\n")
    elif avatar.monsters_killed <= global_vars.NO_OF_MONSTERS_TO_BE_KILLED_MAX_FOR_LEVEL_TWO:
        print(f"\nLevel 2: Future awaits you! 😎\n") 
    elif avatar.monsters_killed >= global_vars.NO_OF_MONSTERS_TO_BE_KILLED_MIN_FOR_LEVEL_THREE:
        print(f"\nLevel 3: Brave Warrior, Salutations! 🙇\n")


def display_and_accept_user_action_on_monster_approach(monster):
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


