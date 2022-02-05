class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        maxx = []
        for num in nums:
            if num in freq:
                freq[num] = freq[num]+1
            else:
                freq[num] = 1
        heap = [(-val,key) for (key,val) in freq.items()]
        heapq.heapify(heap)
        while(k>0):
            maxx.append(heapq.heappop(heap)[1])
            k=k-1
        return maxx