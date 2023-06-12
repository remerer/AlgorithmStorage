import re

number = re.compile('\d+')
testlist = ["foo100bar029.txt", "Foo010.txt", "Foo123"] 

# print(test.split(number.findall(test)[0]))
for i in range(len(testlist)):
    testlist[i] = [testlist[i].split(number.findall(testlist[i])[0])[0], number.findall(testlist[i])[0], testlist[i].split(number.findall(testlist[i])[0])[1]]
testlist.sort(key=lambda x:x[1].lstrip('0'))
testlist.sort(key=lambda x:x[0].upper())

print(testlist)