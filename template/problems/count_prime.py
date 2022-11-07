import time
import math

class Solution(object):
    def is_prime1(self,n):
        if n<=1: return False
        if n<=3: return True
        if n%2==0 or n%3==0: return False
        for i in range(5,math.ceil(math.sqrt(n))+1,2):
            if n%i==0: return False
        return True
    def is_prime2(self,n):
        if n<=1: return False
        if n<=3: return True
        if n%2==0 or n%3==0: return False
        i=5
        while i*i<=n:
            if n%i==0 or n%(i+2)==0: return False
            i+=6
        return True

    def count_prime1(self,n):
        c = 0
        for i in range(2, n+1):
            if self.is_prime1(i): c+=1
        return c

    def count_prime2(self,n):
        """
        create array from 2 to N,
        start i from 2, first non-zero is prime, cross out (set to 0) all its multiples
        increase i to next non-zero, which is prime, and repeat
        :param n:
        :return:
        """
        num = [i for i in range(n+1)]
        c = 0
        i = 2
        while i<=n:
            p = num[i]
            if p!=0:
                c+=1
                for k in range(2, (n//p)+1): num[k*p]=0
            i +=1
        return c

N = 1000000
s = Solution()
start = time.time()
print('Method 1:', s.count_prime1(N))
end = time.time()
print('Time:', "{:.2f}".format(end - start))

start = time.time()
print('Method 2:', s.count_prime2(N))
end = time.time()
print('Time:', "{:.2f}".format(end - start))