#!/usr/bin/python3
"""tracking the iss using api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()
    iss_people = {}
    num_people = 0
    ## display our Pythonic data
    # print("\n\nConverted Python data")
    # print(helmetson)

    # print('\n\nPeople in Space: ', helmetson['number'])
    # people = helmetson['people']
    # print(people)
    
    for peoples in helmetson['people']:
        if peoples['craft'] == "ISS":
            iss_people[num_people] = peoples
            num_people += 1
    
    print(f"People on ISS: {num_people}")

    for peoples in iss_people:
        print(f"{iss_people[peoples]['name']} on the {iss_people[peoples]['craft']}")


if __name__ == "__main__":
    main()
