import urllib.request as req

import json
import csv

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with req.urlopen(url) as resp:
	data = json.load(resp)

spots = data["result"]["results"]

with open("data.csv", mode="w", encoding="utf-8", newline="") as csvfile:
	for spot in spots:
		name = spot["stitle"]
		dist = spot["address"].split("  ")[1][0:3]
		lng = spot["longitude"]
		lat = spot["latitude"]
		pic = "https://" + spot["file"].split("https://")[1]

		writer = csv.writer(csvfile)
		writer.writerow([name, dist, lng, lat, pic])
