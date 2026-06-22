# ================================
# LESSON 7: Lists
# ================================

# List banana
fruits = ["apple", "mango", "banana", "orange"]

# Poori list print karo
print("Poori list:", fruits)

# Index se ek item nikalo (0 se shuru)
print("Pehla fruit:", fruits[0])    # apple
print("Doosra fruit:", fruits[1])   # mango
print("Aakhri fruit:", fruits[-1])  # orange (-1 = aakhri)

# List ki length
print(f"Total fruits: {len(fruits)}")

# Loop se sab print karo
print("\n--- Sab fruits ---")
for fruit in fruits:
    print(f"  - {fruit}")

# List mein naya item add karo
fruits.append("grapes")
print(f"\nAdd karne ke baad: {fruits}")

# List se item delete karo
fruits.remove("banana")
print(f"Delete karne ke baad: {fruits}")
