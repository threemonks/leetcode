"""
public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
//impliment here
}
/* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
* retrieves it from the data source. If the cache is full, attempt to cache the returned data,
* evicting the T with lowest rank among the ones that it has available
* If there is a tie, the cache may choose any T with lowest rank to evict.
*/
public T get(K key) {
//impliment here
}
/*
* For reference, here are the Rankable and DataSource interfaces.
* You do not need to implement them, an‍‌‍‌‌‌‌‌‍‌‍‌‍‌‌‌‌‌‌‍d should not make assumptions
* about their implementations.
*/
public interface Rankable {
/**
* Returns the Rank of this object, using some algorithm and potentially
* the internal state of the Rankable.
*/
long getRank();
}
public interface DataSource<K, T extends Rankable> {
T get(K key);
}

"""

"""
import java.ut ...[/quote]
 
[hide=200]没必要用TreeMap吧，感觉PriorityQueue应该就够了吧？[mw_shl_code=java,true]public class RetainBestCache<K, T extends Rankable> {
    int entriesToRetain;
    HashMap<K, T> map = new HashMap<K,T>();
    PriorityQueue<Wrapper<K, T>> pq;
    DataSource<K,T> ds;
  
    /* Constructor with a data source (assumed to be slow) and a cache size */
    public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
        //impliment here
        this.pq = new PriorityQueue<>(new Comparator<Wrapper>() {
            public int compare(Wrapper w1, Wrapper w2) {
                return w1.data.getRank() - w2.data.getRank();
            }
        });
        this.ds = ds;
        this.entriesToRetain = entriesToRetain;
    }
    /* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
    * retrieves it from the data source. If the cache is full, attempt to cache the returned data,
    * evicting the T with lowest rank among the ones that it has available
    * If there is a tie, the cache may choose any T with lowest rank to evict.
    */
    public T get(K key) {
        //impliment here
        if (map.containsKey(key)) {
            return map.get(key);
        }
        T data = DataSource.get(key);
        if (map.size() < entriesToRetain) {
            map.put(key, data);
            pq.offer(new Wrapper(key, data));
        } else {
            evict();
            map.put(key, data);
            pq.offer(new Wrapper(key, data));
        }
        return data;
    }
 
    private evict() {
        Wrapper leastRank = pq.poll();
        map.remove(leastRank.key);
    }
}
 
class Wrapper<K, T> {
    T data;
    K key;
 
    public Wrapper(T data, K key) {
        this.data = data;
        this.key = key;
    }
}
 
/*
* For reference, here are the Rankable and DataSource interfaces.
* You do not need to implement them, and should not make assumptions
* about their implementations.
*/
public interface Rankable {
    /**
    * Returns the Rank of this object, using some algorithm and potentially
    * the internal state of the Rankable.
    */
    long getRank();
}
 
public interface DataSource<K, T extends Rankable> {
    T get(K key);
}
"""

