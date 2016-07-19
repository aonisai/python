# -*- coding: utf-8 -*-

#test_list_1 = ['python','-','izm','.','com']
test_list_1 = ['1','2','3','2','1']
test_list_2 = []
print test_list_2

print '-------------------------------------'

print "test1"
for i in test_list_1:
   print i

print '-------------------------------------'

test_list_2.append('python')
test_list_2.append('-')
test_list_2.append('izm')
test_list_2.append(',')
test_list_2.append('com')

print "test2",test_list_2

#test_list_1.insert(0,'http://www.')
#test_list_1.remove('2')
#print test_list_1.pop(1)
#print test_list_1.index('2')
print test_list_1.count('2')
print '-------------------------------------'

for i in range(test_list_1.count('2')):
    test_list_1.remove('2')

print "test1",test_list_1

#print test_list_1.pop()
#print "test1",test_list_1