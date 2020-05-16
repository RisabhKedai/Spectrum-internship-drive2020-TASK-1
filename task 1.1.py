'''1.Create an inner function to calculate the addition in the following way
•	Create an outer function that will accept two parameters ‘a’ and ‘b’ 
•	Create an inner function inside an outer function that will calculate the addition of ‘a’ and ‘b’ 
•	At last, an outer function will add 5 into addition and return it.
'''

def main_outer(a,b):
	#this the main outer function which will add and return the output with 5 added
	def first_inner(a,b):
		#this is the inner function declared as per the first line in the task
		def second_outer(a,b):
			#this is the outer function to be declared inside the inner function
			def second_inner(a,b): return a+b
			#this is the inner most function which returns the addition of a and b
			return second_inner(a,b)#getting the addition answer
		return second_outer(a,b)#which returns the answer from the inner addition
	return first_inner(a,b)+5#finally returning the addition+5 as the final answer

#printiong results
print("the answer is:-\n"+str(main_outer(int(input("enter a:-\n")),int(input("enter b:-\n")))))
