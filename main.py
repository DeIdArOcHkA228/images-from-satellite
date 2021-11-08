import requests
from pathlib import Path


filename = 'images/satellite.jpeg'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

Path("images/").mkdir(parents=True, exist_ok=True)





def installing_pictures(picture_url, path):
    response = requests.get(picture_url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
test = installing_pictures(url, filename)
