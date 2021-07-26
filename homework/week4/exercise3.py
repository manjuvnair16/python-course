'''
*********************************************************************************
3. Create small shopping list program, reading and writing to a file path hardcoded into your script to store the contents of the shopping list between running the program.

Usage:The program will wait for user input
Type in items on your shopping list, separated by commas between items.
After you hit Enter, the contents of your current shopping list will be shown.
e.g butter, onions, beetroot
My Names's Shopping List:beetrootonionsbuttercookies

If an item is already on the list, do not add the item to the list again.

If no input is provided, display the current shopping list

Update the list(Extension) if the keyword "reset" is used as an input to your shopping list, remove all the current items in the shopping list(Extension) 

if the keyword "remove" is used before an item, remove that item from the shopping list 

After you've got working code, try to go back and refactor it to make sure it's easy to read and look for areas of improvement.
Suggested Order:
Get input from the user using input(), splitting the input string by ",". 
Print this list.
Read from a file and create a list from the content, splitting by either "/n" or ",". 
Print the new list.
Combine both lists and print this after getting the input.
Create a set from both lists, to remove duplicates. Print the set.
Either append the new list to the existing file or overwrite the file with the combined list. Think about why you might choose to do one over the other, but either will work here.
Format the output from your script so that list is presented in a format that is easy to read.
(Extension 1)Add a check if 'reset' was in the input string. If so, write a new file to the same file path. 
(Extension 2)
For each item in the new list that contains the string "remove", put them a new list with that item, but remove the string "remove".
*********************************************************************************
'''

def read_existing_shopping_list_from_file():
    with open("shopping list.txt", 'r') as file:
        file_shopping_list = [line.strip() for line in file]
    return file_shopping_list


def accept_user_input_of_shopping_items():
    return input(f"Enter the items on your shopping list separated by commas between items and hit Enter:\
                            \ne.g butter, onions, beetroot\
                            \n")


def check_for_reset_shopping_list(shopping_list_items):
    if shopping_list_items.lower().startswith("reset"):
        return True
    else:
        return False


def reset_shopping_list():
    with open("shopping list.txt", 'w') as file:
        file.write("")


def convert_user_input_items_str_to_list(shopping_list_items):
    current_list = [item.strip() for item in shopping_list_items.split(",")]
    return current_list


def check_for_remove_item_from_list(item):
    if item.lower().startswith("remove"):
        return True
    else:
        return False


def handle_remove_item_from_current_list_and_file(item, current_list, copy_current_list, file_shopping_list):
    copy_current_list = remove_item_from_current_list(copy_current_list, item)
    item = item.split("remove")[1].strip()
    if item in file_shopping_list:
        file_shopping_list = remove_item_from_file_shopping_list(file_shopping_list, item)

    return copy_current_list, file_shopping_list


def remove_item_from_current_list(copy_current_list, item):
    copy_current_list.remove(item)
    return copy_current_list


def remove_item_from_file_shopping_list(file_shopping_list, item):
    file_shopping_list.remove(item)
    return file_shopping_list


def check_for_item_already_in_file_list(item, file_shopping_list):
    if item in file_shopping_list:
        return True
    else:
        return False


def join_new_shopping_list_with_file_list(file_shopping_list, copy_current_list):
    return file_shopping_list + copy_current_list


def convert_shopping_list_to_str(file_shopping_list):
    shopping_list_items = "\n".join(file_shopping_list)
    _append_next_line_to_file_list(shopping_list_items)
    return shopping_list_items


def _append_next_line_to_file_list(shopping_list_items):
    shopping_list_items += "\n"
    return shopping_list_items


def write_new_shopping_list_to_file(shopping_list_items):
    with open("shopping list.txt", 'w') as file:
        file.write(shopping_list_items)


def read_new_shopping_list_from_file():
    with open("shopping list.txt", 'r') as file:
        file_list_items = file.read()
    return file_list_items   


def print_new_shopping_list(file_list_items):
    print(f"My Shopping List:\
                \n{file_list_items}\
            ")

def main():    
    shopping_list_items = accept_user_input_of_shopping_items()
    if check_for_reset_shopping_list(shopping_list_items):
        reset_shopping_list()
    else:
        current_list = convert_user_input_items_str_to_list(shopping_list_items)
        file_shopping_list = read_existing_shopping_list_from_file()
        copy_current_list = current_list[0:]

        for item in current_list:
            if check_for_remove_item_from_list(item):
                copy_current_list, file_shopping_list = handle_remove_item_from_current_list_and_file(item, current_list, copy_current_list, file_shopping_list)
            elif check_for_item_already_in_file_list(item, file_shopping_list):
                copy_current_list = remove_item_from_current_list(copy_current_list, item)
        
        updated_file_shopping_list = join_new_shopping_list_with_file_list(file_shopping_list, copy_current_list)
        shopping_list_items = convert_shopping_list_to_str(updated_file_shopping_list)
        write_new_shopping_list_to_file(shopping_list_items)
        file_list_items = read_new_shopping_list_from_file()
        print_new_shopping_list(file_list_items)


if __name__ == "__main__":
    main()

    
   
    


    
