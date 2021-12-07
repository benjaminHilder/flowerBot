import threading
import time
import square
import main

class myThread(threading.Thread):
    def __init__(self, square):
        threading.Thread.__init__(self)
     
        self.square = square

    
    def run(self):
        print("Starting: "  + "\n")

        countDown(self.square ,60,self.square.harvestTime)
        print("Exiting: "  + "\n")

def countDown(square, delay, count):
    while count:
        time.sleep(delay)
        #print("%s: %s %s" % ( time.ctime(time.time()), count) + "\n")
        square.harvestClock -= 1
        count -= 1
        print("harvest clock ", square.harvestClock)
    #
    print("Thread ", " done" )
        

#thread1 = myThread(1, "Thread1", 10)
#thread2 = myThread(2, "Thread2", 5)
#
#thread1.start()
#thread2.start()
#thread1.join()
#thread2.join()
