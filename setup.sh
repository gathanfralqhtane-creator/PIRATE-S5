#!/bin/bash
clear
echo -e "\e[1;31m"
figlet "INSTALLING"
echo -e "\e[1;33m[*] جاري تجهيز أدوات PIRATE-S1...\e[0m"
pkg update && pkg upgrade -y
pkg install python nmap aircrack-ng figlet ruby curl -y
gem install lolcat
chmod +x pirate.py
echo -e "\e[1;32m[+] التثبيت اكتمل! شغل الأداة بـ: python pirate.py\e[0m"
