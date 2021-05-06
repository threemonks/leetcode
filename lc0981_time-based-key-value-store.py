"""
981. Time Based Key-Value Store
Medium

1228

143

Add to List

Share
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]


Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""
from collections import defaultdict

"""
Design+Binary Search

Basic key value stores in dictionary. For each key, store {timestamp, value} as sorted list of tuples since timestamp set is always increasing.
when we get a certain timestamp, we do binary search to return value on that timestamp if exists, else return immediate left one

"""
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # print('get key=%s timestamp=%s' % (key, timestamp))
        if key not in self.data:
            return ""
        vals = self.data[key]
        # if before first timestamp return "", or after last one, return last one
        if vals[-1][0] <= timestamp:
            return vals[-1][1]
        elif timestamp < vals[0][0]:
            return ""
        # print(vals)
        lo, hi = 0, len(vals)
        while lo < hi:
            mid = (lo + hi) // 2
            # print('lo=%s hi=%s mid=%s' % (lo, hi, mid))
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] < timestamp: # we increase lo to mid+1 when target found, so after exit while, lo is larger than matching value
                lo = mid + 1
            else:
                hi = mid
        # if not found, return next on left of lo, or "" if nothing on left
        return vals[lo-1][1] if lo-1>=0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

def main():

    obj = TimeMap()
    obj.set("foo", "bar", 1)
    assert obj.get("foo", 1) == "bar", 'fails'
    assert obj.get("foo", 3) == "bar", 'fails'
    obj.set("foo", "bar2", 4)
    assert obj.get("foo", 4) == "bar2", 'fails'
    assert obj.get("foo", 5) == "bar2", 'fails'


if __name__ == '__main__':
   main()