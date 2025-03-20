import requests

URL = "http://api.open-notify.org/iss-now.json"

iss_pos = requests.get(URL)
print(iss_pos)

