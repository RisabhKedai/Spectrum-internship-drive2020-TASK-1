'''5.  Given two Python sets, update first set with items that exist only in the first set and not in the second set .
S1={1,2,3,4,5,6,7,8,9}
S2={1,3,4,6,8,11,22,34,51,67}
'''

print("enter the elements of set 1 seperated by space")
set1=set(map(int,input().split()))#taking set 1 input
print("enter the elements of set 2 seperated by space")
set2=set(map(int,input().split()))#taking set 2 input
set1=set1.difference(set2)
print(set1)#printing the result