import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_269974.json'

uh = urllib.urlopen(serviceurl)
data = uh.read()
js = json.loads(str(data))

info = js['comments']

count = 0
for item in info:
	count = count + int(item['count'])

print count
