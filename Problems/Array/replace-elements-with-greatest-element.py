arr = [5,18,9,12,4,17,2,7,13]
mx =-1
ln = len(arr)
tmp = -1
for i in range(ln-1,0,-1):
	if i == (ln-1):
		mx = arr[i]
		tmp = arr[i]
		arr[i] = -1
	print(arr[i], mx)
	if (tmp>=mx):
		mx = arr[i]
		tmp = arr[i-1]
		arr[i-1] = mx
	else:
		tmp = arr[i-1]
		arr[i-1] = mx
print(arr)