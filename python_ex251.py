# IMPORTANT. I changed many of the variable names in this example
# so the example fits on smaller devices. Old versions of the book have longer
# variable names. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!


class Rectangle():
    def __init__(self, w, l):
        self._width = w
        self._len = l

    def area(self):
        return self._width * self._len

    def change_size(self, w, l):
        self._width = w
        self._len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())
