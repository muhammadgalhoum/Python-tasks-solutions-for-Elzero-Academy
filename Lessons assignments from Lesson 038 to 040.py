# تكليفات الدروس من الدرس 038 إلى 040
# -----------------------------------------------

# Task_1

name = input("Please enter your first name : ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")


# Task_2

age = int(input("Please enter your age : ").strip())
if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


# Task_3

first_name = input("Please enter the first name : ").strip().capitalize()
second_name = input("Please enter the second name : ").strip().capitalize()
print(f"Hello {first_name} {second_name:.1s}.")


# Task_4

my_email = input("Please enter your email :").strip().lower()
print(f"Your Name Is {my_email.capitalize()[:my_email.index('@')]}")
print(
    f"Email Service Provider Is {my_email[my_email.index('@') + 1 : my_email.index('.')]}")
print(f"Top Level Domain Is {my_email[my_email.index('.') + 1:]}")
