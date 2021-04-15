# تكليفات الدروس من الدرس 065 إلى 068
# -----------------------------------------------

# Important Note: You should execute Tasks in order and Don't execute all of them in one time

import os,os.path

# Task_1

file = open(r"C:\Users\mogaze\Desktop\Python\assign.py", "w")

index = 1
while index <= 50:
    if index == 25:
        text_file = open(
            r"C:\Users\mogaze\Desktop\Python\special-txt.txt", "w")

    else:
        text_file = open(
            rf"C:\Users\mogaze\Desktop\Python\txt{str(index)}.txt", "w")
        # The following sentence will write(Elzero Web School => {index}) in all files from 1:50
        # And the value of index equal the number of it's file
        text_file.write(f"Elzero Web School => {index}\n")

    index += 1
text_file.close()

print(os.getcwd())      # Current Working Directory
print(os.path.dirname(os.path.abspath(__file__)))      # The Path of My Folder
print(os.path.basename(file.name))                  # The name of my opened file
DIR = r"C:\Users\mogaze\Desktop\Python"
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
file.close()


# Task_2

text_file = open(r"C:\Users\mogaze\Desktop\Python\txt1.txt", "a")
text_file.write("Appended => Elzero Web School\n" * 50)
text_file.close()


# Task_3

text_file = open(r"C:\Users\mogaze\Desktop\Python\txt1.txt", "r")

line_count = 0
for line in text_file:

    if line != "\n":

        line_count += 1

print("Number Of Lines Is => ", line_count)
text_file.close()

text_file = open(r"C:\Users\mogaze\Desktop\Python\txt1.txt", "r")

data = text_file.read()
words = data.split()

print("Number Of Words Is => ", len(words))
text_file.close()

text_file = open(r"C:\Users\mogaze\Desktop\Python\txt1.txt", "r")

string_list = text_file.readlines()
count_character_L = "".join(string_list)

total = 0
number_of_characters = 0
for letter in count_character_L:
    if letter == "l":
        total += 1

for letter in count_character_L:

    if letter == " " or letter == "\n":
        continue
    else:
        number_of_characters += 1

print("Number Of Chars Is => ", number_of_characters)
print("Number Of \"l\" Char Is =>", total)

text_file.close()


# Task_4

for i in range(41, 51):
    os.remove(rf"C:\Users\mogaze\Desktop\Python\txt{i}.txt")
