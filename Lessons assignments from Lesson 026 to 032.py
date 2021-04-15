# تكليفات الدروس من الدرس 026 إلى 032
# -----------------------------------------------

# Task_1

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
for num in list(unique_list):
    if list(unique_list).index(num) == len(unique_list) - 1:
        print(f"{num}")
    else:
        print(f"{num}, ", end="")
unique_list = list(unique_list)
print(type(unique_list))
unique_list.pop(-1)
# we can write pop() function without giving it any index as it pop the last element as default
for num in list(unique_list):
    if list(unique_list).index(num) == len(unique_list) - 1:
        print(f"{num}")
    else:
        print(f"{num}, ", end="")

# Another solution without Turning object Data type
unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
for num in unique_list:
    if unique_list.index(num) == len(unique_list) - 1:
        print(f"{num}")
    else:
        print(f"{num}, ", end="")
print(type(unique_list))
unique_list.pop(-1)
# we can write pop() function without giving it any index as i pop()the last element as default
for num in unique_list:
    if unique_list.index(num) == len(unique_list) - 1:
        print(f"{num}")
    else:
        print(f"{num}, ", end="")


# Task_2

nums = {1, 2, 3}
letters = {"A", "B", "C"}
# First way
nums.update(letters)
print(nums)

# Second way
merge_lists = list(nums) + list(letters)
print(set(merge_lists))

# Third way
nums.union(letters)  # We can write (nums | letters)
print(nums)


# Task_3

my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()  # We can use this way too ==> my_set = {}
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")


# Task_4

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))


# Task_5

my_dict = {"HTML": "90%",
           "CSS": "80%",
           "Python": "30%"
           }
# Note : The Values of Keys in Dictionary must be between double string but the Keys don't must
print(f"\"{list(my_dict.keys())[0]} Progress Is {my_dict.get('HTML')}\"")
print(f"\"{list(my_dict.keys())[1]} Progress Is {my_dict.get('CSS')}\"")
print(f"\"{list(my_dict.keys())[2]} Progress Is {my_dict.get('Python')}\"")
my_dict["AI"] = "20%"
print(f"\"{list(my_dict.keys())[-1]} Progress Is {my_dict.get('AI')}\"")
