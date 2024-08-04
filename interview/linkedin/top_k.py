"""
https://levelup.gitconnected.com/system-design-interview-distributed-top-k-frequent-elements-in-stream-2e92d63d777e

distribution := map<element, int>{}
for element in elements { distribution[element] += 1}

minHeap := NewMinHeap()
for element, frequency in distribution {
  // O(logk) complexity to rearrange the min-heap by frequency
  minHeap.insertAndRearrange({element, frequency}
  if minHeap.size() > k { minHeap.popMin() }
}

"""