#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint
import json

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
house = {}

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
        belongto = []
        inbook = []
        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        #                  ^ this method already converted the json data to python, so no need for the json library with this one
        for houses in got_dj['allegiances']:
            house = requests.get(houses).json()
            belongto.append(house['name'])
        for houses in got_dj['books']:
            book = requests.get(houses).json()
            inbook.append(book['name'])
        print(f"{got_dj['name']} belong to the following houses: ")
        for houses in belongto:
            print(houses)
        print(f"{got_dj['name']} appeared in the following books:")
        for books in inbook:
            print(books)

if __name__ == "__main__":
        main()

