"""
1146. Snapshot Array
Medium

834

160

Add to List

Share
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""
import bisect

"""
Design Array

nums stores {index: [(snap_id, val)]}
for lookup, do binary search for snap_id in array nums[index], the right most idx where snap_id<= target snap_id has the value we are looking for

"""
class SnapshotArray:

    def __init__(self, length: int):
        self.nums = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if index in self.nums:
            self.nums[index].append((self.snap_id, val))
        else:
            self.nums[index] = [(self.snap_id, val)]

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        # print('get index=%s snap_id=%s self.nums=%s' % (index, snap_id, self.nums))
        if index not in self.nums:
            return 0
        # search for last self.nums[index] index where snap_id <= target_snap_id
        # or search for left most index idx where nums[index][idx][0] >= snap_id+1, then return idx-1
        idx = bisect.bisect(self.nums[index], (snap_id + 1, 0)) - 1
        # print('idx=%s' % idx)
        if idx == -1: # no value at this snapshot
            return 0
        else:
            return self.nums[index][idx][1]

"""
Design Array

use dict nums to store index and value
set(index, val) will update index in dict nums with value val
take snapshot, store all values of nums into dict {snap_id: {idx: val}}
get(index, snap_id) => dct[snap_id].get(index, 0)
"""
class SnapshotArray1:

    def __init__(self, length: int):
        self.nums = {}
        self.snaps = dict()

    def set(self, index: int, val: int) -> None:
        self.nums[index] = val

    def snap(self) -> int:
        snap_id = len(self.snaps)
        self.snaps[snap_id] = self.nums.copy()
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id].get(index, 0)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

def main():
        obj = SnapshotArray(3)
        obj.set(0, 5)
        assert obj.snap() == 0, 'fails'
        obj.set(0, 6)
        assert obj.get(0, 0) == 5, 'fail'

if __name__ == '__main__':
   main()