#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only
# once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums
#Example 1:Input: nums = [1,1,2]
#Output: 2, nums = [1,2,_]
#Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).

n= [1,1,2]

def removeDuplicates(n):
    x,y=0,0
    count=0
    while y<len(n)-1:
        if n[y+1]==n[y]:
            count+=1
        else:
            x+=1
            n[x]=n[y+1]
        y+=1
    for i in range(x+1,len(n)):
        n[i]="_"
    print(n)
    return x+1

print(removeDuplicates(n))

