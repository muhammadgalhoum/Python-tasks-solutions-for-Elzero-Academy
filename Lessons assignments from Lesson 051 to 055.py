# تكليفات الدروس من الدرس 051 إلى 055
# -----------------------------------------------

# Task_1

# Advanced Solution
# The program will take input from the User
def divived_by_five(numbers):
    my_list = []
    for num in numbers:
        if num % 5 == 0:
            my_list.append(num)
    my_list.sort(reverse=True)
    my_sorted_list = my_list
    for count, number in enumerate(my_sorted_list, 1):
        print(f"{count} => {number}")


# You can pass List or Tuple as function argument
divived_by_five((15, 81, 5, 17, 20, 21, 13))  # Tuple
divived_by_five([15, 81, 5, 17, 20, 21, 13])  # List
print("All Numbers Printed")

# Another Important Solution


def divived_by_five(*numbers):
    if len(numbers) == 0:
        return"You didn't pass any numbers"
    my_list = []
    for num in numbers:
        if num % 5 == 0:
            my_list.append(num)
    if len(my_list) == 0:
        return"No number is divisible by 5"
    my_list.sort(reverse=True)
    my_sorted_list = my_list
    for count, number in enumerate(my_sorted_list, 1):
        print(f"{count} => {number}")
    return "All Numbers Printed"


# In this case you can pass one number or more or didn't pass any number as a function argument
print(divived_by_five(15, 81, 5, 17, 20, 21, 13))

# The ordinary solution which is required
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
my_sorted_list = []
for number in my_nums:
    if number % 5 == 0:
        my_sorted_list.append(number)
for count, number in enumerate(my_sorted_list, 1):
    print(f"{count} => {number}")
print("All Numbers Printed")


# Task_2

numNotPrinted = [6, 8, 12]
index = 1
while index <= 20:
    if index not in numNotPrinted:
        print(f"{str(index).zfill(2)}")
    index += 1
print("All Numbers Printed")


# Task_3

my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
A = 100
B = 80
C = 40
total = ""
for key in my_ranks:
    if my_ranks[key] == 'A':
        mark = 100
    elif my_ranks[key] == 'B':
        mark = 80
    elif my_ranks[key] == 'C':
        mark = 40
    total += my_ranks[key]
    print(f"My Rank in {key} Is {my_ranks[key]} And This Equal {mark} Points")
# print(total)    # I want to make sure that i collect all my marks letters as a string Data type
markList = list(total)
# print(markList)     # I print markList to make sure that I change total Data Type to List
lastMarkList = []
for letter in markList:
    if letter == 'A':
        lastMarkList.append(A)
    elif letter == 'B':
        lastMarkList.append(B)
    elif letter == 'C':
        lastMarkList.append(C)
total_mark = 0
for mark_value in lastMarkList:
    total_mark += mark_value
print(f"Total Points Is {total_mark}")


# Another Solution
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
A = 100
B = 80
C = 40
total = ""
for key in my_ranks:
    if my_ranks[key] == 'A':
        mark = 100
    elif my_ranks[key] == 'B':
        mark = 80
    elif my_ranks[key] == 'C':
        mark = 40
    total += my_ranks[key]
    print(f"My Rank in {key} Is {my_ranks[key]} And This Equal {mark} Points")
# print(total)    # I want to make sure that i collect all my marks letters as a string Data type
lastMarkList = []
for letter in total:
    if letter == 'A':
        lastMarkList.append(A)
    elif letter == 'B':
        lastMarkList.append(B)
    elif letter == 'C':
        lastMarkList.append(C)
total_mark = 0
for mark_value in lastMarkList:
    total_mark += mark_value
print(f"Total Points Is {total_mark}")


# Task_4

# First Solution without using items() method
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

A = 100
B = 80
C = 40
D = 20
total_marks_firstStudent = ""
total_marks_secondStudent = ""
total_marks_thirdStudent = ""

for main_key in students:
    print("------------------------------")
    print(f"\"-- Student Name => {main_key}\"")
    print("------------------------------")
    for inner_key in students[main_key]:
        if students[main_key][inner_key] == 'A':
            if main_key == "Ahmed":
                total_marks_firstStudent += students[main_key][inner_key]
            elif main_key == "Sayed":
                total_marks_secondStudent += students[main_key][inner_key]
            elif main_key == "Mahmoud":
                total_marks_thirdStudent += students[main_key][inner_key]
            mark = 100
        elif students[main_key][inner_key] == 'B':
            if main_key == "Ahmed":
                total_marks_firstStudent += students[main_key][inner_key]
            elif main_key == "Sayed":
                total_marks_secondStudent += students[main_key][inner_key]
            elif main_key == "Mahmoud":
                total_marks_thirdStudent += students[main_key][inner_key]
            mark = 80
        elif students[main_key][inner_key] == 'C':
            if main_key == "Ahmed":
                total_marks_firstStudent += students[main_key][inner_key]
            elif main_key == "Sayed":
                total_marks_secondStudent += students[main_key][inner_key]
            elif main_key == "Mahmoud":
                total_marks_thirdStudent += students[main_key][inner_key]
            mark = 40
        elif students[main_key][inner_key] == 'D':
            if main_key == "Ahmed":
                total_marks_firstStudent += students[main_key][inner_key]
            elif main_key == "Sayed":
                total_marks_secondStudent += students[main_key][inner_key]
            elif main_key == "Mahmoud":
                total_marks_thirdStudent += students[main_key][inner_key]
            mark = 20

        print(f"\"- {inner_key} => {mark} Points\"")

    marksList_firstStudent = []
    for letter in total_marks_firstStudent:
        if letter == 'A':
            marksList_firstStudent.append(A)
        elif letter == 'B':
            marksList_firstStudent.append(B)
        elif letter == 'C':
            marksList_firstStudent.append(C)
        elif letter == 'D':
            marksList_firstStudent.append(D)

    marksList_secondStudent = []

    for letter in total_marks_secondStudent:
        if letter == 'A':
            marksList_secondStudent.append(A)
        elif letter == 'B':
            marksList_secondStudent.append(B)
        elif letter == 'C':
            marksList_secondStudent.append(C)
        elif letter == 'D':
            marksList_secondStudent.append(D)

    marksList_thirdStudent = []

    for letter in total_marks_thirdStudent:
        if letter == 'A':
            marksList_thirdStudent.append(A)
        elif letter == 'B':
            marksList_thirdStudent.append(B)
        elif letter == 'C':
            marksList_thirdStudent.append(C)
        elif letter == 'D':
            marksList_thirdStudent.append(D)

    if main_key == "Ahmed":
        total_mark_firstStudent = 0
        for mark_value_firstStudent in marksList_firstStudent:
            total_mark_firstStudent += mark_value_firstStudent
        print(
            f"\"Total Points For {main_key} Is {total_mark_firstStudent}\"")
        # print(marksList_firstStudent)

    elif main_key == "Sayed":
        total_mark_secondStudent = 0
        for mark_value_secondStudent in marksList_secondStudent:
            total_mark_secondStudent += mark_value_secondStudent
        print(f"\"Total Points For {main_key} Is {total_mark_secondStudent}\"")
        # print(marksList_secondStudent)

    elif main_key == "Mahmoud":
        total_mark_thirdStudent = 0
        for mark_value_thirdStudent in marksList_thirdStudent:
            total_mark_thirdStudent += mark_value_thirdStudent
        print(f"\"Total Points For {main_key} Is {total_mark_thirdStudent}\"")
        # print(marksList_thirdStudent)

