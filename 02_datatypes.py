# ================================
# LESSON 2: Data Types
# ================================

# String — text
name = "Ramzan"

# Integer — pura number
age = 22

# Float — decimal number
height = 5.9

# Boolean — True ya False
is_student = True
is_married = False

# Type check karo — kaunsa data type hai?
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student)) # <class 'bool'>

# F-string se print
print(f"Name: {name} — Type: {type(name)}")
print(f"Age: {age} — Type: {type(age)}")
print(f"Height: {height} — Type: {type(height)}")
print(f"Student: {is_student} — Type: {type(is_student)}")
