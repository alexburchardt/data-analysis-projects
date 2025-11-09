food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list=(food.split(','))
equipment_list=(equipment.split(','))
pets_list=(pets.split(','))
sleep_aids_list=(sleep_aids.split(','))

food_list.sort()
equipment_list.sort()
pets_list.sort()
sleep_aids_list.sort()

print(food_list)
print(equipment_list)
print(pets_list)
print(sleep_aids_list)

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold=[food_list,equipment_list,pets_list,sleep_aids_list]

print(cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
user_input=int(input("Select a cabinet 0-3"))
Selected_cabinet=cargo_hold[user_input:]
print(Selected_cabinet)


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
if 0<= user_input <=3:
    print (f"User selected cabinet {user_input}: {Selected_cabinet}")
else:
    print ("Invalid number.")


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
user_cabinet_input=int(input("Select a cabinet 0-3"))
if 0<= user_cabinet_input <=3:
    selected_cabinet=cargo_hold[user_cabinet_input]
    print (f"User selected cabinet {user_input}: {selected_cabinet}")

    user_item_input=input("Select an item")
    if user_item_input in selected_cabinet:
        print(f"Cabinet {user_cabinet_input} DOES contain {user_item_input}")
    else:
        print(f"Cabinet {user_cabinet_input} DOES NOT contain {user_item_input}")
else:
    print ("Invalid number.")