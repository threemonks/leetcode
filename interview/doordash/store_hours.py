"""
/*
Problem Statement
To find all the stores that are open in a user’s delivery radius, we need to check the store’s operating hours. We currently store this information in Elasticsearch but the query performance for our use-case is turning out to be not very efficient. The format that we store it in Elasticsearch is something like this:
{
  "store": {
    "store_name": "Tasty Pizzas",
    "store_id": "123345",
    "operating_hours": [
      {
        "day": "mon",
        "hours.open": "10:00 am",
        "hours.close": "2:00 pm"
      },
      {
        "day": "tue",
        "hours.open": "10:00 am",
        "hours.close": "2:00 pm"
      },
      {
        "day": "wed",
        "hours.open": "10:00 am",
        "hours.close": "2:00 pm"
      },
      {
        "day": "thu",
        "hours.open": "10:00 am",
        "hours.close": "2:00 pm"
      },
      {
        "day": "fri",
        "hours.open": "10:00 am",
        "hours.close": "2:00 pm"
      },
      {
        "day": "sat",
        "hours.open": "10:00 am",
        "hours.close": "2:00 pm"
      }
    ]
  }
}
We want to experiment to improve the performance of fetching open stores by converting the operating hours into encoded tokens which would be of fixed length of 5. The first digit would represent the day, the next 4 digits would represent the hours in 24 hours format.
Monday maps to number 1, Tuesday to number 2 and so on.
Ex: Monday, 10:00am transforms to 11000 Ex: Monday, 2:00pm transforms to 11400 (as 2pm -> 14:00 in 24 hr format)
Write a function that takes in a start_time and end_time and gives back a list of encoded tokens. Ensure you validate the input Note: We round up the time to next 5 mins
Ex: Input: ("mon 10:00 am", "mon 11:00 am")
Output: ["11000", "11005", "11010", "11015", "11020", "11025", "11030", "11035", "11040", "11045", "11050", "11055", "11100"]
Input: ("mon 10:15 am", "mon 11:00 am") Output: ["11015", "11020", "11025", "11030", "11035", "11040", "11045", "11050", "11055", "11100"]

q: could start/end be on different weekday?
"""

from typing import List

class Solution:
    def store_hours(self, openings: List[int]) -> None:
        weekday_maps = {
            "mon": 1,
            "tue": 2,
            "wed": 3,
            "thu": 4,
            "fri": 5,
        }

        ans = []

        start, end = openings
        start_weekday, start_time, morning = start.split()
        start_time = int(start_time.replace(":", ""))
        if morning.lower() == "pm":
            start_time = start_time + 1200

        end_weekday, end_time, morning = end.split()
        end_time = int(end_time.replace(":", ""))
        if morning.lower() == "pm":
            end_time = end_time + 1200

        assert start_weekday == end_weekday, 'oepnings start and end in different days'
        for i in range(start_time, end_time+1, 5):
            if i % 100 >= 60: # skip invalid minute
                continue
            ans.append(str(weekday_maps[start_weekday]) + str(i))

        print(f"{ans = }")
        return ans

def main():
    sol = Solution()
    assert sol.store_hours(["mon 10:00 am", "mon 11:00 am"]) == ["11000", "11005", "11010", "11015", "11020", "11025", "11030", "11035", "11040", "11045", "11050", "11055", "11100"], 'fails'
    assert sol.store_hours(["mon 10:15 am", "mon 11:00 am"]) == ["11015", "11020", "11025", "11030", "11035", "11040", "11045", "11050", "11055", "11100"], 'fails'

if __name__ == "__main__":
    main()