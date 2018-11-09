#Initialize the dictionary
phonebook= dict()
n= int(input())
for i in range(n):
    # read both input and they are splited by space as mentioned
    name,number = input().split()
    #assigning th evalue to the name
    phonebook[name] = number

for j in range(n):
    name=input()
    if name in phonebook:
        #formating as required
        print('{}={}'.format(name,phonebook[name]))
    else:
        print("Not found")
