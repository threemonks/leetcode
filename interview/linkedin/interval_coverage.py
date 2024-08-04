
"""
public interface Intervals {

    /**
     * Adds an interval [from, to) into an internal structure.
     */
    void addInterval(int from, int to);

    /**
     * Returns a total length covered by the added intervals.
     * If several intervals intersect, the intersection should be counted only once.
     * Example:
     *
     * addInterval(3, 6)
     * addInterval(8, 9)
     * addInterval(1, 5)
     *
     * getTotalCoveredLength() -> 6
     *
     * i.e. [1,5) and [3,6) intersect and give a total covered interval [1,6) with a length of 5.
     *      [1,6) and [8,9) don't intersect, so the total covered length is a sum of both intervals, that is 5+1=6.
     *
     *          |__|__|__|                  (3,6)
     *                         |__|         (8,9)
     *    |__|__|__|__|                     (1,5)
     *
     * 0  1  2  3  4  5  6  7  8  9  10
     *
     */
    int getTotalCoveredLength();

}

time O(NlogN)
 get O(N)
"""


class Intervals:
    def __init__(self):
        self.intervals = []  # sorted, no overlap

    def addInterval0(self, a, b):
        if not self.intervals:
            self.intervals.append([a, b])
        else:
            new_intervals = self.intervals + [[a, b]]
            sorted_intervals = []
            for interval in sorted(new_intervals):
                if interval[0] <= sorted_intervals[-1][1]:
                    sorted_intervals[-1][1] = max(sorted_intervals[-1][1], interval[1])
                else:
                    sorted_intervals.append(interval)

            self.intervals = sorted_intervals[:]

    def addInterval(self, a, b):
        if not self.intervals:
            self.intervals.append([a, b])
        else:
            added = False
            new_intervals = []
            if not self.intervals or a < self.intervals[0][0]:
                new_intervals.append([a, b])
                added = True
            n = len(self.intervals)
            for i in range(n):
                interval = self.intervals[i]
                # append or merge interval
                if new_intervals and interval[0] <= new_intervals[-1][1]:
                    # merge
                    new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])
                else:
                    new_intervals.append(interval)

                if self.intervals[i][0] <= a and (i+1 >= n or a < self.intervals[i+1][0]):
                    # insert a after i-th interval
                    if not added:
                        # append or merge a, b
                        if new_intervals and a <= new_intervals[-1][1]:
                            # merge
                            new_intervals[-1][1] = max(new_intervals[-1][1], b)
                        else:
                            new_intervals.append([a, b])
                        added = True

            self.intervals = new_intervals[:]
        print('adding a=%s b=%s self.intervals=%s' % (a, b, self.intervals))

    def getTotalCoveredLength(self):
        print('intervals=%s' % self.intervals)
        ans = 0
        for interval in self.intervals:
            ans += interval[1] - interval[0]

        return ans

if __name__ == '__main__':
    sol = Intervals()
    sol.addInterval(3, 6)
    sol.addInterval(8, 9)
    sol.addInterval(1, 5)
    assert sol.getTotalCoveredLength() == 6