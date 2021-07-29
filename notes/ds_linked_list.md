## LinkedList tips:
1. Always examine if the node is null before you call the next field.
2. Carefully define the end conditions of your loop.
3. complexity time: O(N) space O(1)
## Reverse Linked List
0. dummy head represents head of reversed list, for each current node, insert it in front of reversed list dummy head, and re-position reversed list dummy head, then move current node pointer to its next
1. point newhead at current node to be swapped
2. assign previous newhead to newhead.next
3. move cur to cur.next

    newhead, newhead.next, cur = cur, newhead, cur.next

step0      1,      2,     3,     4
        newhead
           cur

step1      1,      2,     3,     4
        newhead   cur

step2      2,      1,     3,     4
        newhead          cur

step3:     3,      2,     1,     4
        newhead                  cur

## Linked List - one pass - traverse n-th node from end

use one pointer curr to traverse from head to end (.next is null),
when curr moves n steps, then start another pointer p1 at head,
to move lock step with curr, when curr reaches end, p1 will be at n steps from end
