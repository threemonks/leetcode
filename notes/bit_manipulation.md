## Two's complement
* The two's complement of an N-bit number is defined as its complement with respect to 2N; the sum of a number and its two's complement is 2N. For instance, for the three-bit number 0102, the two's complement is 1102, because 0102 + 1102 = 10002 = 810 which is equal to 23. The two's complement is calculated by inverting the bits and adding one.

## bitmasks operations
* bitmask count number of 1 bits
  bin(n).count('1')

    def bit_count(n):
        cnt = 0
        while n:
            n &= n-1
            cnt += 1

        return cnt

## Bit operations
* Set union A | B
* Set intersection A & B
* Set subtraction A & ~B
* Set negation ALL BITS ^A or ~A
* Set bit A |= (1<<bit)
* Clear A &= ~(1<<bit)
* Test bit (A & (1<<bit)) == 1
* Extract last bit (least siginificant) A & (-A) or A & (A-1) or x^(x&(x-1))
* Clear last bit (least siginificant) A & (A-1)

* get most siginificant 1 bit
  n &= n-1

* loop all subset of bits
    sub_state = state
    while sub_state >=0:
        sub_state = (sub_state-1) & state

* verify if submask is a subset of mask
        if submask & mask == submask:
