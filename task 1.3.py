'''3. Given a Python list, remove all the even number from the list 
and save those even number in another list and print both the lists.
For a given input list:  List1 = [1,2,3,4,5,6,7]
Output : List1=[1,3,5,7]
	List2 = [2,4,6]
'''
#asking for the input list
print("enter the elements of your list seperated by space")
#storing the input list in l
l=list(map(int,input().split()))
el=[] #even list
ol=[] #odd list
#traversing through each element of the list
for i in l:
	#checking if the element is odd or even
	if i%2==0:
		#if even add it to even list
		el.append(i)
	else:
		#if odd add it to odd list
		ol.append(i)
print("the odd terms are:-")
#printing the odd list
print(ol)
print("the even terms are:-")
#printing the even list
print(el)