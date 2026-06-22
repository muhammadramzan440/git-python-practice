# ================================
# LESSON 9: File Handling
# ================================

# PART 1: File mein likhna (write mode)
with open("test.txt", "w") as f:
    f.write("Mera naam Ramzan hai\n")
    f.write("Main Multan se hoon\n")
    f.write("Main DevOps seekh raha hoon\n")

print("File likh di!")

# PART 2: File padhna (read mode)
with open("test.txt", "r") as f:
    content = f.read()

print("File ka content:")
print(content)

# PART 3: File mein add karna (append mode)
with open("test.txt", "a") as f:
    f.write("Python bhi seekh raha hoon\n")

print("Nai line add kar di!")

# PART 4: Line by line padhna
with open("test.txt", "r") as f:
    lines = f.readlines()

print("Line by line:")
for line in lines:
    print(f"  {line.strip()}")
# .strip() = line ke aakhir ka \n hatao
