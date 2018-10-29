class Narender:
    def Father(self):
        print("Narender: I am the Father\n")

class Rajbala:
    def Mother(self):
        print("Rajbala: I am the Mother\n")
'''
class Aekansh(Narender,Rajbala):
# if something is mandatory required : as if in the class we are required to pass some arguments so we can skip it by using (pass)
    pass
'''
class Aekansh(Narender,Rajbala):
# if something is mandatory required : as if in the class we are required to pass some arguments so we can skip it by using (pass)
    print("My name is Aekansh \n")

aeku=Aekansh()
aeku.Father()
aeku.Mother()
