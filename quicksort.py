def quicksort(nums, start, end):
	if start<end:
		piv_pos=partition(nums, start, end)
		quicksort(nums,start,piv_pos-1)
		quicksort(nums, piv_pos+1,end)
	return nums
def partition(nums, start,end):
	piv=nums[start]
	i=start+1
	for j in range(start+1, end):
		if nums[j]<piv:
			nums[i], nums[j]=nums[j], nums[i]
			i+=1
	nums[start], nums[i-1]=nums[i-1], nums[start]

print(quicksort([9,2,3,4,5,1],0,6))