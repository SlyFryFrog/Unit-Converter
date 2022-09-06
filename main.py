# Unit Converter App
from writing_material import writing_material


def conversion_menu(w_num):
    dictionary_name = writing_material[w_num]['file']
    round_to = 2 # Temporary location/function until settings is created
    
    print(f"\nWelcome to the {writing_material[w_num]['name']}! Please choose one of the following options:\n") # Welcome message
    
    while True:
        # Prints list of available conversion options
        for num in dictionary_name:
            print(f"\t{num} - {dictionary_name[num]['menu_option']}")
        
        user_input = input("\nType here: ").lower() # Input for desired conversion to perferm
        print("\n") # Added to separate lines - has not importance

        # Checks which command user typed
        if user_input == 'e' or user_input == 'm':
            return commands(user_input)
        
        # Prompts user if input is invalid
        elif user_input in dictionary_name:
            print(f"Enter value in {dictionary_name[user_input]['original_unit']} to convert to {dictionary_name[user_input]['requested_unit']}")
            
            # Tries to calculate number - if it fails due to letters, etc. being entered, goes to exception
            try:
                convert_number = int(input("\nType here: "))
                answer = round(dictionary_name[user_input]['calculation'](convert_number), round_to)
                
                print(f"\n{convert_number}{dictionary_name[user_input]['old_abbreviation']} - {answer}{dictionary_name[user_input]['new_abbreviation']}\n")

            except ValueError:
                print("Invalid response.\n")

        else:
            print("Invalid option, please try again.\n")


# Checks user commands
def commands(user_input):
    if user_input == 'm':
        print(bar)
        return main_menu(bar)
    
    elif user_input == 'e':
        raise SystemExit
    
    else:
        print("Invalid command.")
        return main_menu(bar)



def main_menu(bar):
    menu_options = {'1' : 'Temperature', 
                    '2' : 'Length', 
                    '3' : 'Area',
                    'E' : 'Exit'}
    
    # Lists available categories for the user to choose from
    print("Welcome to the Unit Converter App! Please choose one of the following categories:\n")
    
    for key, value in menu_options.items():
        print(f"\t{key} - {value.title()}")
    
    user_input = input("\nWhat category would you like to choose?\n").lower()


    if user_input == '1' or user_input == '2' or user_input == '3': # Temporary until all sections are done
        w_num = user_input
        print(bar)
        return conversion_menu(w_num)
    
    elif user_input == 'e':
        commands(user_input)
    
    else:
        print("\nEither the section you typed is currently unavailable or you typed an invalid response. Please try again.")
        return main_menu(bar)



if __name__ == "__main__":
    bar = "\n\n=================================================================================================================\n\n"
    
    main_menu(bar) # Lists conversion categories