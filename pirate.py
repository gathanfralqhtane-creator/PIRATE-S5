import os
import sys
import time

# ألوان
R = '\033[1;31m' # أحمر
G = '\033[1;32m' # أخضر
Y = '\033[1;33m' # أصفر
W = '\033[0m'    # أبيض

def clear():
    os.system('clear')

def logo():
    print(R + """
      .---.              .-----------.
     /     \    __      /    .---.    \ 
    / /     \  (  )    /    /     \    \ 
   //////    ' \/ `   //////      |
  //// [  PIRATE-S1  ] ////       |
 //////      (☠️ )    //////       /
      `----------'            /
     _______WIFI-DEVIL_______/
    """ + Y + """
   [☠️ ] Dev: Gathan (THE-DEVIL)
   [☠️ ] Tool: Wifi Hunter S1
   -----------------------------------------
    """ + W)

def main():
    clear()
    logo()
    print(G + "[1] " + W + "بيانات الشبكة (IP/Gateway) + استخراج الرمز")
    print(G + "[2] " + W + "كشف الشبكات المخفية واستخراج رموزها")
    print(G + "[3] " + W + "إنشاء نقطة وهمية (Evil Twin) لصيد الأجهزة")
    print(R + "[4] " + W + "خروج")
    
    choice = input("\n" + R + "[PIRATE@WIFI]:# " + W)
    
    if choice == '1':
        print(Y + "\n[*] جلب البيانات..." + W)
        os.system("ip route show | grep default")
        os.system("ifconfig wlan0 | grep inet")
        print(R + "[!] محاولة سحب الرمز (يحتاج Root)..." + W)
        os.system("su -c 'cat /data/misc/wifi/wpa_supplicant.conf | grep psk'")
        input("\nاضغط Enter للعودة..."); main()
        
    elif choice == '2':
        print(Y + "\n[*] جاري البحث عن الشبكات المخفية (Monitor Mode)..." + W)
        os.system("airodump-ng wlan0")
        input("\nاضغط Enter للعودة..."); main()
        
    elif choice == '3':
        ssid = input(Y + "اسم الشبكة الوهمية: " + W)
        pw = input(Y + "الرمز المختار: " + W)
        print(R + f"\n[!] تم إطلاق {ssid}.. بانتظار الضحايا..." + W)
        os.system(f"nmcli dev wifi hotspot ssid {ssid} password {pw}")
        input("\nاضغط Enter للإغلاق..."); main()
        
    elif choice == '4':
        sys.exit(R + "\nالشيطان يحييك.. إلى اللقاء." + W)
    else:
        main()

if __name__ == "__main__":
    main()
  
