# ================================
# LESSON 5: Loops
# ================================

# FOR LOOP — jab pata ho kitni baar chalana hai
# Bash mein: for i in 1 2 3 4 5; do

print("--- For Loop ---")
for i in range(1, 6):
    print(f"Number: {i}")

# range(1, 6) = 1 se 5 tak (6 shamil nahi)

print("")

# WHILE LOOP — jab condition true ho tab tak chalo
# Bash mein: while [ $count -lt 5 ]; do

print("--- While Loop ---")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count = count + 1   # count badhaao, warna infinite loop!
