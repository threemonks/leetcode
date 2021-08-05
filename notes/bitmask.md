## bitmasks operations
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
    b |= (1<<i)

* unset i-th bit
    b &= ~(1<<i)

* check if i-th bit is set

   b & (1<<i) == 1

* loop all subset of bits
    sub_state = state
    while sub_state >=0:
        sub_state = (sub_state-1) & state

* verify if submask is a subset of mask
        if submask & mask == submask:
