class Solution:

    def  longestChain(words):
        currmost = 0
        wordset = set(words)
        for item in wordset:
            most = 0
            n = len(item)
            checkitem = item
            i = 0
            while i < n:
                if i == 0:
                    checkitem = checkitem[1:]
                elif i == n-1:
                    checkitem = checkitem[0:-1]
                else:
                    checkitem = checkitem[0:i]+checkitem[i:]
                if checkitem in wordset:
                    most+=1
                    n = len(checkitem)
                else: i+=1
            currmost = max(currmost,most)
        return currmost

if __name__ == '__main__':
    Solution().longestChain(["a","ab","abc"])





def  longestChain(words):
    words, mapi, word_set = sorted(words, key=lambda x:len(x), reverse=True), {}, set(words)
    for word in words:
        if word not in mapi: mapi[word] = 1
        for i in xrange(len(word)):
            new_word = word[:i]+word[i+1:]
            if new_word in word_set:
                mapi[new_word] = max(mapi.get(new_word, 1), mapi[word]+1)
    return max(mapi.values())