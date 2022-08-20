# Unit Converter App
def temperature_menu():
    # Dictionary of all variables for temperature conversions
    temperature_conversions = { '1': { 'menu_option' : "Celsius to Fahrenheit",
                                            'original_unit' : "Celsius",
                                            'requested_unit' : "Fahrenheit",
                                            'calculation' : lambda x :(x * 9/5) + 32
                                        },
                                '2' : {'menu_option' : "Fahrenheit to Celsius",
                                            'original_unit' : "Fahrenheit",
                                            'requested_unit' : "Celsius",
                                            'calculation' : lambda x :(x - 32) * 5/9
                                        },
                                '3' : {'menu_option' : "Celsius to Kelvin",
                                            'original_unit' : "Celsius",
                                            'requested_unit' : "Kelvin",
                                            'calculation' : lambda x :(x - 273.15)
                                        },
                                '4' : {'menu_option' : "Kelvin to Celsius",
                                            'original_unit' : "Kelvin",
                                            'requested_unit' : "Celsius",
                                            'calculation' : lambda x :(x + 273.15)
                                        },
                                'm' : {'menu_option' : "Main Menu"
                                        },
                                'e' : {'menu_option' : "Exit"
                                        },
    }
    print("\nWelcome to the Temperature Converter! Please choose one of the following options:\n")
    
    while True:
        # Prints list of available conversion options
        for num in temperature_conversions:
            print(f"\t{num} - {temperature_conversions[num]['menu_option']}")
        
        user_input = input("\nType here: ").lower()
        print("\n") # Added to separate lines - has not importance

        # Checks which command user typed
        if user_input == 'e' or user_input == 'm':
            return commands(user_input)
        
        # Prompts user if input is invalid
        elif user_input in temperature_conversions:
            print(f"Enter value in {temperature_conversions[user_input]['original_unit']} to convert to {temperature_conversions[user_input]['requested_unit']}")
            
            # Tries to calculate number - if it fails due to letters, etc. being entered, goes to exception
            try:
                convert_number = int(input("\nType here: "))
                answer = temperature_conversions[user_input]['calculation'](convert_number)
                print(answer)
            
            except ValueError:
                print("Invalid response.\n")

        else:
            print("Invalid option, please try again.")

# Checks user commands
def commands(user_input):
    if user_input == 'm':
        print(bar)
        return main_menu()
    
    elif user_input == 'e':
        raise SystemExit
    
    else:
        print("Invalid command.")
        return main_menu()


def main_menu():
    menu_options = {'1' : 'Temperature', 
                    '2' : 'Length', 
                    '3' : 'Area', 
                    '4' : 'Volume',
                    '5' : 'Weight',
                    'E' : 'Exit'}
    
    # Lists available categories for the user to choose from
    print("Welcome to the Unit Converter App! Please choose one of the following categories:\n")
    
    for key, value in menu_options.items():
        print(f"\t{key} - {value.title()}")
    
    user_input = input("\nWhat category would you like to choose?\n").lower()


    if user_input == '1' or user_input == 'temperature':
        print(bar)
        return temperature_menu()
    
    elif user_input == 'e' or user_input == 'exit':
        commands(user_input)
    
    else:
        print("\nEither the section you typed is currently unavailable or you typed an invalid response. Please try again.")
        return main_menu()


if __name__ == "__main__":
    # Global variables
    global bar 
    bar = "\n\n=================================================================================================================\n\n"
    
    main_menu() # Lists conversion categories 
