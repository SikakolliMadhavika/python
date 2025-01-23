# Arithmatic operations
# print(123 + 456)
# print(123 - 456)
# print(123 * 456)
# print(123 / 456)
# print(123 // 456)
# print(123 % 456)


#using variables
# a=123
# b=456
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(4**4)
# print(a%b)


#strings
# a='Madhavika'


# length of str
# print(len(a))


# type of str
# print(type(a))


#indexing
# print(a[7])
# print(a[0])
# print(a[3:7])


#slicing with +ve and -ve indexing
# m='premiddam dude poyedemundi maha ithe tirigi premistaru'
# print(m[0:5])
# print(m[5:0:-1])
# print(len(m))
# print(m[-1:-54:-1])
# print(m[ : : -1])
# print(id(m))

#represents same memory alloocation
# p='premiddam dude poyedemundi maha ithe tirigi premistaru'
# a='premiddam dude poyedemundi maha ithe tirigi premistaru'
# print(id(p))
# print(id(a))


# p[5] = 's'   immutable


#complex
# b1= 3 + 5j
# b2 = 5 + 3j
# print(b1+b2)
# print(b1-b2)
# print(b1*b2)
# print(b1/b2) 
# print(b1**b2)
# print(b1%b2) TypeError: unsupported operand type(s) for %: 'complex' and 'complex'
# print(b1//b2) TypeError: unsupported operand type(s) for //: 'complex' and 'complex'


#Boolean data type
a='madhu'
print(a=='madhu')
print(a=='madhavika')
b=123
print(b==123)


#Typecasting
print(int(True))
print(float(False))
print(complex(True))
print(bool(True))
print(str(True))


#list
list_1 = [1, 2, 3, 'madhu', False, [5, 6, 7]]
print(len(list_1)) #len()
print(list_1[3])   # +ve indexing
print(list_1) #printing
# print(list_1[6]) IndexError: list index out of range max index is len-1
print(list_1[-6])  #-ve indexing
print(list_1[1:6:3]) #slicing
print(list_1[-1:-6:-2]) #slicing in reverse
print(list_1[5][0]) # accessing the list inside a list
list_1[2]='Hi'  #mutable
print(list_1)
list_1[4] = 'Bye'
print(list_1)
print(len(list_1[5])) #length of list inside list
list_1[5][1] = 567
print(list_1)



#tuple
tup_1 = (1,2,3,'Hi',('madhu', 5, 6)) 
print(len(tup_1)) #len
print(type(tup_1)) #type
print(tup_1[2]) # +ve indexing
print(tup_1[-4]) # -ve indexing
print(tup_1[-5:-1]) #slicing
print(tup_1[-1:-5:-1]) # slicing in reverse
# tup_1[3]=123 #TypeError: 'tuple' object does not support item assignment which represents immutability
print(tup_1[4][0]) # accessing tuple inside tuple



#Range
print(list(range(100,1,-1))) # printing range in reverse
print(list(range(1,100))) # printing range











