from modules.extractors.constants import global_vars
from modules.classes.pick_up import PickUp
import pandas as pd

'''
--------------------------------------------------------------------
Get and load pick up data into list from csv file using pandas
--------------------------------------------------------------------
'''

def load_pick_up_data_from_csv_to_list():  
    """
    Gets data from pick_up_data.csv & loads it into PICK_UP_LIST
    """

    df = pd.read_csv("data/pick_up_data.csv")
    for i in df.index:
        row_index = df.loc[i]
        global_vars.PICK_UP_LIST.append(PickUp(row_index["name"], row_index["img"], row_index["description"]))

