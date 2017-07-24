class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []
        for i in range(len(nums)):
            if nums[i] not in heap:
                heapq.heappush(heap,nums[i])
            if len(heap) > 3:
                heapq.heappop(heap)
        if len(heap) < 3: return heap[-1]
        return heap[0]