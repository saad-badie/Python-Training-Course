import requests
import sys

if len(sys.argv) != 2:
	sys.exit()
	
response = requests.get("https://itunes.apple.com/search?entity=song&limit=30&term=" + sys.argv[1])
print(response.json())
