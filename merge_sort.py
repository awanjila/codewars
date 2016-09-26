
"""
Merge sort with python
"""

def mergesort(nums):
	n=len(nums)
	if n==1:
		return nums

	left=nums[0:n//2]
	right=nums[n//2:n]
	left=mergesort(left)
	right=mergesort(right)
	return merge(left, right)

def merge(left, right):
	combined=[]
	while len(left)>0 and len(right)>0:
		if left[0]>right[0]:
			combined.append(right[0])
			right.remove(right[0])
		else:
			combined.append(left[0])
			left.remove(left[0])
	while len(left)>0:
		combined.append(left[0])
		left.remove(left[0])
	while len(right)>0:
		combined.append(right[0])
		
		right.remove(right[0])

	return combined

print(mergesort([9, 5, 6, 1, 8, 2, 3]))
