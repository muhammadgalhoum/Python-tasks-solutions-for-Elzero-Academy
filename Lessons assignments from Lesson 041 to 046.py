# تكليفات الدروس من الدرس 041 إلى 046
# -----------------------------------------------

# Task_1

num1 = int(input("Please enter the first number : ").strip())
num2 = int(input("Please enter the second number : ").strip())
operation = input(
    "Please enter  any operator of these operators +, -, *, /,% : ").strip()

if operation == "+":
    result = num1 + num2
    print(
        f"Your Numbers are {num1}, {num2} and the result is {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(
        f"Your Numbers are {num1}, {num2} and the result is {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(
        f"Your Numbers are {num1}, {num2} and the result is {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        num2 = int(input(
            f"The Second Number Can\'t be Equal be tO {num2}, Enter a nother number : ").strip())
        result = num1 / num2
    print(
        f"Your Numbers are {num1}, {num2} and the result is {num1} / {num2} = {result}")
elif operation == "%":
    result = num1 % num2
    print(
        f"Your Numbers are {num1}, {num2} and the result is {num1} % {num2} = {result}")
else:
    print("Please enter  any operator of these operators +, -, *, /,% : ")


# Task_2

age = 17
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")


# Task_3

age = int(input("Please Enter Your age :").strip())
if age > 10 and age < 100:
    months = age * 12
    weeks = months * 4
    days = age * 356
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print(f"Your Age in Months Is : {months}")
    print(f"Your Age in Weeks Is : {weeks:,d}")
    print(f"Your Age in Days Is : {days:,d}")
    print(f"Your Age in Hours Is : {hours:,d}")
    print(f"Your Age in Minutes Is : {minutes:,d}")
    print(f"Your Age in Seconds Is : {seconds:,d}")
else:
    print(f"Your age which equal to {age} out of range")


# Task_4

country = input("Input Your Country : ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria",
             "Yemen", "Bahrain", "England"]
# We remove KSA and USA from countries List as they need more condtions
# because their all Letters are Capital and we use capitalize() method
price = 100
discount = 30
if country in countries:
    real_price = price - discount
    print(f"Because you\'re from {country} the price is : ${real_price}")
else:
    print(
        f"Sorry, we have no discount for your country {country}, the price is : ${price}")
