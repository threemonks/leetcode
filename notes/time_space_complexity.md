Time and Space Complexity
1. divide & conquer - time complexity depends on actual function >N^2
    https://www.csd.uwo.ca/~mmorenom/CS874/Lectures/Introduction.html/node16.html

    T(n) = a T(n/b) + f (n)
    a = 1 => ??

2. recursion - faboncial series - 2^N, but in general, could be from O(logN) to O(N) to O(N^2) to O(2^N)
    https://www.ideserve.co.in/learn/time-and-space-complexity-of-recursive-algorithms
    https://stackoverflow.com/questions/13467674/determining-complexity-for-recursive-functions-big-o-notation

int recursiveFun1(int n)
{
    if (n <= 0)
        return 1;
    else
        return 1 + recursiveFun1(n-1);
}

=> O(N)

return 1 + recursiveFun2(n-5);

=> O(N)

return 1 + recursiveFun3(n/5);

=> O(log(N))

void recursiveFun4(int n, int m, int o)
{
    if (n <= 0)
    {
        printf("%d, %d\n",m, o);
    }
    else
    {
        recursiveFun4(n-1, m+1, o);
        recursiveFun4(n-1, m, o+1);
    }
}

=> O(2^N)




