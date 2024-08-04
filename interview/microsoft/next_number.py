"""
给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。

下一个数 题目解析

1、遇到从右往左起第一个"01"将其转换为"10"（比num大）
同时如果出现"1111000","1110"这种1聚集在一起的情况，将"01"转化为"10"生成"10111000","10110"，但是正确答案为"10000111","10011"所以需要将转化后"10"后的1全部移到最右端（即与0交换）
2、遇到从左往右起第一个"10"将其转化为"01"(比num小)
同时如果出现"1001","10011"这种末尾聚集1的情况，将"10"转化为"01"生成"0101","01011"，但是正确答案为"0110","01110",所以需要将转化后"01"后的0全部移到最右端（即与1交换）

试了一个新的处理方式，预处理一个从0到第30位仅每位为1的一个数组然后进行处理。需要检测某一位是否为1时只需要和数组中对应的值进行与操作即可

"""


from typing import List
"""
Next Number
to get next larger, in binary format, find first 0 from right, swap it with the next 1 to its right 
"""
class Solution:
    def next_number(self, num: int) -> List[int]:
        s = bin(num)[2:] # conver to binary 0.1...
        n = len(s)

        # for larger, convert right most 01 to 10, and push all 1's after the new 10 to right most.
        larger = ''
        for i in range(n-1, -1, -1):
            if s[i] == '1' and (i-1<0 or s[i-1] == '0'):
                if i-1>= 0:
                    larger = s[:i-1] + '10' + ''.join(sorted(s[i+1:]))
                else:
                    larger = '10' + ''.join(sorted(s[i+1:]))
                break

        # for smaller, convert left most 10 to 01, and push all 0's after the new 01 to right most
        smaller = ''
        for i in range(n):
            if s[i] == '0' and (i-1<0 or s[i-1] == '1'):
                if i-1>=0:
                    smaller = s[:i-1] + '01' + ''.join(sorted(s[i+1:], reverse=True))
                else:
                    smaller = '01' + ''.join(sorted(s[i+1:], reverse=True))
                break

        print(int(smaller, 2), int(larger, 2))
        return [int(smaller, 2), int(larger, 2)]

def main():
    sol = Solution()
    assert sol.next_number(11) == [7, 13], 'fails'


if __name__ == '__main__':
   main()