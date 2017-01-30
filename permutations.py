class traced(object):
    """When the decorated function is called, the decorator should print out an ASCII art tree
    of the recursive calls and their return values. """
    depth = 0
    def __init__(self,f):
        """constructor of this decorator that takes the decorated function and set the
            decorator's field"""
        # replace this and fill in the rest of the class
        self.__f = f
        self.__name__=f.__name__
    def __call__(self,*args,**dargs):
        """ the core decorator function that takes the argument of the decorated function and
        call the function as well as implementing extra tracing features as well as handling the
        exception"""
        level = '| '*traced.depth + ',- ' + str(self.__name__) + '(' +\
                ', '.join([str(para) for para in args]) +\
                ', '.join([str(key) + '=' + str(val) for key, val in dargs.iteritems()]) + ')'
        print level
        traced.depth += 1
        try:
            res = self.__f(*args,**dargs)
        except Exception as e:
            traced.depth -= 1
            raise e
        traced.depth -= 1
        level2 = ('| ' * traced.depth) + '`- ' + repr(res)
        print level2
        return res

@traced
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 0: return []
    if len(nums) == 1: return [nums]
    res = []
    for idx, item in enumerate(nums):
        p1 = nums[:idx]
        p2 = nums[idx+1:]
        for perm in permute(p1+p2):
            perm.append(item)
            res.append(perm)
    return res


permute([1,2,3])
