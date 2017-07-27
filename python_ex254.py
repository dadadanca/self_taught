# I changed the variable in this example from
#  numbers in older versions of the book to nums 
# so the example fits on smaller devices. If you have an older
# version of the book, you can email me at cory@theselftaughtprogrammer.io 
# and I will send you the newest version. Thank you so much for purchasing my book!

class Data:
    def __init__(self):
        self._nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self._nums[index] = n

    def __repr__(self):
        return "%s"%self._nums

data_one = Data()
data_one._nums[0] = 100
print(data_one._nums)

data_two = Data()
data_three = data_two

data_two.change_data(0, 100)
print(data_two)
print(data_three)
