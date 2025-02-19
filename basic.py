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


# #Boolean data type
# a='madhu'
# print(a=='madhu')
# print(a=='madhavika')
# b=123
# print(b==123)


# #Typecasting
# print(int(True))
# print(float(False))
# print(complex(True))
# print(bool(True))
# print(str(True))


# #list
# list_1 = [1, 2, 3, 'madhu', False, [5, 6, 7]]
# print(len(list_1)) #len()
# print(list_1[3])   # +ve indexing
# print(list_1) #printing
# # print(list_1[6]) IndexError: list index out of range max index is len-1
# print(list_1[-6])  #-ve indexing
# print(list_1[1:6:3]) #slicing
# print(list_1[-1:-6:-2]) #slicing in reverse
# print(list_1[5][0]) # accessing the list inside a list
# list_1[2]='Hi'  #mutable
# print(list_1)
# list_1[4] = 'Bye'
# print(list_1)
# print(len(list_1[5])) #length of list inside list
# list_1[5][1] = 567
# print(list_1)



# #tuple
# tup_1 = (1,2,3,'Hi',('madhu', 5, 6)) 
# print(len(tup_1)) #len
# print(type(tup_1)) #type
# print(tup_1[2]) # +ve indexing
# print(tup_1[-4]) # -ve indexing
# print(tup_1[-5:-1]) #slicing
# print(tup_1[-1:-5:-1]) # slicing in reverse
# # tup_1[3]=123 #TypeError: 'tuple' object does not support item assignment which represents immutability
# print(tup_1[4][0]) # accessing tuple inside tuple



# #Range
# print(list(range(100,1,-1))) # printing range in reverse
# print(list(range(1,100))) # printing range

# m= [1, 2, 3]
# print(id(m[0]))
# print(id(m[1]))
# print(id(m[2]))


# s = 'madhu'
# print(id(s[0]))
# print(id(s[1]))
# print(id(s[2]))
# print(id(s[3]))
# print(id(s[4]))



# # Range
# m= [12, 24, 36]
# print(range(0,5))


# print(list(range(0,5))) #typecasting into list
# print(tuple(range(0,5))) # typecasting into tuple


# for i in range(0,5):  # printing in line by line
#     print(i)


# for i in m:   #printing using list variable
#     print(i)

# for i in range(len(m)): #printing without using list variablr
#     print(m[i])


# # sets
# set1 = {1,4,5,5,6,9,0,1,5,3,5}
# print(set1)  #unordered   #prints repeated value only once

# list1= [1,1,1,2,2,3,4,5,5]
# print(list1)
# print(set(list1))



# #NoneType

# num=None
# print(num)
# print(id(num))
# print(type(num))


# # input()
# num = input('Enter your fav num') 
# print(num) 
# numm = input('Enter another num') 
# print(num+numm) # output 515 due to default string data type


# num1 = int(input('Enter your fav num'))
# numm1 = input('Enter another num')
# print(num1+numm1) # output TypeError: unsupported operand type(s) for +: 'int' and 'str'


# num2 = int(input('Enter your fav num'))
# numm2 = int(input('Enter another num'))
# print(num2+numm2) # output 11




# #Conversions
# int1 = 10
# bool1 = True
# str1 = 'madhu'
# list1 = [1, 3.5, True, ['hi', 6]]
# tup1 = (1, 2)


# int1 = float(10)   # int to float
# print(int1)
# int1 = int(int1)   # float to int
# print(int1)


# print(int(bool1))   # bool to int
# print(bool(0))      # int to bool


# print(bool(str1))  #string to bool
# print(bool(''))
# print(str(bool1))   #bool to string


# # print(int(str1)) # Error string to int
# # print(int('25.5555'))  # string to int Error
# print(int('12'))   # string to int possible only when string is integer

# print(str(int1))    # int to string


# print(str(10.0))     # float to string

# print(float('25.555')) # string to float


# # print(int(3+5j)) #complex to int error
# print(complex(3))  # int to complex


# print(list(str1)) #string to list
# print(str(list1)) #list to string


# # print(list(12))   #int to list Error
# # print(tuple(12))   # int to tuple Error



# print(complex(2.134))   #float to complex
# # print(float(2+5j))   complex to float error


# print(bool(10.34567))  # float to bool
# print(float(True))       # bool to float



# # print(list(10.23456))   float to list error
# # print(float(list1))  list to float error


# # print(tuple(0.2345)) #float to tuple error
# # print(float(tup1)) #tuple to float error



# print(bool(3+4j)) #complex to bool
# print(complex(True)) # bool to complex


# print(str(2+4j)) #complex to string
# # print(complex('madhu'))  #string to complex error


# # print(list(3+4j)) #complex to list   error
# # print(complex(list1)) # list to complex  error



