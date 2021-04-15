# تكليفات الدروس من الدرس 056 إلى 059
# -----------------------------------------------

# Task_1

add_list = ['add', 'ADD', 'aDd', 'A', 'a', '+']
sub_list = ['subtract', 'subTRACT', 'S', 's', '-']
mult_list = ['Multiply', 'M', 'm', 'multiply', '*']


def calculate(fNum, sNum, operation='add'):  # +, -, *
    if operation in add_list:
        return fNum + sNum
    elif operation in sub_list:
        return fNum - sNum
    elif operation in mult_list:
        return fNum * sNum
    else:
        return "This operation not found"


print(calculate(10, 20, "+"))


# Task_2

list_without_ten = []
list_with_five = []
result = 0


def addition(*nums):      # Type of nums is tuple
    # print(type(nums))      # <class 'tuple'>
    for num in nums:
        if num != 10:
            list_without_ten.append(num)
    # print(list_ten) # I  want to make sure that list_without_ten has no any number = 10
    for number in list_without_ten:
        if number == 5:
            list_with_five.append(number)
    result = sum(list_without_ten) - 2 * (sum(list_with_five))
    # First: I add all numbers in [list_without_ten] which may have any number equal to 5
    # Then I Search for any number = 5 in [list_without_ten] and append it to [list_with_five]
    # Second: I subtract the {double summation ==>[2 * (sum(list_with_five)]} of this number
    # from the summation of [list_without_ten] because he asked me to subtract Not Add any number = 5
    # and I add it Then I should Delete what I add then delete this or these number\s too

    # This equation explain what I mean (x - y) equivalent (x + y = 2y  ==> x - y)
    return result


# Important Note: Execute any function call sentence not all at the same time to have the required result
print(addition(10, 20, 30, 10, 15))  # 65
# print(addition(10, 20, 30, 10, 15, 5, 100))  # 160


# Task_3


def show_skills(name, *skills):      # Type of skills is tuple
    # print(type(skills))      # <class 'tuple'>
    if len(skills) == 0:
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills are:")
        for skill in skills:
            print(f"- {skill}")


# Important Note: Execute any function call sentence not all at the same time to have the required result
show_skills("Muhammad", "HTML", "CSS", "JS", "Python")
# show_skills("Muhammad")


# Task_4


def say_hello(name="Unknown ", age="Unknown", country="Unknown"):
    output = (f"Hello {name} Your Age Is {age} And You Live In {country}")
    return output


# Important Note: Execute any function call sentence not all at the same time to have the required result
print(say_hello("Muhammad", 23, "UAE"))
# print(say_hello())
