from operator import attrgetter

class User:
    def __init__(self,x,y):
        self.name=x
        self.userid=y
    def __repr__(self):
        return self.name +" : " +str(self.userid)
users = [
    User('Bucky', 43),
    User('Sally', 5),
    User('Crazy', 61),
    User('mogra', 77),
    User('Japyd', 2)
]

for user in users:
    print(user)
print("-------------------")
for user in sorted(users,key=attrgetter('name')):
    print(user)

