def removeRepeat(s,letter):
    return ''.join([s[i] for i in xrange(1, len(s)) if s[i] != letter or s[i-1] != letter])
    # li = []
    # for i in s:
    #     if i == letter
    #     li.append(i)
    #
print removeRepeat('xkclueeeexejfenlneeeix', 'e')