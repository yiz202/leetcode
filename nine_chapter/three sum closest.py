class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here

        numbers.sort()
        small = 99999

        for i in range(len(numbers)-1):
            left = i+1
            right = len(numbers)-1
            while left< right:
                diff = abs(numbers[i]+ numbers[left]+ numbers[right]-target)
                if diff < small:
                    small = diff
                    summ = numbers[i]+ numbers[left]+ numbers[right]
                if numbers[i]+ numbers[left]+ numbers[right] > target:
                    right-=1

                elif numbers[i]+ numbers[left]+ numbers[right] < target:
                    left+=1
                else: return target
        return summ

