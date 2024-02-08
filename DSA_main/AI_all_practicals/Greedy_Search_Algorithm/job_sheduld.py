# This sorting step is crucial in the greedy approach for job scheduling. 
# Sorting the jobs based on their deadlines allows us to prioritize the jobs with earlier deadlines,
# as we iterate through the sorted list to schedule the jobs in the schedule_jobs() function.


arr = [['a', 2, 100], ['b', 1, 40], ['c', 2, 80], ['d', 1, 20], ['e', 3, 60]]
# the array is name , deadline and profit 
print("Following is maximum profit sequence of jobs")

# length of array
n = len(arr)
# this actually the time slots 
t = 3

# Sort all jobs according to
# decreasing order of profit
for i in range(n):
#The inner loop (for j in range(n - 1 - i):) iterates over the indices from 0 to n-1-i, which effectively reduces the range of elements to consider in each iteration.
#By subtracting i from the range, the inner loop avoids comparing and swapping the already sorted elements at the end of the array.
   for j in range(n - 1 - i):
#If the value in the current element is smaller than the value in the next element, it means that the elements are out of order based on the sorting criteria
     if arr[j][2] < arr[j + 1][2]:
       arr[j], arr[j + 1] = arr[j + 1], arr[j]

#To keep track of free time slots
#here the t value refers to maximum deadline
result = [False] * t

#To store result (Sequence of jobs)
#intialize the all jobs to the -1
job = ['-1'] * t

#Iterate through all given jobs
for i in range(n):

#Find a free slot for this job
#(Note that we start from the
#last possible slot)
   for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

#Free slot found
     if result[j] is False:
       result[j] = True
       job[j] = arr[i][0]
       break

#print the sequence
print(job)