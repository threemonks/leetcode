"""
588. Design In-Memory File System
Hard

https://leetcode.com/problems/design-in-memory-file-system/

"""
import pickle
from typing import List

"""
basic idea:

Use doubly linked list node to represents file/dir, have children as dictionary of filename to file object (DLinkedNode), each file object link to both its parent and children

mistakes:
1. add file content to existing file is appending
2. multiple children output in lexicographic order
3. when ls returns single filename, it needs to be wrapped in list
"""

class DLinkedNode:
    def __init__(self, name=None, parent=None):
        self.name = name
        self.parent = parent
        self.children = {'.': self, '..': self.parent}
        self.is_file = False
        self.content = None


class FileSystem:

    def __init__(self):
        self.root = DLinkedNode()
        self.root.name = '/'
        self.root.parent = self.root
        self.root.children['..'] = self.root

    def ls(self, path: str) -> List[str]:
        # print(self.root.children.keys())
        if path == '/':
            return sorted([f for f in self.root.children.keys() if f not in ['.', '..']])

        parts = path.lstrip('/').split('/')
        curr = self.root
        for part in parts:
            curr = curr.children.get(part)

        if curr.is_file:
            return [curr.name]
        else:
            return sorted([f for f in curr.children.keys() if f not in ['.', '..']])

    def mkdir(self, path: str) -> None:
        parts = path.lstrip('/').split('/')
        curr = self.root
        for part in parts:
            child = curr.children.get(part)
            if child is None:
                curr.children[part] = DLinkedNode(name=part, parent=curr)
            curr = curr.children.get(part)

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.lstrip('/').split('/')
        curr = self.root
        for part in parts[:-1]:
            curr = curr.children.get(part)

        filename = parts[-1]
        if filename in curr.children:
            curr.children[filename].content += content
        else:
            newfile = DLinkedNode(filename)
            newfile.is_file = True
            newfile.content = content
            curr.children[filename] = newfile

    def readContentFromFile(self, filePath: str) -> str:
        parts = filePath.lstrip('/').split('/')
        curr = self.root
        for part in parts:
            curr = curr.children.get(part)

        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)



def main():
    obj = FileSystem()
    assert obj.ls('/') == [], 'fails'
    assert obj.mkdir("/a/b/c") is None, 'fails'
    assert obj.addContentToFile("/a/b/c/d", "hello") is None, 'fails'
    assert obj.ls("/") == ["a"], 'fails'
    assert obj.readContentFromFile("/a/b/c/d") == "hello", 'fails'

    obj = FileSystem()
    assert obj.ls('/') == [], 'fails'
    assert obj.mkdir("/m") is None, 'fails'
    assert obj.ls("/m") == [], 'fails'
    assert obj.mkdir("/w") is None, 'fails'
    assert obj.ls("/") == ['m', 'w'], 'fails'
    assert obj.ls("/w") == [], 'fails'
    assert obj.ls("/") == ['m', 'w'], 'fails'
    assert obj.addContentToFile("/dycete", "emer") is None, 'fails'
    assert obj.ls("/w") == [], 'fails'
    assert obj.ls("/") == ["dycete","m","w"], 'fails'
    assert obj.ls("/dycete") == ["dycete"], 'fails'

if __name__ == '__main__':
   main()