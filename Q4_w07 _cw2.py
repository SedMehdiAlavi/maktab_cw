class CustomDict :
#     dict1 ={}
    def __new__ (cls, keys , value ) :
        if not keys :
            raise ValueError("key not found")
        obj = object.__new__ (cls)
        return obj
        # if key == None:

    def __init__(self : dict , key = None, value = None):
        #
        self.key = key
        self.value = value


    def __setitem__(self, value):
        # self.dict1[key] = value
        if isinstance(value, int) :
            # self.value = value
            self.value = value*2
        else :
            self.value = value


custom = CustomDict (2 , 4)
# print(custom.key)
# custom.value = 6
# print(custom.value)

custom.__setitem__(8)
print(custom.value)
