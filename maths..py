# task1 submission by  2/8/24

b=90
a=39
print(a,b) #prints value of  integer type variable a & b 
print(a-b,a+b, a%b ,a/b, a**2) #sub,add,modulo,divide,exponential

s="main"
st="flow"
print(s) #prints value of string datatype

print(st+s) # adding two strings

#---------------list---------------------
print('----------------------------------------------------------')
l=['a','e','o','i','u'] #list of vowels
l1=[3,9,8,5,2,1]
print('vowels :',l)
print('numbers :',l1)

lis=l+l1
print('joined list : ',lis) #joins two lists

l1.remove(8)
print("after removal : ",l1) #deletes particular element

l.pop() 
print('pop:',l) #deletes last element

l1.append(0)
print('after append',l1)#adds to the list
print('----------------------------------------------------------')
#----------------tuple-----------------------------------
t=(3,7,8,9,0)
print('original tuple :',t)
#inserting element to tuple
t=t+(5,)       
print('updated',t)

#--------------dictionary----------

d={1:'apple',2:'mango',3:'pineapple',4:'banana'}

print('original dictionary :',d)

print('third element :',d[3])

d[5]='orange'
print('updated dictionary :',d)

d.pop(4)
print("new",d)

#-------------conditional statements--------------------
a=34
b=12
if(a<b):
    print('a is smaller')
else:
    print('b is smaller')