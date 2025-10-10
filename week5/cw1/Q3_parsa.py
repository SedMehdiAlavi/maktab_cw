import time

def decorated_function(func) :
    def wrapper(*args,**kwargs) :
       try :
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        exec_time = end - start
        print("taken time: ", exec_time)

       except ValueError:
           print("ValueError")
           return result
       return wrapper
