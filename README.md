# GoPro-Scripts

Bought a GoPro, having an absolute nightmare trying to get it to just work with Fedora, so this is where I'll be storing any handy scripts I write to help make life easier.

2015-02-22 Cont.: Decided to make the download script more exciting with optional flags and arguments! Have copied "download.py" to "simple_download.py" because it's still perfectly functional, and speaking as a novice python user, if people are looking for examples of how to do stuff, I reckon the simple one is a much less daunting place to start.
2015-02-22: Just the one script so far; download.py. I'm sure there will be more coming in the future.

## Downloads

These scripts will download all files (over WiFi) from a given directory on the GoPro to a given directory on your local machine.

Whichever script you run, there's some setup required.

* You'll need a GoPro with WiFi. I think the Hero 3 and 4 have this feature, maybe the Hero 2 as well.
* Enable and connect to the WiFi from your local machine - the GoPro Wifi show up as a normal WiFi network. More details in this handy YouTube video - https://www.youtube.com/watch?v=-dTyxSQZPro

Whichever script you run, your files will (slowly) download over the GoPro Wifi helping you avoid all the pesky USB dropping out errors when trying to copy the files any other way.

### simple_download.py

This script is basic, and has a small amount of feedback. If you use this one, you'll need to set the `destination` variable in the file to the location that you want the files to download to.

That's it, your files will (slowly) download over the GoPro Wifi, helping you avoid all the pesky USB dropping out errors when trying to copy the files any other way.

### download.py

WORK IN PROGRESS

This script does everything the simple_download.py one does, except it takes optional arguments to stop you having to edit the script directly. It's not finished yet, check the TODOs in the file.

### Hat Tips

* https://www.youtube.com/watch?v=-dTyxSQZPro
* http://stackoverflow.com/a/4492108
* http://stackoverflow.com/a/22776
