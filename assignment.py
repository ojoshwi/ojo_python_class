while True:
    print("Welcome to the Number Magic Game!")
    print("Think of a number and let's do some magic with it.")

    # Step 1: Get the number from the user
    number = float(input("Enter a number: "))

    # Step 2: Perform the magic steps
    step1 = number * 2
    print(f"Step 1: Double it -> {step1}")

    step2 = step1 + 10
    print(f"Step 2: Add 10 -> {step2}")

    step3 = step2 / 2
    print(f"Step 3: Halve it -> {step3}")

    step4 = step3 - number
    print(f"Step 4: Subtract your original number -> {step4}")

    # Always results in 5
    print(f"The result is: {step4}")
    print("Magic, isn't it? It always works!")

    user_choice=input("""
    do you want to continue?
    yes or
    no """)
    if user_choice.lower()=="no":
        break


