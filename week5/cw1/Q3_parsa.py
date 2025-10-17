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

temp = []

@decorated_function
def imulate_weather(days, start_temp = 25):
    if isinstance(days , int) and days > 0:
       print("correct input")

    else:
        print("invalid input")

    for i in range(days):
        temp.append(random.randint(-2, 3) + start_temp)
        avg = sum(temp) // len(temp)

    print(f"temps: {temp}, avg: {avg}, min: {min(temp)}, max: {max(temp)}")

imulate_weather(3)