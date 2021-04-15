# تكليفات الدروس من الدرس 021 إلى 023
# -----------------------------------------------

# Task_1

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])


# Task_2

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(f"\"{friends[0]}\", \"{friends[2]}\", \"{friends[4]}\"")
print(f"\"{friends[1]}\", \"{friends[3]}\"")

# Another way for any List whatever the numbers of it's items
even_list = []
odd_list = []
for name in friends:
    if friends.index(name) % 2 == 0:
        even_list.append(friends[friends.index(name)])
    else:
        odd_list.append(friends[friends.index(name)])
# We will loop on all elements in even_list or odd_list and print the Desired shape
for item in even_list:
    if even_list.index(item) == len(even_list) - 1:
        print(f"\"{item}\"")
    else:
        print(f"\"{item}\", ", end="")
for item in odd_list:
    if odd_list.index(item) == len(odd_list) - 1:
        print(f"\"{item}\"")
    else:
        print(f"\"{item}\", ", end="")


# Task_3

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(f"\"{friends[1]}\", \"{friends[2]}\", \"{friends[3]}\",")
print(f"\"{friends[-2]}\", \"{friends[-1]}\"")


# Task_4

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2] = "Elzero"
friends[-1] = "Elzero"
print(friends)

# Another way in our List "friends" Not Original Case
friends[3:] = "Elzero", "Elzero"
print(friends)


# Task_5

friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends)


# Task_6

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.remove("Nasser")
friends.remove("Osama")
print(friends)
friends.remove("Salem")
print(friends)


# Task_7

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

# Another way u should use one of them
friends += employees + school
print(friends)


# Task_8

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# Note: if we writ the Two following Lines of Code
# print(friends.sort())              ==> Output = None
# print(friends.sort(reverse=True))  ==> Output = None
# So we should use sort method firstly then use print method
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)


# Task_9

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))


# Task_10

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])
