first_number= int(input("enter your first number :"))
second_number= int(input("enter your second number :"))
user_choice = input ("""
        please choose ur option
        + for addition,
        - for subraction
        """)
if user_choice =="+":
    print("addition=", first_number + second_number)
elif user_choice =="-":
        print("subraction=", first_number - second_number)
else:
    print("Invalid option")
    
   print("mutipication=", first_number * second_number)
    print("subraction=", first_number - second_number)
    print("division=", first_number / second_number)
    print("exponent=", first_number ** second_number)
    print("modulus=", first_number % second_number)
    print("floor division=", first_number // second_number)
