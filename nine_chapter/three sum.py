class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):

        # write your code here
        solution = set()
        numbers = sorted(numbers)


        for i in range(len(numbers)-1):
            left = i+1
            right = len(numbers)-1
            while left< right:
                possible = numbers[i]+numbers[left]+numbers[right]
                if possible == 0:
                    li = tuple(sorted([numbers[i],numbers[left],numbers[right]]))
                    solution.add(li)
                    left+=1
                    right-=1

                elif possible < 0:
                    left+=1
                else :
                    right-=1
        return list(solution)
