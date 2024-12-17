user_choice= input("""
 1. circle
 2. Rectangle
""")
if user_choice ==1:
    user_radius= float(input("Enter radius :"))
    result_area= 3.14*user_radius**2
    result_perimeter= 2*3.14*user_radius
    print(f"area={result_area} ")
    print(f"perimeter={result_perimeter} ")

elif user_choice ==2:
    user_length= float(input("Enter length :"))
    user_width= float(input("Enter width"))
    result_area= user_length*user_width
    print(f"area={result_area} ")
    
else:
    print("Invalid input")