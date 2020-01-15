import pygame as pg
from mutage.mp3 import MP3 as MP3
from pygame.locals import *
import RPi.GPIO as GPIO
import requests
import json
import time
import random

url = "http://localhost:8888"
header = {"content-type": "application/json"}

rains = ["大雨", "洪水", "暴風"]
tsunami = ["津波注意報", "津波警報", "大津波警報"]
earthquake = ["4", "5弱", "5強", "6弱", "6強", "7"]
apis = ["/rain", "/tsunami", "/earthquake", "/volcano"]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pg.init()
screen = pg.display.set_mode((800, 480))
pg.display.set_caption("Full Menu")
enfont = pg.font.SysFont(None, 50)
jpfont = pg.font.SysFont("Droid Sans Fallback", 30)

def play_music(filename):
    pg.mixer.init()
    pg.mixer.music.load(filename)
    mp3_length = mp3(filename).info.length()
    pg.mixer.music.play(1)
    time.sleep(mp3_length + 0.01)
    pg.mixer.music.stop()
    return

def alarm(filename):
    for _ in range(2):
        play_music("siren.mp3")
    play_music(filename)

def light_off(button):
    if button:
        GPIO.output(38, GPIO.LOW)

def light_on(button):
    if button:
        GPIO.output(38, GPIO.HIGH)

def create_payload(api, res):
    payload = "危険! : "
    if api == "/rain":
        payload += res['type']
    elif api == "/tsunami":
        payload += res['type']
    elif api == "/volcano":
        payload += res['type']
    elif api == "/earthquake":
        payload += "震度 {}".format(res['level'])
    return payload

def create_screen(api, res, isWarning):
    if isWarning:
        payload = create_payload(api, res)       
    else:
        payload = "平和"
    screen.fill((255, 255, 255))
    text = jpfont.render(payload, True, (0, 0, 0))
    pg.display.update()
    return

def main():
    while True:
        api = random.choice(apis)
        r = requests.get(url+api, headers=header)
        res = r.json()
        print("[*] api response({}) : {}".format(api, res))

        if api == "/earthquake":
            create_screen(api, res, True)
            print("[!] type: {}, level: {}".format(res['type'], res['level']))
            print("    if you want to stop, you shold push the button")
            light_on(True)
            while GPIO.input(40) != GPIO.HIGH:
                play("地震5.mp3")
                light_off(False)
            print("[*] you pushed the button")
            light_off(True)
        elif res['level'] >= 3:
            create_screen(api, res, True)
            print("[!] type: {}, level: {}".format(res['type'], res['level']))
            print("    if you want to stop, you shold push the button")
            light_on(True)
            while GPIO.input(40) != GPIO.HIGH:
                play("地震5.mp3")
                light_off(False)
            print("[*] you pushed the button")
            light_off(True)
        else:
            create_screen(api, res, False)
        time.sleep(5)

if __name__=="__main__":
    main()
