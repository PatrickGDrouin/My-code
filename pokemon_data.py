#!/usr/bin/env python3

# Pikachu dictionary
pikachu = {"name": "Pikachu", "type": "Electric", "level": 25}
pikachu["trainer"] = "ash"
print(pikachu)

# Geodude dictionary with a list for types
geodude = {"name": "Geodude", "types": ["Rock", "Ground"], "level": 16}

# List of starter Pokémon dictionaries
starters = [
{"name": "Bulbasaur", "type": ["Grass", "poison"], "level": 5},
{"name": "Squirtle", "type": "Water", "level": 5},
{"name": "Charmander", "type": "Fire", "level": 5},
]
print(starters[0])

# Print statements
print(f"{pikachu['name']} is a level {pikachu['level']} Pokémon.")
print(f"{geodude['name']}'s first type is {geodude['types'][0]}.")
print(f"{starters[2]['name']} is a {starters[2]['type']} type starter.")
print(list(geodude.values()))
