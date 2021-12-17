# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = True
        incd = False
        decd = False
        for i,elmnt in enumerate(arr):
            if i == 0:continue
            if (inc == True) and (arr[i]>arr[i-1]):
                incd = True
                continue
            else:
                inc = False
            if (inc == False) and (incd == True) and (arr[i]<arr[i-1]):
                decd = True
                continue
            else:
                return False
        if incd == True and decd==True:
            return True