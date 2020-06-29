import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Warehouse :
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self) :
         Warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
