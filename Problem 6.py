complete = 0 # Says whether the program is done or not

from math import pi # Defines pi

while (complete == 0): # Loops

    complete = 0 # Sets program to not done yet

    try: # Checks that you input a number

        r = float(input("What is the radius of this circle? ")) # Asks for radius

    except: # If its not a number

        print("That's not a number!")

        continue # Restarts

    d = r * 2 # Finds diameter

    c = d * pi # Calculates circumference

    a = pi * r * r # Calculates area

    print("The area is",a,"!") # Tells you the area

    print("The circumference is",c,"!") # Tells you the circumference

    print("The diameter is",d,"!") # Tells you the diameter

    again = input("Do you want to go again? ") # Asks you if you want to continue

    again = again.lower() # Converts text to lowercase so that it can recognise it

    if (again == "yes") or (again == "y"): 

        continue # Restarts

    elif (again == "no") or (again == "n"):

        complete = 1 # Ends

    
        


