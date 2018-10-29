'''
# parent class: Parent_Gulia_family
# child class : Parent_Gulia_family
# So the child class is inheriting the properties of the parent class( print_last _name) in the child class

class Parent_Gulia_Family:
    def print_last_name(self):
        print("Gulia")

class Child_Gulia_Family(Parent_Gulia_Family):
    def print_first_name(self):
        print("Shubham")

sons= Child_Gulia_Family()
sons.print_first_name()
sons.print_last_name()
'''
class Parent_Gulia_Family:
    def print_last_name(self):
        print("Gulia")

class Child_Gulia_Family(Parent_Gulia_Family):
    def print_first_name(self):
        print("Shubham")
# OVERRIDING the parent class
    def print_last_name(self):
        print("Singh")

sons= Child_Gulia_Family()
sons.print_first_name()
sons.print_last_name()


