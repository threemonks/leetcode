"""
Amazon
The Unix find command allows you to search for files under a given directory. You can specify criteria for files you are interested in.
Imagine that you need to write code in a high level language like java, that does things similar to the find command. I would like you to focus on 2 uses cases at first.
Find all files over 5 MB somewhere under a directory.
Find all XML files somewhere under a directory.
I would like you to create a library that lets me do this easily. Keep in mind that these are just 2 uses cases and that the library should be flexible.


implemnet linux find command as an api ,the api willl support finding files that has given size requirements and a file with a certain format like

find all file >5mb
find all xml
Assume file class
{
get name()
directorylistfile()
getFile()
create a library flexible that is flexible
Design clases,interfaces.

key points:
1. abstraction of filters (two type of filters can share same base class)
2. logical OR / AND on filtering
3. handle symbolic link

"""
import datetime
import re
import unittest

class File:
    FILE = 0
    DIRECTORY = 1
    SYMBOLIC_LINK = 2
    def __init__(self, name, size=0, ftype=0, mtime=None):
        self.name = name
        self.size = size
        self.type = ftype
        self.mtime = mtime
        self.extension = name.split(".")[-1] if '.' in name else ""
        self.children = []

class Filter:
    def match(self):
        pass

class SizeFilter(Filter):
    def __init__(self, size):
        self.size = size

    def match(self, obj):
        if obj.type != File.FILE:
            return True
        return obj.size > self.size

class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def match(self, obj):
        if obj.type == File.DIRECTORY:
            return True
        return obj.extension == self.extension

class FileSystem:
    def __init__(self):
        self.filters = []

    def add_filter(self, f, op='AND'):
        """

        :param f:
        :param op: boolean operator AND or OR, default to AND
        :return: a Filter
        """
        if isinstance(f, Filter):
            self.filters.append([f, op])

    def apply_filter(self, obj):
        """

        :param f: file object to apply filters on
        :return:
        """
        result = True
        for f, op in self.filters:
            if op == 'AND':
                result = result and f.match(obj)
            elif op == 'OR':
                result = result or f.match(obj)

        return result

    def find(self, obj):
        """

        :param root: root dir to traverse
        :return: return iterator or result obj names
        """
        if obj.type == File.FILE:
            if self.apply_filter(obj):
                return [obj.name]
        elif obj.type == File.DIRECTORY:
            # recursively find results
            res = []
            if self.apply_filter(obj):
                for child in obj.children:
                    res += self.find(child)
            return res
        elif obj.type == File.SYMBOLIC_LINK: # treat like file
            if self.apply_filter(obj):
                return [obj.name]
        return []

def main():
    fs = FileSystem()
    d = File('testdirectory', size=8, ftype=1, mtime=datetime.datetime.now())
    d2 = File('testdirectory2', size=1024, ftype=1, mtime=datetime.datetime.now())
    f1 = File('testfile', size=10*1024*1024, ftype=0, mtime=datetime.datetime.now())
    f2 = File('testfile.xml', size=6*1024*1024, ftype=0, mtime=datetime.datetime.now())
    s1 = File('symlink', size=8, ftype=2, mtime=datetime.datetime.now())
    d.children.append(d2)
    d.children.append(f1)
    d.children.append(f2)
    d.children.append(s1)

    size_filter = SizeFilter(size=5*1024*1024)
    fs.add_filter(size_filter)

    print(fs.find(d))

    extension_filter = ExtensionFilter(extension='xml')
    fs.add_filter(extension_filter)

    print(fs.find(d))

if __name__ == '__main__':
    main()
