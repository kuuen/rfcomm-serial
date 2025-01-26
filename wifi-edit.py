#coding:utf-8

import sys
import argparse
import re
import shutil
import os
import subprocess

FILE_TEMPLATE = r"/etc/wpa_supplicant/wpa_supplicant.conf.edit"
FILE_CONF = r"/etc/wpa_supplicant/wpa_supplicant.conf"
FILE_OLD = r"/etc/wpa_supplicant/wpa_supplicant.conf.old"

try:

    parser = argparse.ArgumentParser()
    parser.add_argument('-ssid', '--ssid', help='ssid' ,required=True)
    parser.add_argument('-password', '--password', help='password' ,required=True)
    args = parser.parse_args()

    ssid = args.ssid
    password = args.password

    if os.path.exists(FILE_OLD):
        os.remove(FILE_OLD)

    shutil.move(FILE_CONF, FILE_OLD)

    with open(FILE_TEMPLATE, "r",encoding="utf-8") as file:
        filedata = file.read()
        filedata = filedata.replace('[ssid]', ssid)
        filedata = filedata.replace('[password]', password)

    with open(FILE_CONF, "w",encoding="utf-8") as file:
        file.write(filedata)

    #subprocess.check_output(['sudo', 'systemctl', 'restart', 'hostapd.service'], stderr=subprocess.STDOUT)

except Exception as e:
#    print(e)
    sys.exit(e)

sys.exit(0)
