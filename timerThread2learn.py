from time import *
import threading

def countdown():
    global my_timer1
    global my_timer2
    my_timer1 = 5
    my_timer2 = 10

    for x in range(999):
        my_timer1 = my_timer1 - 1
        my_timer2 = my_timer2 - 1

        sleep(1)

    print("out of time")


countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

while my_timer1 > 0:
    print("Hello world timer ")
    sleep(1)

while my_timer2 > 0:
    print("Hello world timer 2")
    sleep(1)

print("Time up")