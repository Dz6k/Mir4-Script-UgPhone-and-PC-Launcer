import win32con
from threading import Thread
from win32gui import SendMessage, FindWindow
from random import randint, choice
from mousekey import MouseKey
from time import sleep
from pywinauto import Application

# variables
POSSIBILITIES = 1.75, 2, 2.25, 2.5, 2.75, 3


def stealthfarm(game, ultimate=False):
    mkey = MouseKey()
    mkey.enable_failsafekill('ctrl+e')

    window_name = f'{game}'
    hwnd = FindWindow(None, window_name)

    SendMessage(hwnd, win32con.WM_KEYDOWN, 0x42, 0)
    sleep(0.01)
    SendMessage(hwnd, win32con.WM_KEYUP, 0x42, 0)
    sleep(0.2)

    while True:
        SendMessage(hwnd, win32con.WM_KEYDOWN, 0x09, 0)
        sleep(0.1)
        SendMessage(hwnd, win32con.WM_KEYUP, 0x09, 0)

        for i in range(randint(2, 4)):
            SendMessage(hwnd, win32con.WM_KEYUP, 0x21, 0)
            sleep(0.01)
            SendMessage(hwnd, win32con.WM_KEYDOWN, 0x21, 0)

        sleep(0.3)
        SendMessage(hwnd, win32con.WM_KEYDOWN, 0x46, 0)
        sleep(0.01)
        SendMessage(hwnd, win32con.WM_KEYUP, 0x46, 0)

        SendMessage(hwnd, win32con.WM_KEYDOWN, 0x09, 0)
        sleep(0.1)
        SendMessage(hwnd, win32con.WM_KEYUP, 0x09, 0)
        sleep(choice(POSSIBILITIES))
        if ultimate == True:
            SendMessage(hwnd, win32con.WM_KEYDOWN, 0x52, 0)
            sleep(0.01)
            SendMessage(hwnd, win32con.WM_KEYUP, 0x52, 0)

    SendMessage(hwnd, win32con.WM_KEYDOWN, 0x42, 0)
    sleep(0.01)
    SendMessage(hwnd, win32con.WM_KEYUP, 0x42, 0)


# def stealthfarm(game):
#    mkey = MouseKey()
#    mkey.enable_failsafekill('ctrl+e')
#    window_name = f'{game}'
#    hwnd = FindWindow(None, window_name)
#    win = CreateWindowFromHandle(hwnd)
#
#    SendMessage(hwnd,win32con.WM_KEYDOWN, 0x42, 0)
#    sleep(0.01)
#    SendMessage(hwnd,win32con.WM_KEYUP, 0x42, 0)
#    sleep(0.2)
#
#    while not stop_threads:
#        SendMessage(hwnd,win32con.WM_KEYDOWN, 0x09, 0)
#        sleep(0.1)
#        SendMessage(hwnd,win32con.WM_KEYUP, 0x09, 0)
#
#        for i in range(randint(2, 4)):
#            SendMessage(hwnd,win32con.WM_KEYUP, 0x21, 0)
#            sleep(0.01)
#            SendMessage(hwnd,win32con.WM_KEYDOWN, 0x21, 0)
#
#        sleep(0.3)
#        SendMessage(hwnd,win32con.WM_KEYDOWN, 0x46, 0)
#        sleep(0.01)
#        SendMessage(hwnd,win32con.WM_KEYUP, 0x46, 0)
#
#        SendMessage(hwnd,win32con.WM_KEYDOWN, 0x09, 0)
#        sleep(0.1)
#        SendMessage(hwnd,win32con.WM_KEYUP, 0x09, 0)
#        sleep(choice(POSSIBILITIES))
#    SendMessage(hwnd,win32con.WM_KEYDOWN, 0x42, 0)
#    sleep(0.01)
#    SendMessage(hwnd,win32con.WM_KEYUP, 0x42, 0)


# def start():
#    process = []
#    for indice in range(0, 16):
#        try:
#            app = Application().connect(title=f'Mir4G[{indice}]')
#            app_text = app.window().texts()
#            process += app_text
#        except:
#            ...
#
#    for i in process:
#        thread_name = f"MyThread-{i}"
#        farm = Thread(
#            target=stealthfarm, args=(i,), name=thread_name)
#
#        farm.start()
#
# start the funcion with ultimate


def start():

    process = []
    for indice in range(0, 16):
        try:
            app = Application().connect(title=f'Mir4G[{indice}]')
            app_text = app.window().texts()
            process += app_text
        except:
            ...

    for i in process:
        thread_name = f"MyThread-{i}"
        farm = Thread(
            target=stealthfarm, args=(i, True,), name=thread_name)

        farm.start()


start()
