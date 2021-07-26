'''
----------------------------------------------
Class Definition (Monster)
----------------------------------------------
'''

class Monster:

    def __init__(self, img, name, description, hit_points, attack_style):
        self.img = img
        self.name = name
        self.description = description
        self.hit_points = hit_points
        self.attack_style = attack_style

    def case_hit(self,avatar):
        self.hit_points = self.hit_points - avatar.HP
        avatar.score += 2
        self.display_got_hit_message(avatar)

    def display_got_hit_message(self,avatar):
        print('\033c')
        print(f"You hit the monster! 👊  ✨ \n")
        self.display_message_if_monster_slayed_or_just_hurt(avatar)
        
    def display_message_if_monster_slayed_or_just_hurt(self,avatar):
        if self.hit_points <= 0:
            input(f"Bravo! Monster Slayed! ✨\n\
                    \nPress enter to roll a dice & move forward that many steps!  🎲  🐾 \n\
                ")
        else:
            input(f"✨ Monster took {avatar.HP} damage. Remaining health = {self.hit_points}! Need another blow to be slayed! \n\
                    \nPress enter to continue!\n\
                ") 