#paradigm notes from todays backend meeting



# Procedural Structure Programming in Python

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Function to display a welcome message
def welcome_user(name):
    print(f"Welcome, {name}!")

# Main program
if __name__ == "__main__": ## Entry point for the program
    # Input
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    number_to_check = int(input("Enter a number to check if it's even or odd: "))
    user_name = input("Enter your name: ")

    # Processing
    area = calculate_rectangle_area(length, width)
    check_even_odd(number_to_check)

    # Output
    print(f"The area of the rectangle is: {area}")
    welcome_user(user_name)