import os
import bluetooth

while 1:

    print("Searching ...")

    devices = bluetooth.discover_devices(duration=10, lookup_names=1, flush_cache=1)

    for device_address, device_name in devices:

        print("Found: {}".format(device_name))

        if (device_name.lower() == "chrisg"):
            os.system("mplayer /home/pi/imperial.mp3")