# # print(tuple(3+4j)) #complex to tuple error 
# # print(complex(tup1)) # tuple to complex error 


# # print(list(bool1))   # bool to list error
# print(bool(list1))      # list to bool


# # print(tuple(bool1))   # bool to tuple error 
# print(bool(tup1))      # tuple to bool



# print(tuple('madhu'))   # string to tuple error 
# print(str(tup1))      # tuple to string


# # print(int(1, 2))  # tuple to int error 



# print(tuple(list1))   # list to tuple  
# print(list(tup1))      # tuple to list


# print(bin(23))
# print(oct(76))
# print(hex(65))
# print(0x41)  # gives decimal number


# num1 = 0o12
# print(num1)

# print((50-28)**4*3/2//40)

# print(2<3)
# print(5>6)
# print(4==7)
# print(81<=123)

# num2 = 12
# num2 += 2
# print(num2)


# num2 -= 2
# print(num2) 

# num2 *= 2
# print(num2)

# num2 /= 2
# print(num2)

# num2 //= 2
# print(num2) 

# num2 **= 2
# print(num2)

# num2 %= 2
# print(num2)


# num3= 5
# num3 -= -1
# print(num3)
# print(bool(None))

# # logical and
# print( True and True)
# print( False and True)
# print( True and False)
# print( False and False)




# print(2 and 3)
# print(3 and 2)
# print(0 and "")
# print("" and 0)
# print(None and 'hi')



# # logical or
# print( True or True)
# print( False or True)
# print( True or False)
# print( False or False)



# print(2 or 3)
# print(3 or 2)
# print(0 or "")
# print("" or 0)
# print(0 or 'madhu')
# print(None or 0)


# # logical not
# print( not True)
# print( not False)


# print(not 2)
# print(not 0)
# print(not None)
# print(not -6+2j)


# # Bitwise operators
# # bitwise and &
# print(3 & 4)
# print(12 & True)
# print(13 & True)



# print(True & False)
# print(bin(True))
# print(bin(False))

# # bitwise or |
# print(2 | 3)
# print(True | False )
# print(12 | 13)



# # bitwise xor ^
# print(2 ^ 3)
# print(12 ^ 14)
# print(True ^ True)
# print(True ^ False)



# # bitwise not ~
# print(~ 3)
# print(~ 15)
# print('asdfghjkl')
# print(~True) 


# # leftshift  # Rightshift
# print(5<<2)
# print(200<<2)
# print(20>>2)
# print(20<<3)



# n=31
# if (n==1):
#     print("Pushpa The Rise")
# elif (n==2):
#     print("Pushpa The Rule")
# elif (n==3):
#     print('Pushpa The Rampage')
# else:
#     print('Invalid')



# 
# if (num>0):
#     if(num==1):
#         print('one')
#     else:
#         print('Positive')
# else:
#     if (num==0):
#         print('Zero')
#     else:   
#         print('Negative')



# num = 0
# if(num>0):
#     if num==1:
#         print('one')
#     else:
#         print('+ve')
# elif num==0:
#     print('Zero')
# elif num==-1:
#     print('-1')
# elif num==-2:
#     print('-2')
# else:
#     print('-ve')

# cur=50
# if cur<=100:
#     if cur<0:
#         print('Invalid')
#     else:
#         if(cur<=50):
#             print(0)
#         else:
#             print(cur*50)
# else:
#     if cur<=200:
#         print(cur*100)
#     else:
#         if(cur<=300):
#             print(cur*150)
#         else:
#             print('Invalid')



# for loop using range
# for i in range(0,5,2):  #printing even using step
    # print(i)


# for i in range(0,5):   #printing even using if 
#     if (i%2==0):
#         print(i, 'even')
#     else:
#         print(i, 'odd')



# for i in range(0, 21):   #print mul of 3 using if
#     if i%3==0:
#         print(i)


# for i in range(0,21,3):    #print mul of 3 using step
#     print(i)


# for i in range(1, 21,2):  #print odd using range
#     print(i)


# nested loops
# 

# for i in range(1,11):
#     if i!=5 and i!=7 :
#         for j in range(1,31):
#             print(i,j)








    
        


# i=0
# while (i<6):
#     print(i)
#     i+=1



# num1=1
# while num1<5:
#     print('hi')
#     num1+=1


# num1=5
# while num1<26:
#     if(num1%2==0):
#         print(num1, 'even')
#     else:
#         print(num1, 'odd')
#     num1+=1




# cls= 1
# while cls<11 :
#     if cls!=5 and cls!=7:
#         for i in range(1,31):
#             print(cls,i)
#     cls+=1



cl= 1
while cl<11 :
    if cl!=5 and cl!=7:
        roll=1
        while roll<31:
            print(cl,roll)
            roll+=1

    cl+=1
