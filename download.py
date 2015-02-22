import urllib
from lxml import html

destination = "/home/dave/Pictures/2015-02/"

url = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/"
page = html.fromstring(urllib.urlopen(url).read())

for link in page.xpath("//a"):
    file = url + link.get("href")
    if file.endswith(".MP4"):
        print "Downloading", file, "To", destination + link.text 
        urllib.urlretrieve(file, destination + link.text)
