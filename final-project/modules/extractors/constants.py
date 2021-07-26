from modules.classes.config import Config_Data
import json

with open("data/config.json","r") as config_file:
    global_vars = Config_Data(config_file)