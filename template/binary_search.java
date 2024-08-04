// https://inky-hovercraft-849.notion.site/Binary-Search-45031b3e5bce497ca4f0913af31d70c3#4256b911d1ba4eae8e432cd3c439add4
// exact match
import java.util.Arrays;

public final class BasicSolution {

  private BasicSolution() {
  }

  public static int equalTo(final int[] nums, final int target) {
    if (nums == null) {
      throw new NullPointerException();
    }
    if (nums.length == 0) {
      throw new IllegalArgumentException("The length of nums cannot be zero.");
    }
    int left = 0, right = nums.length - 1; // left and right always inclusive
    while (left <= right) {
      final int mid = (right - left) / 2 + left;
      if (nums[mid] == target) {
        return mid; // return index here
      } else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    throw new IllegalStateException("Cannot find the target value = " + target + " in array = " + Arrays.toString(nums));
  }
}

// first occurence

public static int firstOccurrence(final int[] nums, final int target) {
  int left = 0, right = nums.length - 1;
  while (left < right) {
    final int mid = left + (right - left) / 2;
    if (nums[mid] >= target) { // condition line
      right = mid; // move line
    } else {
      left = mid + 1; // move line
    }
  }
	// 当我们出来到这里的时候，我们并不知道left指的值是否是满足条件
  if (nums[left] >= target) return left; // condition line
  return -1;
}

// last occurence
private static int lastOccurrence(final int[] nums, final int target) {
  int left = 0, right = nums.length - 1;
  while (left < right) {
    final int mid = left + (1 + right - left) / 2;
    if (nums[mid] <= target) { // condition line
      left = mid; // move line
    } else {
      right = mid - 1; // move line
    }
  }
	// 当我们出来到这里的时候，我们并不知道left指的值是否是满足条件
  if (nums[left] <= target) return left; // condition line
  return -1;
}