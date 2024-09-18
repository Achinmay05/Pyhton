d = {} # empty dictionary

marks = {
    "chinmay": 90,
    "Somu": 100,
    "Ghidorah": 150,
    "John": 200
}
# print(marks.items())
# print(marks.keys())
print(marks.values())
marks.update({"chinmay": 250, "MR. Wick": 1500}) # if the key values pair is absent in the dictionary they get added, and existing gets updated

# print(marks.items())

print(marks.get("MR. Wick")) # if the given key is absent this line returns none 
print(marks["MR. Wick"]) # if the given key is absent this line gives error

