
ln = int(input())
nums = []
for i in range(ln):
    nums.append(int(input()))
def calculat(nums):
    if (len(nums)==1):
        return "false"
    else:
        for ind,elmnt in enumerate(nums):
            indx = ind+1
            if((indx)==len(nums)):
                return "false"
            for indd,elmnt in enumerate(nums):
                if((indx)==len(nums)):
                    print("array finished")
                    print(indx)
                    break
                if((nums[ind]==nums[indx])):
                    print("true got")
                    return "true"
                indx = indx+1
    return "false"


print(calculat(nums))