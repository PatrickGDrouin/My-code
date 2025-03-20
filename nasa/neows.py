#!/usr/bin/python3
import requests
from dotenv import load_dotenv
import os

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    #with open("/home/student/nasa.creds", "r") as mycreds:
     #   nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    load_dotenv()
    nasacreds = os.getenv("NASA_API_KEY")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = ("start_date=" + input("enter a start date(yyyy-mm-dd):"))
    if input("would you like to enter an end dat(y/n): ") == "y":
        enddate = ("end_date" + input("enter an end date(yyyy-mm-dd): "))
        neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    else:# make a request with the request library
        neowrequest = requests.get(NEOURL + startdate + "&API_KEY=" + nasacreds)
        print(neowrequest)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

