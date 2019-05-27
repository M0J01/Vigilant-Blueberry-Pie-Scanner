** Notes **
Designed to work with the Raspberry Pi Zero-W
You want to use the blescanner.py. The other scripts were not quite good enough for our purposes. 

blescanner.py scans for all bluetooth devices once every ~65  seconds, and records any that have more than 2 data points (So most devices that list a device name will show up)



** Requirements **
blescanner (<-- This is the one you want)
https://elinux.org/RPi_Bluetooth_LE
- sudo apt-get install python-pip
- sudo apt-get install libglib2.0-dev
- sudo pip install bluepy


Main
sudo apt-get install python-pexpect

Main2
sudo apt-get install libbluetooth-dev
sudo apt-get install bluez
sudo python3 -m pip install pybluez
sudo apt-get install ffmpeg
sudo python3 -m pip install youtube-dl
sudo apt-get install mplayer

Main5
https://pypi.org/project/beacontools/


