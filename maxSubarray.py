#Written by Ryan Tio
#Based on the algorithm for recursively finding a maximum subarray described in class.

import time #Library used for the timing of algorithm
import random #Library used to randomize arrays

#This function was taken from https://www.tutorialspoint.com/maximum-subarray-in-python
#And was only used to check for the correctness of the algorithms.
def maxSubArrCheck(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  dp = [0 for i in range(len(nums))]
  dp[0] = nums[0]
  for i in range(1,len(nums)):
     dp[i] = max(dp[i-1]+nums[i],nums[i])
  #print(dp)
  return max(dp)

#Helper function for the recursive subarray.
def maxCrossSub(A, l, m, r):
	leftIndex = -1
	rightIndex = -1
	leftMax = float('-inf')
	tempSum = 0
	for i in range(m, l - 1, -1): #for i in the mth position down to the lth position
		tempSum = tempSum + A[i]
		if(tempSum > leftMax):
			leftMax = tempSum
			leftIndex = i
	rightMax = float('-inf')
	tempSum = 0
	for j in range(m + 1, r + 1): #for j in the m+1th position to the rth position
		tempSum = tempSum + A[j]
		if(tempSum > rightMax):
			rightMax = tempSum
			rightIndex = j
	return [leftIndex, rightIndex, leftMax + rightMax]

#Note, the value r should be initialized to sizeof(A) - 1
#This is the recursive algorithm for finding the maximum subarray.
def recursiveSubArr(A, l, r):
 	if l == r:
 		return [l, r, A[l]]
 	else:
 		m = int((l + r) / 2) #Find midpoint of the array
 		maxLeftSubarray = recursiveSubArr(A, l, m)
 		maxRightSubarray = recursiveSubArr(A, m + 1, r)
 		maxCrossSubarray = maxCrossSub(A, l, m, r)
 	if(maxLeftSubarray[2] >= maxRightSubarray[2] and maxLeftSubarray[2] >= maxCrossSubarray[2]):
 		return maxLeftSubarray
 	elif(maxRightSubarray[2] >= maxLeftSubarray[2] and maxRightSubarray[2] >= maxCrossSubarray[2]):
 		return maxRightSubarray
 	else:
 		return maxCrossSubarray

#Note, the value size should be initialized to sizeof(A)
#This is the brute force algorithm for finding the maximum subarray
def BFSubArray(A, size):
 	maxSoFar = float('-inf')
 	tempSum = 0
 	ans = [-1, -1, float('-inf')]
 	for i in range(0, size):
 		for j in range(i, size):
 			for k in range(i, j + 1):
 				tempSum = tempSum + A[k]
 			if(maxSoFar < tempSum):
 				maxSoFar = tempSum
 				ans[0] = i
 				ans[1] = j
 				ans[2] = maxSoFar
 			tempSum = 0
 	# print(ans)
 	return ans


def generateArray(size):
	a = []
	for i in range(0, size):
		a.append(random.randint(-1000, 1000))
	return a

def timeRecur(size):
	b = generateArray(size)
	start = time.perf_counter()
	recursiveSubArr(b, 0, len(b) - 1)
	end = time.perf_counter()
	return end - start
	# print("{end - start} seconds")


def timeBF(size):
	b = generateArray(size)
	start = time.perf_counter()
	BFSubArray(b, size)
	end = time.perf_counter()
	return end - start


def timeBoth(size, trials):
	finals = [0, 0]
	timesRecur = []
	timesBF = []
	for i in range(0, trials + 1):
		timesRecur.append(timeRecur(size))
	finals[0] = sum(timesRecur) / len(timesRecur)
	for i in range(0, trials + 1):
		timesBF.append(timeBF(size))
	finals[1] = sum(timesBF) / len(timesBF)
	return finals

def main():
	#Parameters for testing times
	size = 7
	trials = 100000
	times = timeBoth(size, trials)
	print("Size = ", size, "Trials = ", trials)
	print("Recur = ", times[0], "BF = ", times[1])



if __name__ == "__main__":
	main()