def abdullah():
    print("My name is Abdullah")
    #defining a return value
    return("Carzy")
#calling funct
abdullah()

# Return value using in program
m=abdullah()
print(m)

#Default value
def kheruwala(name="Abdullah"):
    if name is "basir":
        print("basir Kheruwala")
    if name is "masir":
        print("masir Kheruwala")
    if name is "Abdullah":
        print("abd Kheruwala")

kheruwala() #default case runs
kheruwala("basir")
kheruwala("masir")
kheruwala("vdud")