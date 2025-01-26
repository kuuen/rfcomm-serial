#!/bin/sh

# bluetoothでSPP通信の待受をおこなう
#while true
#  do
#    sudo rfcomm listen /dev/rfcomm0 22
#done

sudo rfcomm watch /dev/rfcomm0 22 python3 /home/cito/work/python/rfcomm/bluetooth-serial.py

