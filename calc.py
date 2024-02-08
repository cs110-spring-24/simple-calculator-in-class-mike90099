#print("Pick your first number.")
num1 = input("Pick your first number")
num1 = int(num1)
#print("Pick an operator.")
opr = input("Pick an operator")
#if opr != "+" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#elif opr != "-" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#elif opr != "*" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#Welif opr != "^" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#elif opr != "x" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#elif opr != "/" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#elif opr != "//" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#elif opr != "%" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#elif opr != "**" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#if opr != "+" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#
#opr = int(opr)
#else:
#else:
num2 = input("Pick your second number")
num2 = int(num2)
#print("Pick your second number")
#num2 = input()
#if opr != "+" "-" "*" :
#	print("Sorry. These operators are invalid. Instead, please use the following operators:")
#else:
#Addition

if opr == "+" :
	print(num1+num2)

#Subtraction

if opr == "-" :
	print(num1-num2)

#Multiplication with * or x as acceptable operators

if opr == "*" :
	print(num1*num2)
elif opr == "x" :
	print(num1*num2)

# Division

if opr == "/" :
	print(num1/num2)

#Power with ** or ^ as acceptable operators

if opr == "^" :
	print(num1**num2)
elif opr == "**" :
	print(num1**num2)	

# Integer Division
if opr == "//" :
	print(num1//num2)

#Modulo
if opr == "%" :
	print(num1%num2)
