'''4. Get the key corresponding to the minimum value from the following dictionary using appropriate python logic.
sample={
‘physics’, 88 ,  ‘maths’, 75,  ’chemistry’ , 72,’Basic electrical’ , 89 
}
'''
print('enter the number of key value pairs you want to enter')
#taking input of the number of key value pairs
n=int(input())
print('enter the key value pairs as follows')
print('key<space>value')
#declaring an empty deictionary
dic={}
#running a loop n times for n inputs
for i in range(n):
	#taking input of key value pairs seperated by space
	a,b=input().split()
	#adddding it to the dictionary
	dic[a]=int(b)
#converting the dictionary of a list of the key value pairs
k=list(dic.items())
#sorting the dictionary based on the values
k.sort(key=lambda x: x[1])
#printing the key representing the lowest value
print("the lowest key is")
print(k[0][0])