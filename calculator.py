while True:

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another one: "))
    
    a = num1 * num2
    b = num1 + num2
    c = num1 / num2
    d = num1 - num2

    choice = input("Do you want to multiply (m), divide (d), add (a) or subtract (s)? ")
    
    if (choice == "m") or (choice == "multiply"):
        print(a)

    elif (choice == "a") or (choice == "add"):
        print(b)

    elif (choice == "d") or (choice == "divide"):
        print(c)

    elif (choice == "s") or (choice == "subtract"):
        print(d)
        
