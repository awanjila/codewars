"""""""""""""""""""""""
bubble sort algorathim

"""""
def bubblesort(nums):
	n=len(nums)
	for i in range(n-1):
		#second loop ignores the numbers which have already been sorted
		for j in range(1,n-i):
			#compare two adjacent numbes
			if nums[j]<nums[j-1]:
			 #swap the two numbers
				nums[j], nums[j-1]=nums[j-1], nums[j] 
		return nums

print (bubblesort([9, 5, 6, 1, 8, 2, 3]))