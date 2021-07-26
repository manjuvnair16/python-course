from modules.extractors.constants import global_vars
import random

'''
----------------------------------------------
Class Definition  (Avatar)
----------------------------------------------
'''

class Avatar:

    def __init__(self, name,img, HP, signature_move='', 
                monsters_killed=0, monsters_encountered=[], 
                pick_ups_collected=[], pick_ups_used=[], 
                steps = 0, moved_forward = True, 
                score = 0, quit_game = False):
        
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

    
    def decide_to_view_stats(self, monster):
        print('\033c')
        input(f"{'STATS'.center(70)}\n\
                \n{'-'*70}\
                \nYou:{self.img.center(24)}{'| Health:'.center(10)}{self.HP}\n\
                \nMonster:{monster.img.center(5)}{monster.name.center(15)}{'| Health:'.center(10)}{monster.hit_points}\n\
                \nPress enter to continue!\n\
                ")
    

    def decide_to_attack(self, monster):
        print('\033c')
        print(f"You decided to attack! 🗡\n")
        self.handle_different_cases_on_attack(monster)
    

    def handle_different_cases_on_attack(self, monster):
        result = random.choice(global_vars.ATTACK_RESULTS)
        if result.lower() == "hit".lower():
            monster.case_hit(self)
            
        elif result.lower() == "miss".lower():
            self.case_miss()

        else:
            self.case_hurt(monster)


    def case_miss(self):
        input(f"Oops, you missed the monster! 😨 \n\
                \nPress enter to continue!\n\
            ")


    def case_hurt(self, monster):
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
    
    
    def decide_to_run_away(self, monster):
        print('\033c')
        print(f"You decided to run away! 🐾 🐾\n")
        self.handle_different_cases_on_trying_to_run_away(monster)


    def handle_different_cases_on_trying_to_run_away(self, monster):
        action = random.choice(global_vars.ESCAPE_RESULTS)
        if action.lower() == "escaped".lower():
            self.case_escaped()
        else:
            self.case_hurt(monster)
            

    def case_escaped(self):
        no_of_steps_forward = random.randint(global_vars.MIN_STEPS_WHILE_ROLLING_DICE , global_vars.MAX_STEPS_WHILE_ROLLING_DICE)
        self.steps += no_of_steps_forward
        self.moved_forward = True
        input(f"You escaped, phew! 😰  You managed to run {no_of_steps_forward} steps away from the monster!\n\
                \nPress enter to continue!\n\
             ")


    def decide_to_use_pick_ups(self, user_choice):
        print('\033c')
        if user_choice > 0:
            pick_up_obj = global_vars.PICK_UP_LIST[user_choice - 1]
            pick_up_obj.action(self)
        else:
            print(f"\nYou decided to not use any pick-ups!\n\
                    \nGoing Back!\n\
                ")

    def add_pick_up_to_used_list(self, pick_up):
        self.pick_ups_used.append(pick_up)

    def add_pick_up_to_collected_list(self, pick_up):
        self.pick_ups_collected.append(pick_up)

