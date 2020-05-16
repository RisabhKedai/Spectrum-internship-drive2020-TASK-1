'''6. Program to create simple calculator in Python which on input of 1,2,3,4 should add ,
 subtract , multiply and divide respectively.'''
print("enter the two numbers to operate upon")
 #taking integers to operate
a,b=map(int,input().split())
print("choose an operation from below:-")
print("1-Add\n"+"2-Subtract\n"+"3-Multiply\n"+"4-Divide\n")
 #selecting the operator
opt=int(input())
#printing reqired results for the apt  operator
if opt==1:
	print(a+b)
elif opt==2:
	print(abs(a-b))
elif opt==3:
	print(a*b)
elif opt==4:
	print(a/b)
