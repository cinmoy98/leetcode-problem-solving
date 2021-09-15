ln = int(input())
nums = []
for i in range(ln):
    nums.append(int(input()))
f_ind = 0
l = len(nums)
for ind, elmnt in enumerate(nums):
    if((ind+1)!=(l-1)):
        if(nums[ind]<nums[ind+1]):
            nums[f_ind] = elmnt
            f_ind = f_ind + 1
    else:
        if(nums[ind]<nums[ind+1]):
            nums[f_ind] = elmnt
            nums[f_ind+1] = nums[ind+1]
            fin = f_ind+2
        else:
            nums[f_ind] = elmnt
            fin = f_ind+1
        break