voting_data = [
    {"county":"Arapahoe", "registered_voters": 422829}, 
    {"county":"Denver", "registered_voters": 463353}, 
    {"county":"Jefferson", "registered_voters": 432438}]

#for i in voting_data:
#    print(f"{i['county']} county has {i['registered_voters']:,} registered voters.")
for i in voting_data:
    for j in i:
        print(f"Looks like {i['registered_voters']} has {j}")
