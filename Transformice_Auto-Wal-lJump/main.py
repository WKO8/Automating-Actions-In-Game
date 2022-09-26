# Coded by W_K.O
# https://github.com/WKO8

# Function to send keyboard commands to automatically wall jump
def send_right():
    # Importing used libraries
    # Pynput to Control the Keyboard
    # Time to delay between one command and another
    from pynput.keyboard import Key, Controller
    from time import sleep

    # Variables
    keyb = Controller()
    count = 0

    # Repeat to Right Auto Wall jump
    while count < 10:
        keyb.press("d")
        sleep(0.37)
        keyb.release("d")
        sleep(0.05)
        keyb.press("a")
        sleep(0.13)
        keyb.release("a")
        sleep(0.05)
        keyb.press("w")
        sleep(0.11)
        keyb.release("w")
        sleep(0.05)
        count += 1

def send_left():
    # Importing used libraries
    from pynput.keyboard import Key, Controller
    from time import sleep

    # Variables
    keyb = Controller()
    count = 0

    # Repeat to Left Auto Wall jump
    while count < 10:
        keyb.press("a")
        sleep(0.37)
        keyb.release("a")
        sleep(0.05)
        keyb.press("d")
        sleep(0.13)
        keyb.release("d")
        sleep(0.05)
        keyb.press("w")
        sleep(0.11)
        keyb.release("w")
        sleep(0.05)
        count += 1

# Importing Pynput Library for Keyboard Listening
from pynput.keyboard import Listener, Key

# Function to start and pause the program with hotkey
def press(key):
    if key == Key.f2:
        send_right()
    elif key == Key.f1:
        send_left()
    elif key == Key.ctrl_r:
        return

# Stop function
def release(key):
    if key == Key.ctrl_r:
        return False
        exit()
    print(key)

# Keyboard Listening Activator
with Listener(on_press=press, on_release=release) as listener:
    listener.join()

