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
print(12//6)#exponent give answer without decimal
print(2**5)#use for  number multiple by itself how many time.

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

#Project2 Tip Calculator

print("Welcome to tip calculator!")
bill = float(input("Enter your bill?\n"))
tip = int(input("Enter your tip you want give 10 ,12,15?\n")) 
people = int(input("Enter your no. of friends you want to spilt bill?"))

tip_percentage = tip/100
tip_amount = bill * tip_percentage
total_bill = bill + tip_amount
split_bill = total_bill/people
