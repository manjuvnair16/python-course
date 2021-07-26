'''
----------------------------------------------
Class Definition  (PickUp)
----------------------------------------------
'''


class PickUp:

    def __init__(self, name, img, description):
        self.name = name
        self.img = img
        self.description = description


    def action(self, avatar):
        if self.name.lower().startswith("time saver"):
           self.__handle_time_saver(avatar)
           
        elif self.name.lower().startswith("magic potion"):
            self.__handle_magic_potion(avatar)
            
        elif self.name.lower().startswith("treasure"):
            self.__handle_treasure(avatar)

        self.__add_pick_up_to_used_list(avatar)   
        

    def __handle_time_saver(self, avatar):
        avatar.steps += 3
        avatar.moved_forward = True
        input(f"\nYou've moved forward 3 steps 🐾 \n\
                \nPress enter to continue!\n\
             ")
           
    
    def __handle_magic_potion(self, avatar):
        avatar.HP += 30
        input(f"\nYour health has been increased by 30! 💚\n\
                \nPress enter to continue!\n\
            ")
    

    def __handle_treasure(self, avatar):
        avatar.score +=20
        input(f"\nYour score has been increased by 20!\n\
                \nPress enter to continue!\n\
             ")


    def __add_pick_up_to_used_list(self, avatar):
        avatar.add_pick_up_to_used_list(self.name.lower())

