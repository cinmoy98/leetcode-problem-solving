nums1 = [0,0,3,0,0,0,0,0,0]
nums2 = [-1,1,1,1,2,3]
m=3
n=6
i = m-1
j= n-1
k = m+n-1
while(i>=0 and j>=0):
	if (nums1[i]>nums2[j]):
		nums1[k] = nums1[i]
		k=k-1
		i = i-1
	else:
		nums1[k]=nums2[j]
		k=k-1
		j=j-1

while(j>=0):
	nums1[k]=nums2[j]
	k=k-1
	j=j-1

print(nums1)	