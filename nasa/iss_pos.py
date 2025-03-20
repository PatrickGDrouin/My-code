import requests
import reverse_geocoder as rg

URL = "http://api.open-notify.org/iss-now.json"

iss_pos = requests.get(URL).json()

lat= iss_pos['iss_position']['latitude']
lon= iss_pos['iss_position']['longitude']

# reverse_geocoder MUST be passed a tuple as the argument!
coords_tuple= (lat, lon)

result = rg.search(coords_tuple, verbose=False)
                                 # verbose=False removes an annoying output that reads
                                 # "Loading formatted geocoded file..."
print(f"latitude of ISS is: {result[0]['lat']}")
print(f"Longitude of ISS is: {result[0]['lon']}")
print(f"City/Country os ISS: {result[0]['name']}, {result[0]['cc']}")
print(f"Timestamp is: {iss_pos['timestamp']}")


