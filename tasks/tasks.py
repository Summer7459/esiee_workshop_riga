#Task 1: Create a function to cook your favorite dish. It should contain parameters, methods and conditions.

def cook_beef_bourguignon(meat_weight, add_mushrooms, cooking_time):
    print(f"Preparing beef bourguignon with {meat_weight}g of meat...")

    def prepare_ingredients():
        print("Chopping meat, carrots, and onions...")

    def brown_meat():
        print("Browning the meat in a pot...")

    def add_wine():
        print("Adding red wine 🍷 and starting to simmer...")

    def simmer():
        print(f"Letting it simmer for {cooking_time} hours...")

    # Steps
    prepare_ingredients()
    brown_meat()
    add_wine()

    if add_mushrooms:
        print("Adding mushrooms 🍄")
    else:
        print("No mushrooms added")

    if cooking_time >= 3:
        print("Perfect slow cooking 👌")
    else:
        print("Warning: cooking time may be too short")

    simmer()
    print("Beef bourguignon is ready! 🍲")

# Example
cook_beef_bourguignon(800, True, 3)



#Task 2: Conditional Statements
#Write a Python program that checks if a given number is positive, negative, or zero. Print an appropriate message for each case.

class NumberChecker:

    @staticmethod
    def check_number(number):
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

# Example usage
NumberChecker.check_number(10)
NumberChecker.check_number(-5)
NumberChecker.check_number(0)



#Task 3:
#Write a program that prints all even numbers between 1 and 20 using both a for loop and a while loop.

class EvenNumbers:

    @staticmethod
    def using_for():
        print("Using for loop:")
        for i in range(1, 21):
            if i % 2 == 0:
                print(i)

    @staticmethod
    def using_while():
        print("Using while loop:")
        i = 1
        while i <= 20:
            if i % 2 == 0:
                print(i)
            i += 1

# Example usage
EvenNumbers.using_for()
EvenNumbers.using_while()
