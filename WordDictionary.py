class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode) 
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] 
        node.is_end_of_word = True            

    def search(self, word: str) -> bool:
        def _search(word, node):
            for i in range(len(word)):
                if word[i] == ".":
                    for char in node.children:
                        if _search(word[i+1:],node.children[char]):
                            return True
                elif word[i] not in node.children:
                    return False
                
                node = node.children[word[i]]
            return node.is_end_of_word
        return _search(word,self.root)


 
