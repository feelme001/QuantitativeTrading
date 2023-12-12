# Creating a list
fruits = ["apple", "banana", "orange", "grape"]

# Displaying the list
print("Fruits:", fruits)

# Accessing elements in a list
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying elements in a list
fruits[1] = "kiwi"
print("Updated fruits:", fruits)

# Adding elements to a list
fruits.append("pear")
print("Fruits with pear:", fruits)

# Looping through a list
print("Printing fruits:")
for fruit in fruits:
    print(fruit)
    
favorite_fruit = input("Enter your favorite fruit: ")
fruits.append(favorite_fruit)
print("Updated fruits:", fruits)