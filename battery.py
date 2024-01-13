import psutil as ps
import time
from playsound import playsound
from pycaw.pycaw import AudioUtilities,ISimpleAudioVolume
# from pynput.keyboard import Key,Controller
# def volumeset():
#     currentvolume = AudioUtilities.
while True:
    battery = ps.sensors_battery()
    status = battery.power_plugged
    charge = battery.percent
    if(status == False and charge <= 50):
        playsound("batt.mp3")
        time.sleep(660)
    time.sleep(60)
