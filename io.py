batteries=[50,30,9,60,5,24,90,87]
minimum_battery_power=20

usable_battery_power = 0
usable_battery_count = 0

for battery in batteries:
    if battery > minimum_battery_power:
        usable_battery_power += battery #if yes use power added
        usable_battery_count = usable_battery_count + 1   #if yes use battery count add

print(usable_battery_power, usable_battery_count)



#To decode use -1

alien_message= " Hi human, How are you?"

print(f""""
Alien message={alien_message}

Human message= {alien_message [::-1]}
""")

available_foods=[
    "cupcake",
    "pastries",
    "icecream",
    "pizza",
    "burger",
    "cherry",
    "banana",
]
available_crews=3
each_crew_food=len(available_foods)//  available_crews
remaining_food_count=len(available_foods)% available_crews
print(f"Each crew get {each_crew_food} food and remaining food count is {remaining_food_count}")


## function
def setup_mission():
    print("Setting up for mission.....")
    available_foods=[
    "cupcake",
    "pastries",
    "icecream",
    "pizza",
    "burger",
    "cherry",
    "banana",
]
    available_crews= int(input("Enter available crews:"))
    print("Setup completed......")
    return available_crews, available_foods

def alien_attack_game():
    print("Welcome to allien attack game")
    print("Starting misssion......")

    crews_number, food = setup_mission()
    print(f"You have {crews_number} food and remaining food count is {available_foods}")

    print("Welcome to mars!!!")
    print("Your battery is dead please change battery")

def change_battery():
        available batteries=[50,30,9,60,5,24,90,87]
        minimum_battery_power=20

        usable_battery_power = 0
        usable_battery_count = 0

        for battery in batteries:
            if battery > minimum_battery_power:
            usable_battery_power += battery #if yes use power added
            usable_battery_count = usable_battery_count + 1   #if yes use battery count add

     print(usable_battery_power, usable_battery_count)
    
    

    print("Mission completed")
alien_attack_game()
