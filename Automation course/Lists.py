#!/usr/bin/env python3
#for loop
def exp(x, y):
    val = 1
    for i in range(y):
        print("i is: {}".format(i))
        val = val*x
    print(val)
    return val
#exp(2,3)

#while loop
def exp2(x,y):
    val = 1
    while y:
        print("y is: {}".format(y))
        val *= x
        y-=1
    print(val)
    return val
#exp2(2,3)

#lists - can be modified
a=[1,2,3]
a.append('string')
#print(len(a))

#tuples - list that cannot be modified
t=('string',1,2,3)
t+=('another string',4)
#print(len(t))
#for item in t:
   # print(item)

#Dictionaries - value associated with a key - value:key
d={'key1':'value1', 'key2':'value2', 'key3':'value3'}
#to edit value
d['key1'] = 'edited value1'
#to add a key
d['key4'] = 'value4'
print(d)