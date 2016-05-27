import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_269970.xml'
print url
fhand = urllib.urlopen(url)
data = fhand.read()
#print data
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print 'User count:', len(lst)
count = 0
for el in lst:
	count = count + int(el.find('count').text)
print 'All count:', count
#for line in fhand:
#    print line.strip()
