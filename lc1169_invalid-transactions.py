"""
1169. Invalid Transactions
Medium

184

1073

Add to List

Share
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.



Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]


Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.

"""
from collections import defaultdict
from typing import List

"""
HashMap

group transaction by user, then sort by time, and check if different city within 60 min

mistakes:
1. transaction 1, 2, 3 could all be invalid because 1, and 2, and 3 are all within 60 minutes
2. being too close to another invalid transaction will not cause this transaction to be invalid
"""


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        ans = list()
        user_txs = defaultdict(list)

        for tx in transactions:
            user, time, amount, city = tx.split(',')
            user_txs[user].append([int(time), int(amount), city])

        for user, txs in user_txs.items():
            txs = sorted(txs)
            l = len(txs)
            for i in range(l):
                tx0 = txs[i]
                if tx0[1] > 1000:
                    ans.append(','.join([user] + [str(f) for f in tx0]))
                elif any([abs(tx0[0] - txs[j][0]) <= 60 and tx0[2] != txs[j][2] for j in range(l) if i != j]):
                    ans.append(','.join([user] + [str(f) for f in tx0]))

        return ans


def main():
    sol = Solution()
    assert sol.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]) == ["alice,20,800,mtv","alice,50,100,beijing"], 'fails'

    assert sol.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]) == ["alice,50,1200,mtv"], 'fails'

    assert sol.invalidTransactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]) == ["bob,50,1200,mtv"], 'fails'

if __name__ == '__main__':
   main()