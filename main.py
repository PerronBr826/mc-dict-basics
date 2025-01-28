# Mountain Range Dict.

mountain_ranges = {
    "Himalayan" : 8848,
    "Andes" : 6962,
    "Rocky" : 4401,
    "Alps" : 4807,
    "Atlas" : 4167,
}

for key, value in mountain_ranges.items():
    print(f"The {key} mountains are {value} meters tall.")
    print(f"The current mountain range's name is \"The {key} Mountains\"")
    print(f"The current mountain's height is {value}.")