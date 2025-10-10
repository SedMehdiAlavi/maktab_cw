import time
import random

def decorated_function(func) :
    def wrapper(*args,**kwargs) :
       try :
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        exec_time = end - start
        print("taken time: ", exec_time)
        return result

       except ValueError:
           print("ValueError")

    return wrapper
day = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
temp = []
@decorated_function
def imulate_weather(days, start_temp = 25):
    days = random.choice(days)
    temp = random.randint(-2, 3)

    print(days)

imulate_weather(day)