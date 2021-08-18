#from picamera import PiCamera
import errno
import os
import sys
from datetime import datetime
from time import sleep
import configparser

dir = sys.path[0]
config_path = os.path.join(sys.path[0], "watchdog.config")
config = configparser.ConfigParser()
config.read(config_path)

def daymin_now_val():
    a = datetime.now()
    daymin = (a.hour * 60) + a.minute
    return daymin

def time2daymin_val(time):
    hm = time.split(":")
    daymin = int((int(hm[0])*60) + int(hm[1]))
    return daymin

#Video Settings
reboot_bool = config.get('Timing', 'reboot_routine')
reboot_time = eval(config.get('Timing', 'reboot_time'))

shutdown_bool = config.get('Timing', 'shutdown_routine')
shutdown_time = eval(config.get('Timing', 'shutdown_time'))


while True:
    #epoch for interval
    #timer Boolean
    #epoch2000 = (datetime.now() - datetime(2000, 1, 1)).total_seconds()
    if ( (shutdown_bool == 'True') ):
        for key, value in shutdown_time.items():
            if (daymin_now_val()==time2daymin_val(value)):
                cmdSht = 'sudo shutdown now'
                os.sytem(cmdSht)

    if ( (reboot_bool == 'True') ):
        for key, value in reboot_time.items():
            if (daymin_now_val()==time2daymin_val(value)):
                cmdRbt = 'sudo reboot'
                os.sytem(cmdRbt)

    sleep(1)
