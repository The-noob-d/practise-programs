#leetcode two sum prob
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [3,2,4]
target = 6

def two_sum(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] ==target:
                return [i,j]
print(two_sum(nums))