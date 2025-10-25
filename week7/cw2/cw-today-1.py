class Vector3D:
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, other):
        return Vector3D(self.__x + other.x , self.__y + other.y , self.__z + other.z)

    def __sub__(self, other):
        return Vector3D(self.__x - other.x , self.__y - other.y, self.__z - other.z)

    def __iadd__(self, other):
        self.__x += other.x
        self.__y += other.y
        self.__z += other.z
        return self

    def __radd__(self, value):
        self.__x += value
        self.__y += value
        self.__z += value
        return self


    def __eq__(self , other):
        return self.__x == other.x and self.__y == other.y and self.__z == other.z


    def __len__(self):
        return 3

    def __str__(self):
        return f"{self.__x} , {self.__y} , {self.__z}"

    def __repr__(self):
        return f"x={self.__x} :int, y={self.__y} :int, z={self.__z} :int"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self , value):
        self.__x = value


    @property
    def y(self):
        return self.__y


    @x.setter
    def y(self, value):
        self.__y = value

    @property
    def z(self):
        return self.__z

    @x.setter
    def z(self, value):
        self.__z = value

v1 = Vector3D(1,2,3)
v2 = Vector3D(4,5,6)

print(v1)
print(v2)

print(v1 + v2)
print(v2 - v1)

v1 += v2
print(v1)

print(v1.x)
v1.x = 100
print(v1.x)
