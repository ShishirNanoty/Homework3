#Homework3
def comp(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    bln = False
    if a == b or a == c:
        bln = True
    return bln
condit = comp(2,'2',3)
print('Condition is', condit, 'for given input')
