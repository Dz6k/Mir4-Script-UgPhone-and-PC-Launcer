################################################################################
#                                                                              #
#       ALL COORDENATES ARE RELATIVE TO WINDOW'S APLICATION!                   #
#    DON'T CHANGE THE DIMENSION, USE THE DEFALT WHEN YOU OPEN IT               #
#                                                                              #
################################################################################

import win32con
from win32api import MAKELONG
from time import sleep
from mousekey import MouseKey
from threading import Thread
from win32gui import SendMessage, GetWindowText, EnumWindows

# variables
mkey = MouseKey()
# FOR SAFE STOP, PRESS: CTRL + E
mkey.enable_failsafekill('ctrl+e')

# function to get all processes with name UgPhone
# (all instances of it have the same name, so I used it this way... it sends
# inputs to all instances because I couldn't find a better way to capture the
# specific screen of the process)


def find_window_by_title(title, index=0):

    def callback(hwnd, hwnds):
        if GetWindowText(hwnd) == title:
            hwnds.append(hwnd)
        return True

    hwnds = []
    EnumWindows(callback, hwnds)

    if index < len(hwnds):
        return hwnds[index]
    else:
        return None

# donate function


def donate(janela):
    hwnd = find_window_by_title('UgPhone', index=janela)
    for i in range(1):

        # open map (makelong convert the x,y coordenates in float)
        click_guild = MAKELONG(544, 58)

        SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                    win32con.MK_LBUTTON, click_guild)
        SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
        sleep(1)

        # storage
        click_guild = MAKELONG(482, 363)

        SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                    win32con.MK_LBUTTON, click_guild)
        SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
        sleep(1)

        # donate button clan
        click_guild = MAKELONG(350, 399)

        SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                    win32con.MK_LBUTTON, click_guild)
        SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
        sleep(1)

        coordinates = [[206, 154],  # copper
                       [219, 207],  # DS
                       [211, 249]]  # Energy

        # fazer loop a partir daqui iterando sobre as const
        for x in coordinates:
            # loop in energy, copper and darksteel
            click_guild = MAKELONG(x[0], x[1])

            SendMessage(
                hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_guild)
            SendMessage(
                hwnd, win32con.WM_LBUTTONUP, None, click_guild)
            sleep(0.8)
            # max (copper defalt)
            click_guild = MAKELONG(478, 306)

            SendMessage(
                hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_guild)
            SendMessage(
                hwnd, win32con.WM_LBUTTONUP, None, click_guild)
            sleep(0.8)

            # donate button
            click_guild = MAKELONG(483, 351)

            SendMessage(
                hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_guild)
            SendMessage(
                hwnd, win32con.WM_LBUTTONUP, None, click_guild)
            sleep(0.8)

            # confirm donate button
            click_guild = MAKELONG(397, 287)

            SendMessage(
                hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_guild)
            SendMessage(
                hwnd, win32con.WM_LBUTTONUP, None, click_guild)
            sleep(0.8)

        # close donate
        click_guild = MAKELONG(221, 359)

        SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                    win32con.MK_LBUTTON, click_guild)
        SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
        sleep(0.8)

        # exit
        click_guild = MAKELONG(676, 55)

        SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                    win32con.MK_LBUTTON, click_guild)
        SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
        # sleep de 24h
        sleep(86400)


def daily_buy(janela):
    hwnd = find_window_by_title('UgPhone', index=janela)
    for i in range(1):

        # open store
        click_guild = MAKELONG(514, 60)

        SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                    win32con.MK_LBUTTON, click_guild)
        SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
        sleep(1)

        # open intensify
        click_guild = MAKELONG(40, 311)

        SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                    win32con.MK_LBUTTON, click_guild)
        SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
        sleep(1)
        # loop in 4x buy
        for x in range(4):
            sleep(1)
            click_guild = MAKELONG(175, 402)

            SendMessage(
                hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_guild)
            SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
            sleep(1)

            click_guild = MAKELONG(423, 364)

            SendMessage(
                hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_guild)
            SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
            sleep(1)
            click_guild = MAKELONG(669, 57)

        SendMessage(hwnd, win32con.WM_LBUTTONDOWN,
                    win32con.MK_LBUTTON, click_guild)
        SendMessage(hwnd, win32con.WM_LBUTTONUP, None, click_guild)
        sleep(1)

# start threads in loop for


def start_daily_buy():
    # change range() if you need.
    for i in range(50):
        thread_name = f"MyThread-{i}"
        farm = Thread(
            target=daily_buy, args=(i,), name=thread_name)

        farm.start()


def start_donate():

    for i in range(50):
        thread_name = f"MyThread-{i}"
        farm = Thread(
            target=donate, args=(i,), name=thread_name)

        farm.start()
