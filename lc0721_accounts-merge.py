"""
721. Accounts Merge
Medium

2384

428

Add to List

Share
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.



Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.

"""
from collections import defaultdict
from typing import List

"""
DFS

build graph adj_list, connect two emails if they are in one group

then start from each of the email in the graph, DFS search all connected emails until all reachable nodes are visited, and store this as an account's email result.
"""
"""
Union-Find

assign unique id to each unique email, union emails within one accoun, or if same email appear in different accounts.

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10

"""


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        all_emails = []
        for a in accounts:
            all_emails += a[1:]

        maps = {v: i for i, v in enumerate(list(set(all_emails)))}  # email to id map

        dsu = DSU(len(maps))

        for i, a in enumerate(accounts):
            name, emails = a[0], a[1:]
            for email in emails[1:]:
                dsu.union(maps[emails[0]], maps[email])

        acct_emails = defaultdict(list)  # use dsu parent node as key
        acct_names = dict()
        # after union, we now construct new accounts list

        for i, a in enumerate(accounts):
            name, emails = a[0], a[1:]
            acct_names[dsu.find(maps[emails[0]])] = name
            for email in emails:
                acct_emails[dsu.find(maps[emails[0]])].append(email)

        result = []
        for key, val in acct_names.items():
            account = [val]
            acct_email_list = sorted(list(set(acct_emails.get(key))))
            account += acct_email_list
            result.append(account)

        return result


def main():

    sol = Solution()

    assert sorted(sol.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])) == sorted([["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]), 'fails'


if __name__ == '__main__':
   main()