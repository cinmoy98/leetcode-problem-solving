# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
arr = [-8,-2,11,12,17]

original = 0
arr = list(set(arr))
ln = len(arr)
for i,elmnt in enumerate(arr):
	original = arr[i]
	arr[i] = arr[i]*2
	if len(set(arr))<ln:
		print(arr)
		print(set(arr))
		print(elmnt,"true")
	if original%2 == 0:
		arr[i] = original/2
		if len(set(arr))<ln:
			print("True")
	arr[i] = original
