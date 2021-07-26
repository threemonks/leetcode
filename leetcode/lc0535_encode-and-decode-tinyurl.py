"""
535. Encode and Decode TinyURL
Medium

"""
"""
Design / Hash

rolling hash of ord(c)-ord('a') for c in longUrl, mod 10**9+7
store this hash as shorturl with longUrl as key, and store reverse map as well, to enable caching for repeated hashing same longUrl

"""


class Codec:
    def __init__(self):
        self.s2l = {}
        self.l2s = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.l2s:
            return self.l2s[longUrl]

        MOD = 10 ** 9 + 7
        num = 0
        for c in longUrl:
            num = (num * 10 + ord(c) - ord('a')) % MOD

        shortUrl = str(num)
        self.s2l[shortUrl] = longUrl
        self.l2s[longUrl] = shortUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.s2l[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


def main():

    codec = Codec()
    codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))

if __name__ == '__main__':
   main()