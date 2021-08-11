print("Welcome to the Treause Island!")
print("Your mission is to find a treasure!")
road = input("You're at the cross roads. You have to choose which road to follow. 'right', 'left', 'straight'\n")

if road == "right":
    lake = input("You've come to a lake. There's an island at the middle of the lake. You can choose to 'swim' accros the lake or to 'wait' for the boat. What will you choose?\n")
    
    if lake == "swim":
        print("You're a terrible swimmer. You drown.")
        print("THE END")
        
    elif lake == "wait":
        print("There's sudden strom at the lake. Your boat has turned up side down, and you drowned.")
        print("THE END")
        
    else:
        print("Please choose one of the options!")
        
elif road == "left":
    wild_dogs = input("You've met a pack of wild dogs. Are you going to 'run' or 'fight'")

    if wild_dogs == "run":
        print("You're slower than a hungry wild dogs. You die.")
        print("THE END")
        
    elif wild_dogs == "fight":
        print("Your only weapon is a stick. You stand no chance. You die.")
        print("THE END")
        
    else:
        print("Please choose one of the options!")
        
elif road == "straight":
    merchant = input("You meet a merchant who is willing to sell you a Treause Map. Are you going to 'buy' or 'pass'")

    if merchant == "buy":
        print("After a while you start examining the map. The paper was poisoned. You die.")
        print("THE END")
        
    elif merchant == "pass":
        print("In front of you is a wide open road. Who knows what adventures you might come across later?")
        
    else:
        print("Please choose one of the options!")
