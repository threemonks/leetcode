"""
Parse english words into int:

Example 1:

Input: "Three hundred million"
Output: 300,000,000
Example 2:

Input: "Five Hundred Thousand"
Output: 500,000


There are two types of tokens: additive and multiplicative. For numbers below 100 we need additive tokens and for rest we need multiplicative tokens.
For example: 'one hundred twenty two' -> we take first token 'one' , set ans = 1, then we proceed. At second token ('thousand') we need to multiply it with 1000. Now for rest of the string
('twenty two') we call this function recursively and add that value to current num.
Here is a working code, fill in the rest of the token and values in dictionaries. To deal with negative values check the first token.



"""
import sys

muls = {'hundred':100, 'thousand':1000, 'million':1000000}
adds = {'one':1, 'two':2, 'three':3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine':9, 'ten':10,
        'elevent': 11, # ...
        'twenty':20, # ...
        'ninety':90
}
def str2int(toks):
    num = 0
    for i,tok in enumerate(toks):
        if tok in adds:
            num += adds[tok]
        else:
            return num*muls[tok] + str2int(toks[i+1:])
    return num

def getInt(s):
    toks = s.split()
    if toks[0] == 'negative':
          return -1*str2int(toks[1:])
    return str2int(toks)

def main():
    print(getInt(sys.argv[1]))

if __name__ == '__main__':
    main()
