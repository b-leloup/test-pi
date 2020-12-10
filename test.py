import requests
from pynput.keyboard import Key, Listener

url = "http://127.0.0.1:8000/entry/"
mode = True
cap1 = True
cap2 = True
crossing = False

def on_press(key):
    None

def on_release(key):
    try:
        global cap1
        global cap2
        global mode
        global crossing
        if key.char == "s":
            cap1 = not cap1
            if mode and not cap1 and not crossing:
                crossing = True
            if not mode and cap1 and crossing:
                crossing = False
                requests.post(url, json={"isEntry": False})
        elif key.char == "e":
            cap2 = not cap2
            if not mode and not cap2 and not crossing:
                crossing = True
            if mode and cap2 and crossing:
                crossing = False
                requests.post(url, json={"isEntry": True})
        elif key.char == "m":
            mode = not mode
            crossing = False
    except AttributeError:
        if key == Key.esc:
            return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

