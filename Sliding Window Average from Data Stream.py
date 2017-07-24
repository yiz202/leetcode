from collections import deque


class MovingAverage(object):
    def __init__(self, size):
        # Initialize your data structure here.
        self.s = 0
        self.d = deque()
        self.size = size

    # @param {int} val an teger
    def next(self, val):
        # Write your code here
        self.d.append(val)
        self.s += val
        if len(self.d) > self.size:
            left = self.d.popleft()
            self.s -= left
        return (self.s) / (len(self.d) * 1.0)




        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param = obj.next(val)


#using list

class MovingAverage(object):
    def __init__(self, size):
        # Initialize your data structure here.
        self.holder = [0] * size
        self.s = 0
        self.i = -1
        self.size = size

    # @param {int} val an teger
    def next(self, val):
        # Write your code here
        self.s += val
        self.i += 1

        if self.i <= self.size - 1:
            self.holder[self.i] = val
            return self.s / (1.0 * (self.i + 1))
        else:
            deleteIndex = (self.i) % self.size
            self.s -= self.holder[deleteIndex]
            self.holder[deleteIndex] = val
            return self.s / (1.0 * self.size)






            # Your MovingAverage object will be instantiated and called as such:
            # obj = MovingAverage(size)
            # param = obj.next(val)