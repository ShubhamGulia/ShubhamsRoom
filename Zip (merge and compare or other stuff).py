a= [10,20,30,50]
b=[5,50,20,10]
c = zip( a, b)
for a,b in c:
    print(a,b)
    if a > b:
        print(a)
    else:
        print(b)

