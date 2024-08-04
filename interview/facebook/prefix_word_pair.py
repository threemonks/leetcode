"""
https://leetcode.com/discuss/interview-question/884347/facebook-phone-screen-returns-the-pair-words-shorter-longer

Given a set of words return a pair with prefix and then the full word. The words will only contain english lower case letters and input words are not sorted. Return the pair of words with the small word and then the larger word, for ex - 'be' then 'bee'.

Input : ["abs","app","be","apple","bee","better","bet","absolute"]
Output: [("abs","absolute"),("app","apple"),("be","bee"),("bet","better")]

I couldn't solve the problem on time however, it seems to be a trie problem where all the input words can be put in the trie and scan again. Any pointers or thoughts on how to solve?

Update: updated example with format with few more strings


"""

"""
This is an interesting code challenge.

Solution 1 - Time and Space O(n)

Build a trie time and space of O(n)
Traverse each word again and keep track if you see a prefix. time O(n)
Solution 2 - Time O(nlogn) and Space (1)

Sort the words lexicographically O(nlogn)
for each word, compare with the previous, if the previous is a smaller and prefix the current, save in the result set.
Solution 3 - Time O(n^2) and Space (1) ... more like a joke

Double loop and call it a solution ¯\_(ツ)_/¯

"""