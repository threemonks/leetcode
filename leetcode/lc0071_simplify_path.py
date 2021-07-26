"""
71. Simplify Path
Medium

Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period '.' refers to the current directory. Furthermore, a double period '..' moves the directory up a level.

Note that the returned canonical path must always begin with a slash '/', and there must be only a single slash '/' between two directory names. The last directory name (if it exists) must not end with a trailing '/'. Also, the canonical path must be the shortest string representing the absolute path.



Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: path = "/a/./b/../../c/"
Output: "/c"


Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid Unix path.

"""
import math
from functools import lru_cache
from typing import List

"""
use stack to keep track of which directory we are currently at,
for each new dir, if dir == '.', skip,
if dir == '..', pop stack
elif not empty, push into stack
else # empty skip (do nothing)
and finally join back using separator /

time O(N)
space O(N)

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for d in path.split('/'):
            # print('d=%s' % d)
            if d == '.':
                pass
            elif d == '..':
                if stack:
                    stack.pop()
            elif d:
                stack.append(d)
            else:
                # print('empty dir %s' % d)
                pass

        return '/' + ('/'.join(stack) if stack else '')

def main():
    sol = Solution()
    assert sol.simplifyPath("/home/") == "/home", 'fails'

    assert sol.simplifyPath("/../") == "/", 'fails'

    assert sol.simplifyPath("/home//foo/") == "/home/foo", 'fails'

    assert sol.simplifyPath("/a/./b/../../c/") == "/c", 'fails'

if __name__ == '__main__':
   main()