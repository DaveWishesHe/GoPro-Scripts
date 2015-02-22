import urllib, sys, getopt
from lxml import html
from os.path import expanduser

def main(argv):
    url = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/"
    destination = expanduser("~")
    extension = ".MP4"
    try:
        opts, args = getopt.getopt(argv, "hvd:e:", ["help", "verbose", "destination=", "extension="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-v", "--verbose"):
            global _verbose
            _verbose = 1
	elif opt in ("-d", "--destination"):
            destination = arg
        elif opt in ("-e", "--extension"):
            extension = arg
        
    page = html.fromstring(urllib.urlopen(url).read())
    for link in page.xpath("//a"):
        file = url + link.get("href")
        if file.endswith(extension):
            basic_download(file, destination + link.text)

# TODO: Implement user help
def usage():
      print "Huh?"

def basic_download(source, destination):
    print "Downloading", source, "To", destination
    urllib.urlretrieve(source, destination)

# TODO: Implement swanky progress bar
def verbose_download(source, destination):
    # Check this out: http://stackoverflow.com/a/22776
    print "Not Implemented."

if __name__ == "__main__":
    main(sys.argv[1:])
