def calculator(*args):
    total=0;
    for a in args:
        total += a
    print(total)

# passing different numbers of arguments
calculator(3,43,5453,354234)
calculator(1,2,3,4,5,6,7,8,9)
calculator(1,2,3,4,5,6,7,8,9,10)