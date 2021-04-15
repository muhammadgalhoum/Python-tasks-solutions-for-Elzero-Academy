# تكليفات الدروس من الدرس 033 إلى 037
# -----------------------------------------------

# Task_1

# True Values
print(True)
print(bool(1))  # We can also write float number like bool(16.6)
print(bool(6 > 4))
print(bool([1, 2, 3, 4, 5, 6]))
print(bool("Hanan"))
# False Values
print(False)
print(bool(0))
print(bool(12 < 6))
print(bool([]))
print(bool(""))


# Task_2

html = 80
css = 60
javascript = 70
result = html > 50 and css > 50 and javascript > 50
print(result)


# Task_3

num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)


# Task_4

num_one = 10
num_two = 20
result = num_one + num_two
print(result)
second_result = result ** 3
print(second_result)
second_result -= 26000
print(second_result)
last_result = second_result / 5
print(last_result)
last_result = str(last_result)
print(type(last_result))
