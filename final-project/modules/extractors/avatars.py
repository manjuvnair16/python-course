from modules.extractors.constants import global_vars
from modules.classes.avatar import Avatar
import pandas as pd

'''
--------------------------------------------------------------------
Get and load avatar data into list from csv file using pandas
--------------------------------------------------------------------
'''

def load_avatar_data_from_csv_to_list():
    """
    Gets data from avatar_data.csv & loads it into AVATAR_LIST
    """

    df = pd.read_csv("data/avatar_data.csv")
    for i in df.index:
        row_index = df.loc[i]
        global_vars.AVATAR_LIST.append(Avatar(row_index["name"], row_index["img"], int(row_index["HP"]),row_index["signature move"]))    

