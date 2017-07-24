
def chooserand(self,k):
    x = 1
    y = 1
    res = []
    next = 0
      while next < k+1:
          res.append(x)
          res.append(y)
          next = x+y
          y = next
          x = y
chooserand(10)