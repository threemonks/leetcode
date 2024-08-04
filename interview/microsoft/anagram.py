"""
字符串-兄弟字符串

https://www.1point3acres.com/bbs/thread-768238-1-1.html

如果两个字符串的字符一样，但是顺序不一样，被认为是兄弟字符串，问如何在迅速匹配兄弟字符串（如，bad和adb就是兄弟字符串）

1、O（n*m）的轮询方法

判断string2中的字符是否在string1中： String 1: ABCDEFGHLMNOPQRS String 2: DCGSRQPO

判断一个字符串是否在另一个字符串中，最直观也是最简单的思路是，针对第二个字符串string2中每一个字符，与第一个字符串string1中每个字符依次轮询比较，看它是否在第一个字符串string1中。

2、 O(mlogm)+O(nlogn)+O(m+n)的排序方法

一个稍微好一点的方案是先对这两个字符串的字母进行排序，然后同时对两个字串依次轮询。两个字串的排序需要(常规情况)O(mlogm) + O(nlogn)次操作，之后的线性扫描需要O(m+n)次操作。

步骤如下： 1、判断两个字符串的长度是否一样,如果不一样则退出。 2、每个字符串按字符排序，如acb排序之后是abc,如果是兄弟字符串的话，排序之后是一样的。


4、 O（n）到 O（n+m）的素数方法
你可能会这么想：O(n+m)是你能得到的最好的结果了，至少要对每个字母至少访问一次才能完成这项操作，而上一节最后的俩个方案是刚好是对每个字母只访问一次。

给26个字符依次赋予质数。质数是比较特殊的一堆数字，它们只能被1和本身整除。以给a赋值2、给b赋值3、给c赋值5、给d赋值7、给e赋值11、给f赋值13。

加法：两个字符串中的所有字符都赋值了，接着让它们各自相加，如果两个字符串得出的结果是一样的，那它们是兄弟字符串。但是，b+f=3+13=16；c+e=5+11=16，所以有误；

乘法：两个字符串中的所有字符让它们各自相乘，方法是对的，但是会溢出，所以要大整数处理了；用平方和或者立方和：考虑平方和会不会解决加法有误，乘法溢出：b*b+f*f=3*3+13*13=178；c*c+e*e=5*5+11*11=146

然后——轮询第二个字符串，用每个字母除它。如果除的结果有余数，这说明有不匹配的字母。如果整个过程中没有余数，你应该知道它是第一个字串恰好的子集了。

如果是加法，那么使用一个类似于set的数据结构来记录字符串中字母出现的频次即可,但是空间开销会比素数更大（素数法要求分配素数也是需要空间的，虽然是常数级）。代码如下：

/*
如果两个字符串的字符一样，但是顺序不一样，被认为是兄弟字符串，
问如何在迅速匹配兄弟字符串（如，bad和adb就是兄弟字符串）。
*/
#include <iostream>
using namespace std;
  
int isBroStr(char *str1, char *str2)
{
    int a[26 * 2] = {0};
    int i, strLen;
     
    if (!str1 && !str2)
        return 1;
    else if (!str1 || !str2)
        return 0;
    else
    {
        if(strlen(str1) != strlen(str2))
            return 0;
        strLen = strlen(str1);
        for(i = 0; i < strLen; i++)
        {
            ++a[str1[i] - 'A'];
            --a[str2[i] - 'A'];
        }
        for(i = 0; i < 26 * 2; i++)
            if (a[i])
                return 0;
        return 1;
    }       
}
  
int main()
{
    char *str1 = "asdfaabAAB";
    char *str2 = "asdfAABaab";
    if (isBroStr(str1, str2))
        cout << " String 1 and String 2 are brothers!" << endl;
    else
        cout << " String 1 and String 2 are not brothers!" << endl;
    system("PAUSE");
    return 0;
}

"""

class Solution:
    def valid_anagram(self, s1: str, s2: str) -> bool :
        return sorted(s1) == sorted(s2)

def main():
    sol = Solution()
    assert sol.valid_anagram('abc', 'bca') == True, 'fails'

if __name__ == '__main__':
   main()