import requests
from pathlib import Path


filename = 'images/satellite.jpeg'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

Path("images/").mkdir(parents=True, exist_ok=True)

response = requests.get(url)
response.raise_for_status()

with open(filename, 'wb') as file:
    file.write(response.content)
