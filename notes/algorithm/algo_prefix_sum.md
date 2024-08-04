https://github.com/zea7ot/leetcode-problems-by-tags-zea7ot/blob/master/txt/by_algorithm/dynamic_programming/summary.txt

## Prefix Sums:

    * subarray (sum, max, longest, shortest with sum at least) usually invovles prefixsum or sliding window
    * 前缀和主要用于处理数组区间的问题

    about why `count += prefixSums.get(sum - k)` - the count increases of subarray with sum value k after visiting node j is counts[presum-k] (i.e., counts of subarray whose sum is k, and ends at j)
    https://leetcode.com/problems/subarray-sum-equals-k/discuss/535507/Explanation-to-why-map.get(sum-k)-is-done-than-count%2B%2B

    store previous sum and the times of this sum, because sum[i, j] = sum[0, j] - sum[0, i - 1], this is a very very important idea
    https://leetcode.com/problems/binary-subarrays-with-sum/discuss/187005/3-ways-to-solve-this-kind-of-problem.

    about initialization of map of presum counts: preSum.put(0, 1) / counts[0]=1
     https://leetcode.com/problems/subarray-sum-equals-k/discuss/102106/Java-Solution-PreSum-+-HashMap/416171
    https://leetcode.com/problems/subarray-sum-equals-k/discuss/102106/Java-Solution-PreSum-+-HashMap/238328

    with sum_k_array_counts[j] as number of subarray sum to k and ends at j, why sum_k_array_counts[j] - sum_k_array_counts[j-1] = sum_k_array_counts[presum[j]-k]? see this link:
    https://leetcode.com/problems/subarray-sum-equals-k/discuss/535507/Explanation-to-why-map.get(sum-k)-is-done-than-count%2B%2B

    Consider the below example:
    array :: 3 4 7 -2 2 1 4 2
    presum :: 3 7 14 12 14 15 19 21
    index :: 0 1 2 3 4 5 6 7
    k = 7
    Map should look like ::
    (0,1) , (3,1), (7,1), (14,2) , (12,1) , (15,1) , (19,1) , (21,1)

    Consider 21(presum) now what we do is sum-k that is 21-7 = 14 . Now we will check our map if we go by just count++ logic we will just increment the count once and here is where we go wrong.

    When we search for 14 in presum array we find it on 2 and 4 index. The logic here is that 14 + 7 = 21 so the array between indexes
    -> 3 to 7 (-2 2 1 4 2)
    -> 5 to 7 both have sum 7 ( 1 4 2)
    The sum is still 7 in this case because there are negative numbers that balance up for. So if we consider count++ we will have one count less as we will consider only array 5 to 7 but now we know that 14 sum occurred earlier too so even that needs to be added up so map.get(sum-k).

    Here is my way of understanding why count += map.get(sum-k):
    with sum(nums[0:7]) = 21
    counts_of_presum = number of subarray sum to value presum starting at index 0, within nums up to current index
    counts_of_presum[21-7]=counts_of_presum[14] <=> number of subarray sum to 14 starting at index 0, within nums[0:7)
                                                <=> number of subarray sum to 21-14=7 ending at index 6, within nums[0:7)
                                                <=> increase of number of subarray sum to 21-14=7 for nums[0:6], to the number of subarray sum to 7 for nums[0:7]
    so we have this
        for j from 5 to 6
            `res = res + counts_of_presum[presum-k]`

## prefixsum + hashmap (number of times a given prefix sum appears)
  prefix sum和哈希table联合起来一起使用会起到非常大的作用