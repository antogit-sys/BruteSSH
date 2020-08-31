#!/bin/bash

sudo apt install -y figlet crunch ncrack #debian based
clear
sudo pacman -S --noconfirm figlet crunch ncrack #arch based
clear
sudo yum -y install figlet crunch ncrack #centos based
clear
dnf install -y figlet crunch ncrack #fedora based
clear
chmod a+x brutessh.py
echo "+-------------+"
echo "|END INSTALL  |"
echo "+-------------+"
sleep 1.5
clear
