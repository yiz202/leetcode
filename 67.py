class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        new = []
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        else:
            b = '0' * (len(a) - len(b)) + b
        l = max(len(a), len(b))
        a = list(reversed(a))
        b = list(reversed(b))
        for i in range(l):
            sumi = int(a[i]) + int(b[i]) + carry
            if sumi >= 2:
                new.append(str(sumi % 2))
                carry = 1
            else:
                new.append(str(sumi))
                carry = 0
        if carry == 1:
            new.append('1')
        return ''.join(list(reversed(new)))