"""
public class RetainBestCache<K, T extends Rankable> {
 
     private Map<K, T> cache;. 鍥磋鎴戜滑@1point 3 acres
     private Map<Long, Set<K>> rankingOfObject;.鏈枃鍘熷垱鑷�1point3acres璁哄潧
     private DataSource<K, T> dataSource;
     private int maxSizeOfCache;
 
    /* Constructor with a data source (assumed to be slow) and a cache size */
    public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {. From 1point 3acres bbs
        // Implementation here
        cache = new HashMap<>();
        rankingOfObject = new TreeMap<>();
        dataSource = ds;
        maxSizeOfCache = entriesToRetain;
    }
 
    /* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
     * retrieves it from the data source. If the cache is full, attempt to cache the returned data,
     * evicting the T with lowest rank among the ones that it has available
     * If there is a tie, the cache may choose any T with lowest rank to evict.
     */
    public T get(K key) {
        // Implementation here
        if(cache.containsKey(key)) {
          return cache.get(key);
        }
        return fetchDataFromDs(key);
    }
. visit 1point3acres.com for more.
    private T fetchDataFromDs(K key) {
       if(cache.size() >= maxSizeOfCache) {
          evictElement();
        }
        T object = dataSource.get(key);
        cache.put(key, object);
        long rankOfObject = object.getRank();
        if(!rankingOfObject.containsKey(rankOfObject)) {. 鐗涗汉浜戦泦,涓€浜╀笁鍒嗗湴
          rankingOfObject.put(rankOfObject, new HashSet<>());
        }
        rankingOfObject.get(rankOfObject).add(key);
        return object;
    }
 
    private void evictElement() {
      Entry<Long, Set<K>> entry = rankingOfObject.topEntry();
      K key = entry.getValue().getIterator().next();
      entry.getValue().remove(key);
      cache.remove(key)
      if(entry.getValue().size() == 0) {
        rankingOfObject.remove(entry.getKey());
      }.鏈枃鍘熷垱鑷�1point3acres璁哄潧
    }
 
 
}
. visit 1point3acres.com for more.
// What if rank is defined as number of reads of element in cache?
// LRU. from: 1point3acres.com/bbs
// Let's assume that rank can change dynamicly. It is not immutable, but it is not LRU. We do not know how it is changed
 
 
/*
* For reference, here are the Rankable and DataSource interfaces.
* You do not need to implement them, and should not make assumptions
* about their implementations.
*/
 
public interface Rankable {. from: 1point3acres.com/bbs
    /**.鐣欏璁哄潧-涓€浜�-涓夊垎鍦�
     * Returns the Rank of this object, using some algorithm and potentially
     * the internal state of the Rankable.
     */
    long getRank();
}
 
public interface DataSource<K, T extends Rankable> {
    T get (K key);
}. W

"""

"""
https://github.com/shileiwill/destination/blob/master/Round1/src/company/linkedin/RetainBestCache.java

package company.linkedin;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.TreeMap;
//Important
public class RetainBestCache<K, V> {

	public static void main(String[] args) {

	}

	private Map<K, V> cache; 
	private TreeMap<Integer, Set<K>> rank; // Since it is ordered by Rank, an integer, TreeMap is super important
	private DataSource<K, V> dataSource; 
	private int capacity; 

	/* Constructor with a data source (assumed to be slow) and a cache size */ 
	public RetainBestCache(DataSource<K, V> ds, int capacity) {
		this.dataSource = ds;
		this.capacity = capacity;
		this.cache = new HashMap<K, V>();
		this.rank = new TreeMap<Integer, Set<K>>();
	}
	
	/* Gets some data. 
	 * If possible, retrieves it from cache to be fast. If the data is not cached, 
	 * retrieves it from the data source. If the cache is full, attempt to cache the returned data, 
	 * evicting the T with lowest rank among the ones that it has available 
	 * If there is a tie, the cache may choose any T with lowest rank to evict. 
	 * */ 
	public V get(K key) {
		V res = null;
		if (cache.containsKey(key)) {
			res = cache.get(key);
		} else {
			res = dataSource.get(key);
			int curRank = dataSource.getRank(key);
			// Add to cache
			cache.put(key, res);
			if (!rank.containsKey(curRank)) {
				rank.put(curRank, new HashSet<K>());
			}
			rank.get(curRank).add(key);
			
			if (cache.size() > capacity) {
				removeLowestRank();
			}
		}
		
		return res;
	}

	private void removeLowestRank() {
		Entry<Integer, Set<K>> firstEntry = rank.firstEntry();
		int firstKey = firstEntry.getKey();
		Set<K> firstSet = firstEntry.getValue();
		
		K toRemove = firstSet.iterator().next();
		
		// Remove from rank TreeMap
		firstSet.remove(toRemove);
		if (firstSet.isEmpty()) {
			rank.remove(firstKey);
		}
		
		// Remove from Cache Map
		cache.remove(toRemove);
	} 
}

class DataSource<K, V> {
	V get(K key) {
		return (V)new Object();
	}
	
	int getRank(K key) {
		return 1;
	}
}

"""