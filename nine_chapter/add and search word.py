class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size  = 0

    def insert(self,word):
        if len(word) == 0:
            return
        i = 0
        p = self.root
        while i < len(word):
            if p.children[ord(word[i])-ord('a')] == None:
                new_TriNode = TrieNode()
                p.children[ord(word[i])-ord('a')]=new_TriNode
                p = new_TriNode
            else:
                p = p.children[ord(word[i])-ord('a')]
            i+=1
        p.leaf = True

    def search(self,word):
        if len(word) == 0:
            return False
        return self.research(word,self.root,0)
    def research(self,word,triNode,i):
        if i == len(word):
            if triNode.leaf == True:
                return True
            return False
        if word[i] == '.':
            for j in range(26):
                if triNode.children[j]!=None:
                    if self.research(word,triNode.children[j],i+1) == True:
                        return True
            # if i == len(word)-1: return True
            return False

        if triNode.children[ord(word[i])-ord('a')]:
            return self.research(word,triNode.children[ord(word[i])-ord('a')],i+1)
        else: return False

class TrieNode:
    def __init__(self):
        self.leaf = False
        self.children = [None]*26












class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
        self.trie = Trie()


    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        self.trie.insert(word)


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
if __name__ == '__main__':
    w = WordDictionary()
    w.addWord("ran")
    w.addWord("rune")
    w.addWord("runner")
    w.addWord("runs")
    w.addWord("add")
    w.addWord("adds")
    w.addWord("adder")
    w.addWord("addee")
    w.search("add")
