def quick_sort_prob(arr):
	n=len(arr)
	arr=(nums for nums in input().split(" "))
	left=[]
	right=[]	
	equal=[]
	if n >1:
		pivot=arr[0]
		for x in arr:
			if x<pivot:
				left.append(x)
			if x==pivot:
				equal.append(x)
			if x>pivot:
				right.append(x)
		return quick_sort_prob(left)+equal+quick_sort_prob(right)
	else:
		return arr





