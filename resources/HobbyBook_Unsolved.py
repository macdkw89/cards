# @TODO: Your code here
myDict = {
    "name": "Arlo", 
    "age": 3.5, 
    "hobbies": ["fetching", "eating", "sleeping"],
    "wakeup": {"early": "8:00am", "late": "10:30am"}}

#blank print for console clarity
print()

print(f"{myDict['name']} is {myDict['age']} years old") 
print(f"{myDict['name']} has {len(myDict['hobbies'])} hobbies")
print(f"{myDict['name']}\'s favorite hobby is {myDict['hobbies'][1]}")
print(f"He wakes up at {myDict.get('wakeup')['early']}")

