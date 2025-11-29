import keyboard
import time

def toggle_caps_lock():
    print("Caps Lock включен. Нажмите Ctrl+C для остановки.")
    print("Caps Lock is on. Press Ctrl+C to stop.")
    try:
        while True:
            keyboard.press_and_release('caps lock')
            time.sleep(2)
    except KeyboardInterrupt:
        print("Caps Lock")

if __name__ == "__main__":
    toggle_caps_lock()