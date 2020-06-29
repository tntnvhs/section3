import sys
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self) :
        print("------")
        print("Name:" + self.name)
        print("Phone:" + self.phone)
        print("------")
    def __del__(self):
        print("delete!")
        
user1 = UserInfo("kin", "010-4109-4303")
user2 = UserInfo("park", "010-3109-4303")

print(id(user1))
print(id(user2))

#user1.set_info("kin", "010-4109-4303")
#user2.set_info("park", "010-3109-4303")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)
