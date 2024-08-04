"""
DoorDash obtains restaurant data from various sources which have varying quality. These sources often have duplicate merchants with minor typos in their names. The assignment is to create a list of unique restaurants across various sources ignoring the errors before onboarding them.
Definition: Similar restaurants
Two restaurants R1 and R2 are similar if we can swap a maximum of two letters (in different positions) of R1, so that it equals R2.
For example, source one may have a restaurant named "omega grill" while another source may have the same restaurant as "omgea grill".
For example, "biryani" and "briyani" are similar (swapping at positions 1 and 2). "biryani" is not similar to following, "biryeni" (no e to swap with), "briynai"(Needs 2 swap)
For a given restaurant name, find and return all the similar restaurant names in the list.
Implement the function below:
public List findSimilarRestaurants(String name, String[] list) {}


#Tests
input = "hotpot"
list = ["hottop", "hotopt", "hotpit", "httoop", "hptoot"]
print(findSimilarRestaurants(intput, list))
print(["hottop", "hotopt", "hptoot"])

input = "biryani"
list = ["biryani", "biryeni", "biriyani", "biriany", "briynai"]
print(findSimilarRestaurants(intput, list))
print(["biryani", "biriany"])

input = "omega grill"
list = ["omeag grill", "omeea grill", "omega gril", "omegla gril"]
print(findSimilarRestaurants(intput, list))
print(["omeag grill"])


Given a restaurant name, find other restaurants in the list that are k-anagrams with each other. A name is a k-anagram with another name if both the conditions below are true:
The names contain the same number of characters.
The names can be turned into anagrams by changing at most k characters in the string
For example:
name = "grammar", k = 3, and list = ["anagram"], "grammar" is k-anagram with "anagram" since they contain the same number of characters and you can change 'r' to 'n' and 'm' to 'a'.
name = "omega grill", k = 2 and list = ["jmegra frill"], "omega grill" is k-anagram with "jmega frill" since they contain same number of characters and you can change 'o' to 'j' and 'g' to 'f'
public List findKAnagrams(String name, String[] list, int K) {}

input = "anagram"
list = ["grammar", "grammer", "anagram"]
K = 2
printfindKAnagrams(intput, list, K))
print(["grammar", "anagram"])

input = "anagram"
list = ["grammar"]
K = 3
printfindKAnagrams(intput, list, K))
print(["grammar"])

input = "anagram"
list = ["grammar"]
K = 1
printfindKAnagrams(intput, list, K))
print([])

input = "omexyb grillg"
list = ["omgxca grille"]
K = 2
printfindKAnagrams(intput, list, K))
print(["omgxca grille"])

# Then the interviewer asked to make sure both algorithms are linear.

"""

from typing import List

class Solution:
    def findSimilarRestaurants(name, lst):
        pass

    def printfindKAnagrams(inputs, lst, K):
        pass

def main():
    sol = Solution()

if __name__ == "__main__":
    main()