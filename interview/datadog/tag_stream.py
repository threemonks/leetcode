"""
Hi, I need some help to ace an interview question. I found this question was asked during an DataDog coding interview.

There is a stream that has coming tags and also has a list of keywords, design a high performance filter to output these keywords remaining tags.
For example: given stream ['apple, facebook, google', 'banana, facebook', 'facebook, google, tesla', 'intuit, google, facebook'],
 if the keyword is ['apple'] the output should ['facebook', 'google'] because only 'apple, facebook, google' has apple.
 Similarly if the keyword is ['facebook', 'google'], the output should ['apple', 'tesla', 'intuit']. The output can be in any order and can be put into a single list/array.

I was not sure how to handle these:

High performance filter.
The tags are coming as in a stream.

"""

"""
break input tag string into tags, store it as dict of tags to set of remaining tags in the group

when querying for keyword, for each keyword, lookup the sets from the dict
if multiple keywords, take intersection of all sets found

"""
class Solution:
    def parse(self, inputs, keywords):
        maps = dict()

        for tagstr in inputs:
            tags = tagstr.split(", ")
            for idx, tag in enumerate(tags):
                other_tags_set = set(tags[:idx] + tags[idx+1:])
                if tag not in maps:
                    maps[tag] = other_tags_set
                else: # tag already in maps
                    maps[tag] = maps[tag].union(other_tags_set)

        print(f"{maps = }")
        remaining_tags = None
        for keyword in keywords:
            if remaining_tags is None:
                remaining_tags = maps[keyword]
            else: # none Empty already
                remaining_tags = remaining_tags.intersection(set(maps[keyword]))

        print(f"{remaining_tags = }")
        return sorted(list(remaining_tags))

def main():
    sol = Solution()
    inputs = ['apple, facebook, google', 'banana, facebook', 'facebook, google, tesla', 'intuit, google, facebook']
    assert sol.parse(inputs = inputs, keywords = ['apple']) == ['facebook', 'google'], 'fails'
    assert sol.parse(inputs = inputs, keywords = ['facebook', 'google']) == ['apple', 'intuit', 'tesla'], 'fails'

if __name__ == '__main__':
   main()