# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date

def calcFee(returned,due):
    fee = 0
    
    if(returned<=due):
        fee = 0
    elif(returned>due and returned.month==due.month):
        fee = ((returned - due).days)*15
    elif(returned.month>due.month and returned.year==due.year):
        fee = (returned.month - due.month)*500
    elif(returned>due and returned.year>due.year):
        fee = 10000
    
    return fee

r = input().split()
d = input().split()

r = date(int(r[2]), int(r[1]), int(r[0]))
d = date(int(d[2]), int(d[1]), int(d[0]))

print(calcFee(r,d))