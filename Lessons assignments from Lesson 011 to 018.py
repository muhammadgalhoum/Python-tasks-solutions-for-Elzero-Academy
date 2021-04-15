# تكليفات الدروس من الدرس 011 إلى 018
# -----------------------------------------------

# Task_1

my_name = "Muhammad"
my_age = "23"
my_country = "Egypt"
print(f"\"Hello \'{my_name}\', How You Doing \\ \"\"\" Your Age Is \"{my_age}\"\" + And Your Country Is: {my_country}")


# Task_2

print(f"""
      Hello \'{my_name}\', How You Doing \\
      \"\"\" Your Age Is \"{my_age}\"\" +
      And Your Country Is: {my_country} """)

# Aonther_way
print(f"Hello \'{my_name}\', How You Doing \\\n\"\"\" Your Age Is \"{my_age}\" +\nAnd Your Country Is: {my_country}")


# Task_3

name = 'Elzero'
print(f"Second Letter Is \"{name[1:2]}\"")
print(f"Third Letter Is \"{name[2:3]}\"")
print(f"Last Letter Is \"{name[-1]}\"")


# Task_4

name = 'Elzero'
print(f"\"{name[1:4]}\"")
print(f"\"{name[0]}{name[2]}{name[4]}\"")
print(f"\"{name[4]}{name[2]}{name[0]}\"")


# Task_5

name = "#@#@Elzero#@#@"
print(name.strip("#@"))


# Task_6

num = "9"  # Try put another number like 15, 130, 950, 1500
print(f"{num.zfill(4)}")


# Task_7

name_one = "Osama"
name_two = "Osama_Elzero"
print(f"{name_one.rjust(20,'@')}")
print(f"{name_two.rjust(20,'@')}")


# Task_8

name_one = "OSamA"
name_two = "osaMA"
print(f"{name_one.swapcase()}")
print(f"{name_two.swapcase()}")


# Task_9

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))


# Task_10

name = "Elzero"
print(name.index("z"))


# Task_11

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))


# Task_12

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))


# Task_13

name = "Muhammad"
age = 23
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
