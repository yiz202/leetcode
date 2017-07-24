class Solution:
    # @param {string} num1 a non-negative integers
    # @param {string} num2 a non-negative integers
    # @return {string} return product of num1 and num2
    def multiply(self, num1, num2):
        # Write your code here
        l1 = len(num1)
        l2 = len(num2)
        arr = [0] * (l1 + l2 + 1)
        for i in range(l1):
            for j in range(l2):
                arr[i + j] += int(num1[l1 - 1 - i]) * int(num2[l2 - 1 - j])
        for k in range(len(arr) - 1):
            arr[k + 1] += arr[k] / 10
            arr[k] = arr[k] % 10
        i = l1 + l2
        while i >= 1 and arr[i] == 0:
            i -= 1
        s = ''
        for c in arr[::-1]:
            s += str(c)
        return s

print Solution().multiply("123", "45")