# unbalanced binary tree

#        66
#     44     77
#   22      1
#         3

# output:
# 66
# 44 77
# 22 1
# 3

# - most memory efficient way AND
# - fastest way

# """

# n.l n.r n.v
# N nodes
# time O(N)
# space O(N)
def traverse(n):
    q = [n]

    while q:
        l = len(q)
        newq = []
        for i in range(l):
            if i.l:
                newq.append(i.l)
            if i.r:
                newq.append(i.r)

        print(" ".join([str(i.v) for i in q]))
        q = newq[:]