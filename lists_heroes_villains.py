#!/usr/bin/env python3

# Original lists
marvel_heroes = ["Iron Man", "Captain America", "Thor", "Black Widow", "Hulk"]
marvel_villains = ["Thanos", "Loki", "Ultron", "Hela", "Red Skull"]
dc_heroes = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman"]
dc_villains = ["Joker", "Lex Luthor", "Darkseid", "Cheetah", "Reverse Flash"]

# Empty list to hold combined data
full_list = []

# Combine the heroes and villains
combined_heroes = []
combined_heroes.extend(marvel_heroes)
combined_heroes.extend(dc_heroes)
combined_heroes.insert(1, "rocket")

combined_villains = []
combined_villains.extend(marvel_villains)
combined_villains.extend(dc_villains)
combined_villains.insert(2, "sandman")

# Append combined lists to the full list
full_list.append(combined_heroes)
full_list.append(combined_villains)

# Print statements
print(full_list)
print("Just the heroes:", full_list[0])
print("Just the villains:", full_list[1])
print("First character from the first list:", full_list[0][0])  # "Iron Man"
print("Last character from the last list:", full_list[1][-1])  # "Reverse Flash"
print(f"The second hero: {combined_heroes[1]}")
print(f"the third villain: {combined_villains[2]}")


