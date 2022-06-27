# Create a Python list to store your grocery list
myList = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]

# Print the grocery list
print(myList)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list
myList[3] = "Almond Butter"

# Remove "Jelly" from grocery list and print out the updated list
myList.pop(-1)

# Add "Coffee" to grocery list and print the updated list
myList.append("Coffee")

print(myList)
print(len(myList))