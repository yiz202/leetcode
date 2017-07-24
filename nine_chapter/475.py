class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        # Time complexity: max(O(nlogn), O(mlogn))
        # houses = sorted(houses)
        # heaters = sorted(heaters)
        # res = 0
        # j = 0
        # for i in range(len(houses)):
        #     while j < len(heaters)-1 and abs(heaters[j+1]-houses[i]) <= abs(heaters[j]-houses[i]):
        #         j+=1
        #         continue
        #     res = max(res,abs(heaters[j]-houses[i]))
        # return res
        def findHeaterIndex(house, heater):
            left = 0
            right = len(heater)
            while left < right:
                mid = (left + right) / 2
                if house > heater[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left

        res = -1
        heaters = sorted(heaters)
        for house in houses:
            i = findHeaterIndex(house, heaters)
            if i != len(heaters): dist1 = heaters[i] - house
            if i != 0: dist2 = house - heaters[i - 1]
            if i == len(heaters):
                result = house - heaters[i - 1]
            elif i == 0:
                result = heaters[i] - house
            else:
                result = min(dist1, dist2)
            res = max(result, res)

        return res

