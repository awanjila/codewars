"""
You are given an array of integers, , and a positive integer, . Find and print the number of pairs where and + is evenly divisible by .

Input Format

The first line contains space-separated integers, and , respectively.
The second line contains space-separated integers describing the respective values of .

Constraints

Output Format

Print the number of pairs where and + is evenly divisible by .
"""
def divisible_sums(values, arr):
	n=len(arr)
	res=0
	for i in range (n):
		for j in range(i+1,n):
		 	if i<j and (arr[i]+arr[j])%values[1]==0:
		 		res+=1
	return res

values=list(map(int, input().strip().split(" ")))
arr=list(map(int, input().strip().split(" ")))

print (divisible_sums(values, arr))