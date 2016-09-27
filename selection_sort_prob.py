"""
Consider an Array a of size N
Iterate from 1 to N
In ith
iteration select the ith minimum and swap it with a[i]

You are given an array a
, size of the array N and an integer x. Follow the above algorithm and print the state of the array after x

iterations have been performed.

Input Format

The first line contains two integer N
and x denoting the size of the array and the steps of the above algorithm to be performed respectively. The next line contains N

space separated integers denoting the elements of the array.

Output Format

Print N
space separated integers denoting the state of the array after x steps

"""

def selection(arr,n):
	y = len(arr)
	for i in range(n):
		minimum = i
		for j in range(i+1, y):
			if arr[j] < arr[minimum]:
				minimum = j
		arr[minimum], arr[i] = arr[i], arr[minimum]
	return arr
    	
values = [int(num) for num in input().split(" ")]
arr = [int(num) for num in input().split(" ")]
print (" ".join(map(str, selection(arr, values[1]))))