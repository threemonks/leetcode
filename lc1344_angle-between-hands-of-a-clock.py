"""
1344. Angle Between Hands of a Clock
Medium

596

135

Add to List

Share
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.



Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0


Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.

"""
"""
Math

calculate angle for one minute on minute handle
calculate angle for one minute on hour handle
minute_angle = minutes  * one_minute_angle
hour_angle = (hour+minutes/60)*one_hour_angle

return min(abs(minute_angle - hour_angle), 360 -  abs(minute_angle - hour_angle))

mistakes:
1. return smaller angle if > 180
2. hour %= 12 (hour==12=>hour = 0)

time O(1)
"""
import math


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_minute_angle = 360 / 60  # 6
        one_hour_angle = 360 / 12  # 30

        minute_angle = minutes * one_minute_angle
        hour_angle = (hour % 12 + minutes / 60.0) * one_hour_angle

        ans = abs(hour_angle - minute_angle)

        return min(ans, 360 - ans)  # smaller angle

def main():
    sol = Solution()
    assert sol.angleClock(hour = 12, minutes = 30) == 165, 'fails'

    assert sol.angleClock(hour = 3, minutes = 30) == 75, 'fails'

    assert sol.angleClock(hour = 3, minutes = 15) == 7.5, 'fails'

    assert sol.angleClock(hour = 4, minutes = 50) == 155, 'fails'

    assert sol.angleClock(hour = 12, minutes = 0) == 0, 'fails'

if __name__ == '__main__':
   main()