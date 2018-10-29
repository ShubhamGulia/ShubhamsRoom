
'''
# init is function which is self called everytime a other function is called of the same class
# it is used in making games and similar stuffs
class Gulia:
    def __init__(self):
        print("Gulia's Family members")
    def member(self):
        print("Narender\n"+"Rajbala\n"+"Aekansh\n"+"Shubham\n")

swift = Gulia()
swift.member()
'''

class Gulia:
    def __init__(self,x):
        self.power=x
    def member(self):
        print("power is " + str(self.power))

# So this how we can initialize the power in init and two object can have different starting power
Narender = Gulia(78)
Rajbala = Gulia(15)
Narender.member()
Rajbala.member()
