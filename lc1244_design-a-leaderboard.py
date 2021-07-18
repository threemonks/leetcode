"""
1244. Design A Leaderboard
Medium

291

60

Add to List

Share
Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.



Example 1:

Input:
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output:
[null,null,null,null,null,null,73,null,null,null,141]

Explanation:
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;


Constraints:

1 <= playerId, K <= 10000
It's guaranteed that K is less than or equal to the current number of players.
1 <= score <= 100
There will be at most 1000 function calls.
"""
"""
Design Hash Map, Sorting

time: addScore O(1)
      top O(Nlog(N))
      reset O(1)
"""
from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        sorted_scores = sorted(self.scores.values(), reverse=True)

        return sum(sorted_scores[:K])

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]


"""
Design Hash Map, Sorting

Using SortedDict to hold player count at each score, to speed out top call
time: addScore O(log(N))
      top O(log(K))
      reset O(log(N))
"""
from collections import defaultdict
from sortedcontainers import SortedDict


class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
        self.score_counts = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        old_score = self.scores[playerId]
        if -old_score in self.score_counts:
            self.score_counts[-old_score] -= 1
            if self.score_counts[-old_score] == 0:
                del self.score_counts[-old_score]
        new_score = old_score + score
        if -new_score in self.score_counts:
            self.score_counts[-new_score] += 1
        else:
            self.score_counts[-new_score] = 1
        self.scores[playerId] = new_score

    def top(self, K: int) -> int:
        total = 0
        for score, counts in self.score_counts.items():
            while K and counts:
                total += -score
                counts -= 1
                K -= 1

        return total

    def reset(self, playerId: int) -> None:
        old_score = self.scores[playerId]
        if -old_score in self.score_counts:
            self.score_counts[-old_score] -= 1
            if self.score_counts[-old_score] == 0:
                del self.score_counts[-old_score]
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

def main():
    """
    Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
    
    :return: 
    """

    obj = Leaderboard()
    obj.addScore(1, 73)
    obj.addScore(2, 56)
    obj.addScore(3, 39)
    obj.addScore(4, 51)
    obj.addScore(5, 4)
    assert obj.top(1) == 73, 'fails'
    obj.reset(1)
    obj.reset(2)
    obj.addScore(2, 51)
    assert obj.top(3) == 141, 'fails'

if __name__ == '__main__':
   main()

