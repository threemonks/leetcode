"""
1166. Design File System
Medium

454

51

Add to List

Share
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.


Example 1:

Input:
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output:
[null,true,1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input:
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output:
[null,true,true,2,false,-1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.


Constraints:

The number of calls to the two functions is less than or equal to 104 in total.
2 <= path.length <= 100
1 <= value <= 10^9
"""
"""
Hash Table / Design
"""
from collections import defaultdict
class FileSystem0:

    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        # validation
        if path == '/' or len(path) == 0 or path in self.paths:
            return False

        parent = path[:path.rfind('/')]

        if len(parent) > 1 and parent not in self.paths: # if parent path does not exist yet
            return False

        self.paths[path] = value

        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

"""
Trie based approach
"""

class TrieNode(object):
    def __init__(self, name):
        self.map = defaultdict(TrieNode)
        self.name = name
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode("")

    def createPath(self, path, value):
        components = path.split("/")

        cur = self.root

        for i in range(1, len(components)):
            name = components[i]

            if name not in cur.map:
                if i == len(components)-1: # last element in path
                    cur.map[name] = TrieNode(name)
                else: # parent not found
                    return False
            # go to next level
            cur = cur.map[name]

        # value not equal to -1 means the path already exists in the trie
        if cur.value != -1:
            return False

        cur.value = value

        return True

    def get(self, path):
        components = path.split("/")

        cur = self.root

        for i in range(1, len(components)): # skip root which is empty name
            name = components[i]
            if name not in cur.map:
                return -1
            cur = cur.map[name]

        return cur.value

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

def main():
    fs = FileSystem()
    assert fs.createPath("/a", 1) is True, 'fails'
    assert fs.get("/a") == 1, 'fails'

    assert fs.createPath("/leet", 1) is True, 'fails'
    assert fs.createPath("/leet/code", 2) is True, 'fail'
    assert fs.get("/leet/code") == 2, 'fails'
    assert fs.createPath("/c/d", 1) is False, 'fail'
    assert fs.get("/c") == -1, 'fail'

if __name__ == '__main__':
   main()