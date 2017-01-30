# Complete the function below.


def maxLength(a, k):
    sorta = sorted(a)
    length = 0
    t = 0
    for item in sorta:
        if k < t:
            return length-1
        t += item
        length += 1


print maxLength([3,1,2,3],4)