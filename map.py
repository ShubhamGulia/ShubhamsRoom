income=[10,20,50]

def money_double(dollars):
     return dollars*2

# iterate 1 item at a time
newmoney= list(map(money_double,income))
#newmoney= money_double(income)

print(newmoney)