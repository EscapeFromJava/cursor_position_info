import threading
import time
import tkinter as tk

import pyautogui
import pyscreeze

running = True


def get_position():
    global running
    while running:
        x, y = pyautogui.position()
        pixel_color = pyscreeze.screenshot().getpixel((x, y))
        cursor_info = ("X: " + str(x) + " Y: " + str(y) + " RGB: (" + str(pixel_color[0]).rjust(3) + ", " + str(
            pixel_color[1]).rjust(3) + ", " + str(pixel_color[2]).rjust(3) + ")")
        label.config(text=cursor_info)
        time.sleep(0.01)


def on_closing():
    global running
    running = False
    time.sleep(0.2)
    root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Coord")
    root.geometry("220x20")

    root.attributes("-topmost", True)

    label = tk.Label(root)
    label.pack(expand=True)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    threading.Thread(target=get_position, daemon=True).start()

    root.mainloop()
