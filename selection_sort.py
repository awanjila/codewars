"""
selection sort problem..
"""
def selection(list_nums):
	n=len(list_nums)

	for i in range(n-1):
		print (list_nums)
		minimum=i
		for j in range(i+1, n):
			if list_nums[j]<list_nums[minimum]:
				minimum=j
		list_nums[minimum], list_nums[i] = list_nums[i], list_nums[minimum]
		print (list_nums)
	return list_nums



print(selection([9,3,1,2,7,5,4,6,7,8,10,33,0,12]))