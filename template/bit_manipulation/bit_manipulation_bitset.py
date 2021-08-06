# convert integer to bit string
bin(n)[2:]

# get mask of length i with all bits set to 1
mask = (1<<i)-1

# count bits of 1
bin(mask).count('1')

def bit_count(n):
    cnt = 0
    while n:
        n &= n - 1
        cnt += 1

    return cnt

# get most significant bit
    n &= n-1

# set i-th bit
    mask |= (1<<i)

# check if i-th bit is set
    (mask & (1<<i)) > 0

# verify if submask is a subset of mask
    if submask & mask == submask:
        pass