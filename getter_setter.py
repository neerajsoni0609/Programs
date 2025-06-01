class Demo:
    def __init__(self) -> None:
        self.__value = 500

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        self.__value = new_value

demo = Demo()
# print(demo.__value) # This will throw AttributeError
print(demo.value) # Prints 500

demo.value = 600
print(demo.value)