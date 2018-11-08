N = int(input())
for n in range(0, N):
    str = input()
    for y in range(0, len(str)):
        if (y % 2 == 0):
            print(str[y], end="")
    print(" ", end="")
    for x in range(0, len(str)):
        if (x % 2 == 1):
            print(str[x], end="")
    print()








