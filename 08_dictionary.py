# ================================
# LESSON 8: Dictionary
# ================================

# Dictionary banana — key: value
person = {
    "name": "Ramzan",
    "age": 22,
    "city": "Multan",
    "job": "DevOps Engineer"
}

# Value nikalo key se
print(person["name"])
print(person["age"])

# F-string se print
print(f"Naam: {person['name']}, Shehar: {person['city']}")

# Naya key-value add karo
person["country"] = "Pakistan"
print(f"Country add karne ke baad: {person}")

# Sari keys dekho
print(f"Keys: {person.keys()}")

# Sari values dekho
print(f"Values: {person.values()}")

# Loop se sab print karo
print("\n--- Poori Dictionary ---")
for key, value in person.items():
    print(f"  {key}: {value}")
