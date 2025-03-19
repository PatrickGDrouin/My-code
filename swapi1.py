#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

# The following URL is constructed incorrectly. It should be api/people/4/
char_URL= "https://swapi.dev/api/people/4/"
film_URL= "https://swapi.dev/api/films/1/"
ship_URL= "https://swapi.dev/api/starships/13/"

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    char_resp= requests.get(char_URL)
    film_resp= requests.get(film_URL)
    ship_resp= requests.get(ship_URL)

    if char_resp.status_code == 200 and film_resp.status_code == 200 and ship_resp.status_code == 200:
        # convert the JSON content of the response into a python dictionaryi
        vader= char_resp.json()
        film= film_resp.json()
        ship= ship_resp.json()
        print(f"{vader['name']} was born in the year {vader['birth_year']}. His eyes are now {vader['eye_color']} and his hair color is {vader['hair_color']}")
        print(f"He first appeared in the movie {film['title']} and could be found flying around in his {ship['name']}")
    else:
        print(f"{URL}: is not a valide URL")

if __name__ == "__main__":
    main()
