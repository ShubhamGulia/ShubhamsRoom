from operator import itemgetter

users= [
    {'fname': 'Ducky', 'lname': 'Hayes'},
    {'fname': 'Elephant', 'lname': 'Abd'},
    {'fname': 'Ducky', 'lname': 'Abd'}
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print(" ----------------------------------")

for x in sorted(users, key=itemgetter('fname','lname')):
    print(x)
