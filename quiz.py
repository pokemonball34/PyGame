# A Function that asks for the initial temperature type and converts it from Celsius to Fahrenheit or vice versa
def temperature_type_def(temperature_type):

    # Conditional to check if user typed in C or c to convert from C -> F
    if temperature_type == 'C' or temperature_type == 'c':
        # Asks the user for the temperature value
        temperature = float(input('Please input the temperature value: '))
        # Returns the converted value
        return print(str(temperature) + "C is " + str(temperature * 1.8 + 32) + "F.")

    # Conditional to check if user typed in F or f to convert from F -> C
    elif temperature_type == "F" or temperature_type == "f":
        # Asks the user for the temperature value
        temperature = float(input('Please input the temperature value: '))
        # Returns the converted value
        return print(str(temperature) + "F is " + str((temperature - 32) / 1.8) + "C.")

    # Recursion to reset the program if the user written an error
    else:
        # Prints the console that an error has occured
        print('ERROR, Please try again')
        # Restarts the function
        return temperature_type_def(input('Please input the temperature type you are converting from (Type C or F): '))

# Calls the function
temperature_type_def(input('Please input the temperature type you are converting from (Type C or F): '))