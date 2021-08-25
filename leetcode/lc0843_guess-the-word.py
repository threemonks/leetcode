"""
843. Guess the Word
Hard

929

995

Add to List

Share
This is an interactive problem.

You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.



Example 1:

Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"], numguesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Example 2:

Input: secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10
Output: You guessed the secret word correctly.


Constraints:

1 <= wordlist.length <= 100
wordlist[i].length == 6
wordlist[i] consist of lowercase English letters.
All the strings of wordlist are unique.
secret exists in wordlist.
numguesses == 10
"""
from typing import List

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        pass

"""
The goal is to design algo to get the secret in as little as possible guesses

1. let's call master.guess() 10 times or until we find the secret word, whichever comes first.
2. trying to narrow the candidates after each time we call master.guess()
3. how to narrow the candidates? => for each guess returning value x, only keep the ones that have exact x matches with word
4. how to select word in candidates as the input of master.guess()

//pseudocode version 3
for(int i = 0, matches = 0; i < 10 && matches != 6; i ++){
	matches = master.guess(randomly select a word in candidates);
	for(String candidate: candidates){
		if(matches == getMatches(candidate, word)){
			tempCandidates.add(candidate);
		}
	}

	candidates = tempCandidates;
}

"""
import random


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def matches(word1, word2):
            # count number of char matches
            # print('word1=%s word2=%s' % (word1, word2))
            return sum([bool(word1[i] == word2[i]) for i in range(6)])

        cand = random.choice(wordlist)
        match_count = master.guess(cand)

        count = 0
        while count < 10 and match_count != 6:  # try up to 10 times or a full match
            if match_count == 6:
                return
            # filter wordlist to keep only words with exactly matches char match
            wordlist = [word for word in wordlist if matches(word, cand) == match_count]
            # print('count=%s match_count=%s wordlist=%s' % (count, match_count, wordlist))
            cand = random.choice(wordlist)
            match_count = master.guess(cand)
            count += 1
