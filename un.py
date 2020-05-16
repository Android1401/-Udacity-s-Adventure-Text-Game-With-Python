import random
import time

def way():
    random.randint(1,2,3)
def start_room():
    
    start_room_options=['1','2','3']
    user_choice=""
    while user_choice not in start_room_options:
        print("You were in sunshine valley hotel")
        time.sleep(2)
        print("You have stuck in a car with flat tyre")
        time.sleep(2)
        print("You have only 3 options to do")
        time.sleep(2)
        print("1.stay in the car")
        time.sleep(2)
        print("2.Get out and check the tires")
        time.sleep(2)
        print("3.start the car and drive with no lights")
        time.sleep(2)

        user_choice=str(input("Enter option number"))
#print("You have selected"+"user_choice")

    if user_choice==start_room_options[0]:
       room01()
    elif user_choice==start_room_options[1]:
       room02()
    elif user_choice==start_room_options[2]:
       room03()
def room01():
    print("you stayed in the car")
def room02():
    print("You went out to check the tyres")
def room03():
    print("You started the car with flat tyre")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    start_room()
    playAgain = input("Do you want to play again? (yes or y to continue playing): ") 
