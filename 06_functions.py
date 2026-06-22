# ================================
# LESSON 6: Functions
# ================================

# Function banana — def keyword se
# Bash mein: function_name() { ... }
# Python mein: def function_name():

def greet(name):
    print(f"Assalam o Alaikum, {name}!")

def add_numbers(a, b):
    result = a + b
    return result  # result wapas bhejo

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Functions call karo
greet("Ramzan")
greet("Ali")

total = add_numbers(10, 20)
print(f"10 + 20 = {total}")

status = check_age(25)
print(f"Age 25: {status}")

status = check_age(15)
print(f"Age 15: {status}")
