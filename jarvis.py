#!/usr/bin/env python
import threading
import time
import schedule

# so this little python bot that could, will create an event list 
# It will load in a calendar based on a JSON file - from this.
# 
# For recurring events it wil create an appropriate scheduled job.
#
# For one off events it will create an scheduled job based on the current time.. for example : 

#
#from datetime import datetime
#now = datetime.now()
# I'm just creating a datetime in 3 hours... (you'd use output from above)
#from datetime import timedelta
#run_at = now + timedelta(hours=3)
#delay = (run_at - now).total_seconds()
#
# Now we know the delay to create... so:
# schedule.every(delay).minutes.do(job)
#
#Or we could use APScheduler https://pypi.python.org/pypi/APScheduler/3.2.0



class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Doing something imporant in the background')

            time.sleep(self.interval)

example = ThreadingExample()



time.sleep(10)
print('Checkpoint')
time.sleep(12)

print('Bye')