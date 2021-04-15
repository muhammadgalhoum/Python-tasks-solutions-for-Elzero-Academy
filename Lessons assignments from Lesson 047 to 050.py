# تكليفات الدروس من الدرس 047 إلى 050
# -----------------------------------------------

# Task_1

num = int(input("Enter Any  Positve Integer Number : ").strip())
my_list = []
if num == 0:
    print(f"Number {num} Is Not Larger Than 0")
elif num > 0:
    while num > 0:
        num -= 1
        if num == 6:
            continue
        elif num == 0:
            break
        my_list.append(num)
        print(num)
    print(f"{len(my_list)} Numbers Printed Successfully.")
else:
    print(f"Please Enter {-1*num} not {num} and run the code again")


# Task_2

# Advanced Solution
names = input(
    "Enter your friends and put only one space between every name : ").strip()
# We can add any numbers of our friends as we like not only 5 friends
friends = names.split(" ")      # The String became List
index = 0
my_list = []
while index < len(friends):
    if friends[index][0] == friends[index][0].capitalize():
        print(friends[index].capitalize())
    else:
        my_list.append(friends[index])
    index += 1
print(f"Friends Printed And Ignored Names Count Is {len(my_list)}")

# Required Solution
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
index = 0
my_list = []
while index < len(friends):
    if friends[index][0] == friends[index][0].capitalize():
        print(friends[index].capitalize())
    else:
        my_list.append(friends[index])
    index += 1
print(f"Friends Printed And Ignored Names Count Is {len(my_list)}")


# Task_3

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print([item for item in skills])
    skills = []


# Task_4

# Advanced Solution
my_friends = []     # Max elements in this list is 4
while len(my_friends) < 4:
    person_name = input("Enter the person name : ").strip()
    if person_name == person_name.upper():
        print("Invalid Name")
    elif person_name == person_name.lower():
        person_name = person_name.capitalize()
        my_friends.append(person_name)
        print(f"Friend {person_name} Added => 1st Letter Become Capital")
        if 4 - len(my_friends) == 1:
            print(f" The Last Place")
        elif 4 - len(my_friends) == 0:
            break
        else:
            print(f"Names Left in List Is {4 - len(my_friends)}")
    elif person_name == person_name.capitalize():
        my_friends.append(person_name)
        print(f"Friend {person_name} Added")
        if 4 - len(my_friends) == 1:
            print(f"The Last Place")
        elif 4 - len(my_friends) == 0:
            break
        else:
            print(f"Names Left in List Is {4 - len(my_friends)}")
print(my_friends)

# Original Solution and that is required
my_friends = []     # Max elements in this list is 4
while len(my_friends) < 4:
    person_name = input("Enter the person name : ").strip()
    if person_name == person_name.upper():
        print("Invalid Name")
    elif person_name == person_name.lower():
        person_name = person_name.capitalize()
        my_friends.append(person_name)
        print(f"Friend {person_name} Added => 1st Letter Become Capital")
        if 4 - len(my_friends) == 0:
            break
        else:
            print(f"Names Left in List Is {4 - len(my_friends)}")
    elif person_name == person_name.capitalize():
        my_friends.append(person_name)
        print(f"Friend {person_name} Added")
        if 4 - len(my_friends) == 0:
            break
        else:
            print(f"Names Left in List Is {4 - len(my_friends)}")
print(my_friends)
