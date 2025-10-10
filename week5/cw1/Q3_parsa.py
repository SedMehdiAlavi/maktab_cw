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
    temp.append(random.randint(-2, 3) + start_temp)
    print(temp)
    
    print(days)

    if not isinstance(days , int) and days < 0:
       print("ok input")
     
   

imulate_weather(days)