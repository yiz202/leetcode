class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        def helper(leftnum, rightnum, op):
            if op == '*': return leftnum * rightnum
            if op == '+':
                return leftnum + rightnum
            else:
                return leftnum - rightnum

        res = []
        if input.isdigit(): return [int(input)]
        for i in range(len(input)):
            if input[i] in ['+', '*', '-']:
                leftres = self.diffWaysToCompute(input[:i])
                rightres = self.diffWaysToCompute(input[i + 1:])
                for l in leftres:
                    for r in rightres:
                        res.append(helper(l, r, input[i]))
        return res



Solution().diffWaysToCompute("2*3-4")