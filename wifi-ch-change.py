#coding:utf-8

import sys
import argparse
import re
import shutil
import os
import subprocess

FILE_TEMPLATE = r"/etc/hostapd/hostapd2.4G.conf.Template"
FILE_CONF = r"/etc/hostapd/hostapd2.4G.conf"
FILE_OLD = r"/etc/hostapd/hostapd2.4G.conf.old"

try:

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--channel', help='チャンネルを指定1〜12、14' ,required=True)
    args = parser.parse_args()

    channel = args.channel

#    if re.search(r'^[1-9]$|^1[0-2]$|14', args.channel) == None:
    # チャンネル1-13の間を指定 14だとうまく動かなかった
    if re.search(r'^[1-9]$|^1[0-3]$', args.channel) == None:
        print('Channel specification error :' + str(channel))
        quit()

    if os.path.exists(FILE_OLD):
        os.remove(FILE_OLD)

    shutil.move(FILE_CONF, FILE_OLD)

    with open(FILE_TEMPLATE, "r",encoding="utf-8") as file:
        filedata = file.read()
        filedata = filedata.replace('{*1*}', channel)

    with open(FILE_CONF, "w",encoding="utf-8") as file:
        file.write(filedata)

    subprocess.check_output(['sudo', 'systemctl', 'restart', 'hostapd.service'], stderr=subprocess.STDOUT)

except Exception as e:
#    print(e)
    sys.exit(e)

sys.exit(0)
