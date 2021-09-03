"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5


Constraints:

-1000 <= a, b <= 1000
"""
"""
Bit Manipulation

XOR ^ will do bit-wise add, except not handling carry, because

1   =>  001 
2   =>  010 
1^2 =>  011 (2+1 = 3)

3  => 011 
2  => 010 
3^2=> 001  

to find carry, we can do AND &

3    =>  011 
2    =>  010 
3&2  =>  010

now we need to add it to the previous value we generated i.e ( 3 ^ 2), but the carry should be added to the left bit of the one which genereated it.
so we left shift it by one so that it gets added at the right spot.

Hence (3&2)<<1 => 100

so we can do

3^2         =>  001 
(3&2)<<1    =>  100 

Now xor them, which will give 101(5) , we can continue this until the carry becomes zero.

Why would a&b << 1 goes to zero eventually?

a&b << 1 will introduce an 0-bit and has the ability to reduce a head 1-bit, 

To deal with the fact that python allows int much larger than 32 bits, manually bound the length of sum and carry by setting up a mask 0xFFFFFFFF. & this mask with an (very long) integer will only keep the last 32 bits. Then, at each step of the loop, we & sum and carry with this mask

at last, we also need to deal with when a+b is negative in 32 bit

time O(b) - b = number of bits in input
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff # 32 bit mask in hexadecimal
        while b:
            sums = (a^b) & mask # ^ get different bits, add
            b = ((a&b)<<1) & mask # & gets double 1s, <<1, moves carry
            a = sums

        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        if (a>>31) & 1:
            return ~(a^mask)
        else:
            return a


def main():
    sol = Solution()
    assert sol.getSum(a = 1, b = 2) == 3, 'fails'

    assert sol.getSum(a = 2, b = 3) == 5, 'fails'

if __name__ == '__main__':
   main()