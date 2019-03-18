#!/bin/sh
sudo service hostapd stop
sleep 5s
sudo service networking restart
sleep 10s
sudo service hostapd start

