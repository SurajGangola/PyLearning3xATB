import time
def note_time_decorator(f1):
     def wapr():
         Start_time=time.time()
         f1()
         end_time=time.time()
         print("time taken  - "+str(end_time-Start_time))
     return wapr()

@note_time_decorator
def logs_fun():
    time.sleep(5)
    print("print the log of the time taken")


@note_time_decorator
def reporting_log():
    time.sleep(2)
    print("print the log of the time taken")

