'''Given input String of combination of the lower and upper case ,
arrange characters in such a way that all lowercase letters should come first.'''
#taking string input and converting to list
s=list(input("enter your string:-\n"))
#traversing through each character
j=0
k=''
while j<len(s):
	#if it is a upper case character
	if s[j]>='A' and s[j]<='Z' and s[j]!=" ":
		k+=s.pop(j)
		#joining it to the end of another string
		j-=1
	j+=1
#printing results
print("".join(s)+k)
