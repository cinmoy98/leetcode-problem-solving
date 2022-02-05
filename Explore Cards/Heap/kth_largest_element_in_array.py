class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        k=k-1
        while(k>0):
            heapq.heappop(nums)
            k=k-1
        return -nums[0]