print("@SHubham Gulia")

class Boys:
    gender = "MALE"
    def __init__(self,x):
        self.name = x

Shubham = Boys("Shu")
Aekansh = Boys("Aek")
print(Shubham.name)
print(Shubham.gender + ("\n"))

print(Aekansh.name)
print(Aekansh.gender)

'''
So :  gender variable defined is CLASS variable : thats is same for all objects
      name is instance variable : thats is unique for all objects  
'''