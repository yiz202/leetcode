class Solution:
    # @param {string} num1 a non-negative integers
    # @param {string} num2 a non-negative integers
    # @return {string} return sum of num1 and num2
    def addStrings(self, num1, num2):
        # Write your code here
        s = ''
        sum, carry = 0, 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:
            sum = carry
            sum += ord(num1[i]) - ord('0') if i >= 0  else 0
            sum += ord(num2[j]) - ord('0') if j >= 0  else 0
            carry = sum / 10
            s = str(sum % 10) + s
            i -= 1
            j -= 1
        if carry == 1:
            return '1' + s
        else:
            return s

