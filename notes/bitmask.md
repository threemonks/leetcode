## bitmasks tricks
* bitmask count number of 1 bits
  bin(n).count('1')

    def bit_count(n):
        cnt = 0
        while n:
            n &= n-1
            cnt += 1

        return cnt

* get most siginificant 1 bit
  n &= n-1

* set i-th bit
    mask |= (1<<i)

* loop all subset of bits
    sub_state = state
    while sub_state >=0:
        sub_state = (sub_state-1) & state

* verify if submask is a subset of mask
        if submask & mask == submask:
