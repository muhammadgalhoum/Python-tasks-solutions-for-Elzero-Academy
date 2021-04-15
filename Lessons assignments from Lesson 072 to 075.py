# تكليفات الدروس من الدرس 072 إلى 075
# -----------------------------------------------
from functools import reduce

# Task_1


def remove_chars(word):
    return word[1:-1]


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars, friends_map)

for friend in cleaned_list:
    print(f"\"{friend}\"")


# Solution using lambda function

# Note: When using lambda function u should turn off FormatOnSave from settings

for friend in map(lambda word: word[1: -1], friends_map):
    print(f"\"{friend}\"")


# Task_2

def get_names(name):
    return name.endswith("m")


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names, friends_filter)

for name in names:
    print(f"\"{name}\"")


# Solution using lambda function

# Note: When using lambda function u should turn off FormatOnSave from settings

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

for name in filter((lambda name: name.endswith("m")), friends_filter):
    print(f"\"{name}\"")


# Task_3

nums = [2, 4, 6, 2]


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply(nums))


# Solution using lambda function

# Note: When using lambda function u should turn off FormatOnSave from settings

# Note : We should import reduce from functools like this => from functools import reduce
nums = [2, 4, 6, 2]

result = reduce((lambda x, y: x * y), nums)

print(result)


# Task_4

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
my_list = list(skills)
my_list.reverse()
for count, lang in enumerate(my_list, 50):
    if type(lang) == int:
        continue
    else:
        print(f"\"{count} - {lang}\"")


# Another Solution
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

index = len(skills) - 1
count = 50
while index >= 0:
    item = skills[index]
    if type(item) == int:
        index -= 1
        count += 1
        continue
    else:
        print(f"\"{count} - {item}\"")

    index -= 1
    count += 1
