"""
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, he decides to cancel class if fewer than students are present when class starts.

Given the arrival time of each student, determine if the class is canceled.

Input Format

The first line of input contains , the number of test cases.

Each test case consists of two lines. The first line has two space-separated integers, (students in the class) and (the cancelation threshold). The second line contains space-separated integers () describing the arrival times for each student.

Note: Non-positive arrival times () indicate the student arrived early or on time; positive arrival times () indicate the student arrived minutes late.

"""

tests=int(input())
for testcase in range(tests):
	given =list(map(int, tests.strip().split(" ")))
	arriving_time=list(map(int, tests.strip().split(" ")))
	class_capacity=given[0]
	for arrival_time in arriving_time:
		if arrival_time>0:
			class_capacity-=1
	if  class_capacity<given[1]:
		print "YES" #CLASS DISMISSED
	else:
		print "NO" #CLASS OK

"""
def makeProfAngry(profs_class, arriving_time):
	profs_class=list(map(int, input().strip().split()))
	arriving_time=list(map(int, input().strip().split()))
	class_capacity=profs_class[0]
	threshold=profs_class[1]
	for time in arriving_time:
		if time>0:
			class_capacity-=1
	if  class_capacity<profs_class[1]:
		print ("yes")
	else:
		print ("no")

print(makeProfAngry(profs_class, arriving_time))

"""
