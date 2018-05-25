import time
from glob import glob
import platform

from pydobot import Dobot

def load():
    if platform.system() == "Windows":
        pass
    elif platform.system() == "Darwin" :
        available_ports = glob('/dev/cu*usb*')  # mask for OSX Dobot port
    else:
        available_ports = glob('/dev/ttyUSB*')  # mask for Raspi Dobot port


if len(available_ports) == 0:
    print('no port found for Dobot Magician')
    exit(1)

device = Dobot(port=available_ports[0])

time.sleep(0.5)
device.speed(50)
device.go(250.0, 0.0, 25.0)
device.speed(50)
device.go(250.0, 0.0, 0.0)
device.speed(50)
device.go(250.0, 0.0, 25.0)
device.speed(50)
device.go(250.0, 0.0, 0.0)
device.speed(50)
device.go(250.0, 0.0, 25.0)
device.speed(50)
device.go(250.0, 0.0, 0.0)
time.sleep(2)
device.close()