# Second Solution using items() method

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

A = 100
B = 80
C = 40
D = 20
total_marks_firstStudent = ""
total_marks_secondStudent = ""
total_marks_thirdStudent = ""

for main_key, main_value in students.items():  # Don't forgot to put "," when using items() method
    print("------------------------------")
    print(f"\"-- Student Name => {main_key}\"")
    print("------------------------------")
    for child_key, child_value in main_value.items():  # Don't forgot to put "," when using items() method
        if child_value == 'A':
            if main_key == "Ahmed":
                total_marks_firstStudent += child_value
            elif main_key == "Sayed":
                total_marks_secondStudent += child_value
            elif main_key == "Mahmoud":
                total_marks_thirdStudent += child_value
            mark = 100
        elif child_value == 'B':
            if main_key == "Ahmed":
                total_marks_firstStudent += child_value
            elif main_key == "Sayed":
                total_marks_secondStudent += child_value
            elif main_key == "Mahmoud":
                total_marks_thirdStudent += child_value
            mark = 80
        elif child_value == 'C':
            if main_key == "Ahmed":
                total_marks_firstStudent += child_value
            elif main_key == "Sayed":
                total_marks_secondStudent += child_value
            elif main_key == "Mahmoud":
                total_marks_thirdStudent += child_value
            mark = 40
        elif child_value == 'D':
            if main_key == "Ahmed":
                total_marks_firstStudent += child_value
            elif main_key == "Sayed":
                total_marks_secondStudent += child_value
            elif main_key == "Mahmoud":
                total_marks_thirdStudent += child_value
            mark = 20

        print(f"\"- {child_key} {child_value} => {mark} Points\"")

    marksList_firstStudent = list(total_marks_firstStudent)
    marksList_secondStudent = list(total_marks_secondStudent)
    marksList_thirdStudent = list(total_marks_thirdStudent)

    output_marksList_firstStudent = []

    for letter in marksList_firstStudent:
        if letter == 'A':
            output_marksList_firstStudent.append(A)
        elif letter == 'B':
            output_marksList_firstStudent.append(B)
        elif letter == 'C':
            output_marksList_firstStudent.append(C)
        elif letter == 'D':
            output_marksList_firstStudent.append(D)

    output_marksList_secondStudent = []

    for letter in marksList_secondStudent:
        if letter == 'A':
            output_marksList_secondStudent.append(A)
        elif letter == 'B':
            output_marksList_secondStudent.append(B)
        elif letter == 'C':
            output_marksList_secondStudent.append(C)
        elif letter == 'D':
            output_marksList_secondStudent.append(D)

    output_marksList_thirdStudent = []

    for letter in marksList_thirdStudent:
        if letter == 'A':
            output_marksList_thirdStudent.append(A)
        elif letter == 'B':
            output_marksList_thirdStudent.append(B)
        elif letter == 'C':
            output_marksList_thirdStudent.append(C)
        elif letter == 'D':
            output_marksList_thirdStudent.append(D)

    if main_key == "Ahmed":
        total_mark_firstStudent = 0
        for mark_value_firstStudent in output_marksList_firstStudent:
            total_mark_firstStudent += mark_value_firstStudent
        print(
            f"\"Total Points For {main_key} Is {total_mark_firstStudent}\"")
        # print(marksList_firsthirdStudent)

    elif main_key == "Sayed":
        total_mark_secondStudent = 0
        for mark_value_secondStudent in output_marksList_secondStudent:
            total_mark_secondStudent += mark_value_secondStudent
        print(f"\"Total Points For {main_key} Is {total_mark_secondStudent}\"")
        # print(marksList_secondStudent)

    elif main_key == "Mahmoud":
        total_mark_thirdStudent = 0
        for mark_value_thirdStudent in output_marksList_thirdStudent:
            total_mark_thirdStudent += mark_value_thirdStudent
        print(f"\"Total Points For {main_key} Is {total_mark_thirdStudent}\"")
        # print(marksList_thirdStudent)
