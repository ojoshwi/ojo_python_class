
user_number= int(input("Enter number"))

if user_number % 2== 0:
    print(f"{user_number} is even")
else:
    print(f"{user_number} is odd")

for i in range(1, user_number):
    if i*i==user_number:
        print(f"{user_number} is not a prime")
        break
else:
    print(f"{user_number} is prime")
    