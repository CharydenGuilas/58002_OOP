# Define a dictionary that maps temperature scale names to their abbreviations
TEMPERATURE_SCALES = {
    'Celsius': 'C', 'Fahrenheit': 'F', 'Kelvin': 'K'
}

# Define a function that converts temperatures between different scales
def temperature_convert(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value

# Prompt the user for input and perform the temperature conversion
while True:
    # Advise the user for input
    print("Enter the input temperature value:")
    value = float(input())
    print('Enter the input temperature scale (C, F, or K, in uppercase or lowercase characters):')
    input_scale = input()
    print('Enter the output temperature scale (C, F, or K, in uppercase or lower characters):')
    output_scale = input()

    # Convert the said temperature and print the result
    result = temperature_convert(value, input_scale, output_scale)
    print(f"{value} {input_scale} = {result} {output_scale}")

    # Advise the user to continue or quit
    print("Enter e to exit, or any key for you to continue:")
    choice = input()
    if choice.lower() == "e":
        break