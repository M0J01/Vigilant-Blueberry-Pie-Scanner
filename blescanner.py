from bluepy.btle import Scanner, DefaultDelegate
from time import gmtime, strftime
import time
import datetime

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

'''
	def handleDiscovery(self, dev, isNewDev, isNewData):
		if isNewDev:
			#print "Discovered Device", dev.addr
		elif isNewData:
			#print "Received new data from", dev.addr
'''


while(1):
	blog = open("scanned_devices.txt", 'a')
	#curTime = datetime.datetime.now()
	curTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	scanner = Scanner().withDelegate(ScanDelegate())
	devices = scanner.scan(5.0)

	for dev in devices:
		if  (len(dev.getScanData()) > 2):
			blog.write(curTime)
			blog.write(" :: Device %s (%s), RSSI=%d dB, " % (dev.addr, dev.addrType, dev.rssi))
			#print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
			for (adtype, desc, value) in dev.getScanData():
				#print " %s = %s" % (desc, value)
				blog.write(" %s = %s, " % (desc, value))
			blog.write("\n")
	blog.close()
	print strftime
	print "... Scan complete, going to sleep... \n"
	time.sleep(60)
