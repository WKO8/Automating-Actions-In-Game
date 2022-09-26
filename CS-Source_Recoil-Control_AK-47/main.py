# Coded by W_K.O
# https://github.com/WKO8


# Function to control the AK-47 spray automatically
def send():
    # Importing used libraries
    from pynput.mouse import Button, Controller
    from time import sleep
    
    mouse = Controller()
    mouse.press(Button.left)
    sleep(0.3)
    mouse.move(0, 5000)
    sleep(0.3)
    mouse.move(0, 100)
    mouse.move(20, 0)
    sleep(0.3)
    mouse.move(0, 100)
    mouse.move(20, 0)
    sleep(0.3)
    mouse.move(0, 50)
    sleep(2)
    mouse.release(Button.left)

# Importing Pynput Library for Keyboard Listening
from pynput.keyboard import Listener, Key

def press(key):
    if key == Key.f3:
        send()
    elif key == Key.pause:
        return

# Stop function
def release(key):
    if key == Key.pause:
        return False
        exit()
    print(key)

# Keyboard Listening Activator
with Listener(on_press=press, on_release=release) as listener:
    listener.join()

