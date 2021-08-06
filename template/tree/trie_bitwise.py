class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        p = self.root
        for b in range(31, -1, -1):  # store most significant bit at root, less significant bit towards leaf
            if (1 << b) & number:
                if not p.one:
                    p.one = TrieNode()
                p = p.one
            else:
                if not p.zero:
                    p.zero = TrieNode()
                p = p.zero

        p.value = number  # store value at leaf node for easier access

def main():
    trie = Trie()

    for num in [1, 2, 3, 4]:
        trie.insert(num)

if __name__ == '__main__':
    main()

