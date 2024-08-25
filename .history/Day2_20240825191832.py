#Subscripting
print("hello"[0])
print("hello"[-2])
print("hello"[-1])
print("hello"[4])

#data Type

#Strings
print("hello"+"1234") #concatentaion

#Integers
print(1331)
print(1331+2344)

#Floats

print(123.45)
print(123.45+2344.44)

#large number use to read big elements easily by putting comma and dash.
print(123456_78901_23456_7890)

#boolean for dicision. [false is 0 value] and [true is 1 value]
a = 23
b = 45
print(a>b) #false
print(a<b) #true
print(True)
print(False)

#Data type checking

print(type(123)) #int
print(type(123.45))#float
print(type("hello"))#str
print(type(True))#boolean

#typecasting convert form one type to another datatype, with same literal datatype.
#int to float
print(int(123.45))#123
print(float(123))#123.0
print(int("2344")+int("5443"))
print(str(2344))#"2344"

#exercise
print("Number of element in  your name :" + str(len(input("enter your name:\n"))))


#Mathematical operator

print(32+43) #additon
print(3405-555) #subtraction
print(98*33) #multiple
print(23/3)# divison with decimal
print(12//6)
print(2**5)

#PEMDAS pirority order og mathematical operator to execute [order go from left to right]
#1. Parenthesis
#2. Exponentiation
#3. Multiplication and Division
#4. Addition and Subtraction

#exercise
print(3*3+3/3-3)

#exercise to get answer 3 in above question
print(3*(3+3)/3-3)#maam method
print(3/3+3-3/3)#my method