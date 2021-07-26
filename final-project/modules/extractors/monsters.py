from modules.extractors.constants import global_vars
from modules.classes.monster import Monster
import requests

'''
--------------------------------------------------------------------
Get, extract and load monster data into list from an api
--------------------------------------------------------------------
'''

def get_extract_and_load_monster_data_from_api_to_list():
    """
    Gets data from API endpoint, extracts useful data, filters out records with duplicate monster names & loads into MONSTER_LIST
    """
    
    duplicate = False
    monsters_api_data = get_monster_data_from_api_endpoint()
    if monsters_api_data != False:
        for monster_item in monsters_api_data:
            monster_data = extract_required_key_value_pair_from_monster_api_data(monster_item)
            duplicate = check_for_duplicate_monster_names(monster_data)
            if duplicate == False:
                load_monster_data_into_list_with_image(monster_data)
    

def get_monster_data_from_api_endpoint():
    response = requests.get('https://api.osrsbox.com/monsters?where={"duplicate":false}')
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        print ("Error: " + str(e))
        return False
    
    # Must have been a 200 status code
    monsters_api_data = response.json()
    return monsters_api_data["_items"]

def extract_required_key_value_pair_from_monster_api_data(monster_item):
      return {k:v for k,v in monster_item.items() if k=="name" or k=="hitpoints" or k=="attack_type" or k=="examine"}


def check_for_duplicate_monster_names(monster_data):
    for element in global_vars.MONSTERS_LIST:
        if element.name == monster_data["name"]:
            return True
    return False   


def load_monster_data_into_list_with_image(monster_data):
    monster_images = ['👾','👻','👹','🎃','👣 👣','👺','💀','☠ 💀','👻','🦀','👀 🐕','👿 🐺','👽 🐺','👿 👽 🐺']
    index_of_images = len(global_vars.MONSTERS_LIST) % len(monster_images)
    monster_image = monster_images[index_of_images]
    monster_details = create_monster_object_with_each_monster_api_record(monster_data,monster_image)
    append_monster_data_into_list(monster_details)
    

def create_monster_object_with_each_monster_api_record(monster_data, monster_image):
    return Monster(monster_image, monster_data["name"],monster_data["examine"],monster_data["hitpoints"],monster_data["attack_type"])   


def append_monster_data_into_list(monster_details):
    global_vars.MONSTERS_LIST.append(monster_details)