# GoPro-Scripts

Bought a GoPro, having an absolute nightmare trying to get it to just work with Fedora, so this is where I'll be storing any handy scripts I write to help make life easier.

## download.py

This one will download all files (over WiFi) from a given directory on the GoPro to a given directory on your local machine.

There's some setup required.

# You'll need a GoPro with WiFi. I think the Hero 3 and 4 have this feature, maybe the Hero 2 as well.
# Enable and connect to the WiFi from your local machine - the GoPro Wifi show up as a normal WiFi network. More details in this handy YouTube video - https://www.youtube.com/watch?v=-dTyxSQZPro
# Once connected, set the `destination` variable in the script to the location that you want the files to download to.
# Run the script

That's it, your files will (slowly) download over the GoPro Wifi, helping you avoid all the pesky USB dropping out errors when trying to copy the files any other way.

### Hat Tips

# http://stackoverflow.com/a/4492108
