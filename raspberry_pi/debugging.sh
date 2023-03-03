#!/bin/bash

# Wifi
wifi="Carson"
wifi_psk="yooser00"
tello="TELLO-603F31"
# Debug code
code="/home/carsonchampie/Desktop/Robotics/Code/examples/takeoff.py"
base=${code##*/}
dir=/home/carsonchampie/Desktop/Robotics/Code/examples/

nmcli dev wifi connect ${tello}

cd ${dir} || exit
python ${base}

nmcli dev wifi connect ${wifi} password ${wifi_psk}
