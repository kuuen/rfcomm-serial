#!/bin/sh
sudo echo 26 > /sys/class/gpio/export
sleep 1s
sudo echo out > /sys/class/gpio/gpio26/direction
sleep 1s
sudo echo 1 > /sys/class/gpio/gpio26/value

