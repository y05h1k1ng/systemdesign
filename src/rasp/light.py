import RPi.GPIO as GPIO
import requests
import json
import time

url = "http://localhost:8888"
header = {"content-type": "application/json"}

rains = ["大雨", "洪水", "暴風"]
tsunami = ["津波注意報", "津波警報", "大津波警報"]
earthquake = ["4", "5弱", "5強", "6弱", "6強", "7"]


GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIIO.OUT)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def light_off(button):
    if button:
        GPIO.output(38, GPIO.HIGH)

def light_on(button):
    if button:
        GPIO.output(38, GPIO.LOW)

def main():
    while True:
        r = requests.get(url+"/rain", headers=header)
        res = r.json()
        print("[*] response :", res)
        if res['level'] >= 2:
            print("[!] type: {}, level: {}".format(res['type'], res['level']))
            print("    if you want to stop, you shold push the button")
            light_on(True)
            while GPIO.input(40) != GPIO.HIGH:
                light_off(False)
            light_off(True)
        time.sleep(1)

if __name__=="__main__":
    main()