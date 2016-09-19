def remove_adjascent_duplicates(nums):
	prev=''
	new_nums=[]
	for i in nums:
		if prev!=num:
			new_nums.append(num)
			prev=num
		return new_nums
