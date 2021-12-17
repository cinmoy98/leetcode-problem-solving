nums = list([0,0,0,1,1,1,2,3,4,5,5,5,6,7,8,9,9,9,10])
indx = 0
temp_indx = None
chng_flag = False
val_count =0
# for i,elmnt in enumerate(nums):
# 	if elmnt == 4:
# 		val_count = val_count+1
# 		if indx is None:
# 			indx = i
# 			temp_indx = indx
# 			chng_flag = True
# 			print(indx)
# 		else:
# 			continue
# 	else:
# 		if chng_flag == True:
# 			nums[temp_indx] = elmnt
# 			print(nums)
# 			temp_indx = temp_indx+1
# 			indx=None
# 		else:
# 			continue
# print(nums)
# val = 2
# for i,elmnt in enumerate(nums):
# 	if elmnt == val:
# 		val_count = val_count+1
# 		if indx is None:
# 			indx = i
# 			temp_indx = indx
# 			chng_flag = True
# 		else:
# 			continue

# 	else:
# 		if chng_flag == True:
# 			nums[temp_indx] = elmnt
# 			temp_indx=temp_indx+1
# 			nums[i]=val
# 		else:
# 			continue

# print(nums)

for i,elmnt in enumerate(nums):
	if i==0:
		continue
	else:
		if nums[i]==nums[i-1]:
			val_count = val_count+1
			if chng_flag==False:
				indx = i
				chng_flag = True
				continue
			else:
				continue
		else:
			if chng_flag==True:
				nums[indx] = nums[i]
				indx=indx+1
print(len(nums))
print(nums[0:len(nums)-val_count])
