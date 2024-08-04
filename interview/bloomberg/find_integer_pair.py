"""
3 542 35 23245 23 5412 354 2354 2.....  n distinct integers

(a, b)   , a-b = K (constant integer)
..

"""


def foo(my_list, K):
    my_list_set = set(my_list)

    ans = []

    for n in my_list:
        if n - K in my_list_set:
            ans.append((n, n - K))

    return ans