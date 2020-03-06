i=0
dix = {'counter':['c','t']}
while 't' in dix['counter']:
    i+=1
    if i==10:
        dix['counter'].remove('t')
print(i)