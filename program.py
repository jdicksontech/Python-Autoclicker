import ctypes
import time
import keyboard
from pynput import mouse

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

running = True
active = False

def click():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.01)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def on_press(x, y, button, pressed):
    global active
    if button == mouse.Button.x2:
        if pressed:
            active = True
            # print("Active: ON")
        else:
            active = False
            # print("Active: OFF")

def stop():
    global running
    running = False

listener = mouse.Listener(on_click=on_press)
listener.start()

keyboard.add_hotkey('f9', stop)

print("Ready. Hold X2 to autoclick, release to stop. F9 to quit.")

while running:
    if active:
        click()
        time.sleep(0.000001)
    time.sleep(0.005)

listener.stop()