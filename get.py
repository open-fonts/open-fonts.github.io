import requests
import zipfile
import json

ghUrl = "https://raw.githubusercontent.com/honeysilvas/google-fonts/dev/json/google-web-font-list-sorted-by-popularity.json"
fontsData = requests.get(ghUrl, headers = {"Accept": "application/json"}).json()

fonts = fontsData['items']
baseUrl = "https://fonts.google.com/download?family="

for i in range(1000):
    if i % 100 == 0:
        print(i)
    font = fonts[i]["family"]
    fontName = fonts[i]["family"]
    getUrl = baseUrl + font
    r = requests.get(getUrl)

    zipfileName = "zips/" + fontName + '.zip'

    with open(zipfileName, "wb") as f:
        f.write(r.content)

    with zipfile.ZipFile(zipfileName, 'r') as zip_ref:
        zip_ref.extractall('fonts/' + fontName)
