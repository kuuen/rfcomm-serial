#!/bin/sh
sudo echo 0 > /sys/class/gpio/gpio26/value
sleep 1s
sudo echo 26 > /sys/class/gpio/unexport
