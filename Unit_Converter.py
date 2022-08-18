# Unit Converter App
import math

def ask_conversion():
    available_options = "Celsius to fahrenheit (C to F)\nFahrenheit to celsius (F to C)\nCelsius to kelvin (C to K)\nKelvin to celsius (K to C)\n"

    print(f"Which of the following units would you like to convert? Type what's in the parenthesis.\n{available_options}")
    
    req_conversion = input("Enter one of the options: ")
 
    if req_conversion.lower() == 'c to f':
        orig_unit = 'celsius'
        new_unit = 'fahrenheit'
        temp_conversion(orig_unit, new_unit, req_conversion)
    
    elif req_conversion.lower() == 'f to c':
        orig_unit = 'fahrenheit'
        new_unit = 'celsius'
        temp_conversion(orig_unit, new_unit, req_conversion)

    elif req_conversion.lower() == 'c to k':
        orig_unit = 'celsius'
        new_unit = 'kelvin'
        temp_conversion(orig_unit, new_unit, req_conversion)
    
    elif req_conversion.lower() == 'k to c':
        orig_unit = 'kelvin'
        new_unit = 'celsius'
        temp_conversion(orig_unit, new_unit, req_conversion)

    elif req_conversion == 'e':
        exit()

    else:
        print("Please choose an available option from the list.\n\n")
        ask_conversion()


# Checks to see if user entered command or an invalid request
def options(user_input):
    if user_input == 'e':
        print("You have successfully exited the program")
        exit()
        
    elif user_input == 'm':
        # Returns user to main menu
        ask_conversion()

    else:
        print("Invalid request, returned to the main menu")
        ask_conversion()


# Celsius to fahrenheit converter
def temp_conversion(orig_unit, new_unit, req_conversion):
    print(f"\nWelcome to the {orig_unit} to {new_unit} converter!\n\nEnter the temperature in {orig_unit} you want to convert to {new_unit}.")
    print(f"Type 'e' to exit and 'm' to return to the main menu.")
    
    while True:
        user_input = input(f"\nEnter {orig_unit} here: ")
        
        # Checks if user_input is a number or a command
        try:
            # Calculates temp conversions
            if req_conversion == 'c to f':
                temp = (float(user_input) * 9/5) + 32

            elif req_conversion == 'f to c':
                temp = (float(user_input) - 32) * 5/9
            
            elif req_conversion == 'c to k':
                temp = (float(user_input) + 273.15)
            
            else:
                temp = (float(user_input) - 273.15)

            # Answer
            print(f"{user_input}°C = {round(temp, 2)}°F")

        except ValueError:
            return options(user_input)


if __name__ == '__main__':
    ask_conversion()