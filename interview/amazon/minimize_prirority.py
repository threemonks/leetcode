"""
https://leetcode.com/discuss/interview-experience/1316685/amazon-oa-sde1-new-questions

The second question was more interesting. You are given a List of Integers which is a list of priorities. A priority can be a number from 1-99. Without changing the order of the array, minimize the priority as much as possible without changing the order.

Example

arr = [1, 4, 8, 4]

->

[1, 2, 3, 2]
I got 13/14 test cases for question 1, and 14/14 for question 2.

Question 2 I did by putting the array into a TreeSet which contains the priority numbers as keys in sorted order. Then I made a HashMap that iterated on the TreeSet, and mapped the old priority to the new priority starting as priority = 1 for the first since we know the minimum number has to be 1. Then it was a matter of going through the array again, and setting the new priority numbers from the HashMap. Ez NLogN solution.

Update: moving onto interviews

Answers


static List<Integer> minPriority(List<Integer> arr) {
      int n = arr.size();
      TreeSet<Integer> ts = new TreeSet<>();
      for (int val : arr) {
         ts.add(val);
      }
      Map<Integer, Integer> mp = new HashMap<>();
      int priority = 1;
      for(int v : ts){
         mp.put(v,priority);
         priority++;
      }
      for(int i=0;i<n;i++){
	     arr.set(i, mp.get(arr.get(i)));
      }

      return arr;
   }

"""

def main():
    pass

if __name__ == '__main__':
    main()
