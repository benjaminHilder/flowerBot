import time
from threading import Timer

def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))

#basic timer
def run_once():
    display('Run once: ')
    t = Timer(5,display,['Timeout:'])
    t.start() #run is called

run_once()
#notice this ran immediately!
#but it also only runs once
print('waiting...')

#Interval timer
#wrap it into a class
#make it run until we stop it
#notice we can have multiple timers at once!

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args,**self.kwargs)
        print('Done')

#Really we are making a thread and controlling it
timer = RepeatTimer(1,display,['Repeating'])
timer.start() #going to call run
timer = RepeatTimer(2,display,['Repeating2'])
timer.start() #going to call run
print('threading started')
time.sleep(10) #suspends execution for the given number of seconds
print('threading finishing')

timer.cancel()