arr = [3,3,2,4,3,3]
idx = 0
for i,elmnt in enumerate(arr):
	if elmnt%2==0:
		temp = arr[idx]
		arr[idx] = elmnt
		arr[i] = temp
		idx = idx+1
print(arr)