## Two appraches for string problems using Sliding Window
1. HashMap, to store a pair with <Character, Integer> which represents the frequency of the character. If HashMap is used, then counter is the size of HashMap. When we traverse the input, we only decrease the counter when the frequency of that letter becomes 0 which means we have exactly one letter with all its occurences matched.
2. Array, if the input is all ASCII character, then an array with size of 256 is good. But if the input is only lower-case letter or upper-case letter, then an array with the size of only 26 is enough. In that case with the assumption that the input is only lower-case letter, the frequency of the character c is freq[c - 'a']. If array is used, then counter is the size of the target string. We only decrease the counter when the value of that character in the freq array is positive which means that character appears in the target string. Because all the charaters that are not in the target string will have a negative number after we scan it.

problems:
- 438. Find All Anagrams in a String
- 567. Permutation in String
- 076. Minimum Window Substring
- 003. Longest Substring Without Repeating Characters
- 340. Longest Substring with At Most K Distinct Characters
- 159. Longest Substring with At Most Two Distinct Characters
- 424. Longest Repeating Character Replacement

