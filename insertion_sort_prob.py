"""
Insert element into sorted list
Given a sorted list with an unsorted number in the rightmost cell, can you write some simple code to insert into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of to a variable and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace it with . total_size=int(input())

"""

numbers=[int(num) for num in input().split(" ")]
key=numbers[-1]
current= len(numbers)-2
while current>=0 and numbers[current]>key:
	numbers[current+1]=numbers[current]
	print(" ".join(map(str,numbers)))
	current-=1
numbers[current+1]=key
print(" ".join(map(str,numbers)))
