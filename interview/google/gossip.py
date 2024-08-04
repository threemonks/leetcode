"""
 Gossip那题用dijkstra做法感觉是最优解了，就是将 dist 数组换成 time 数组。queue 中放从 A 出发到当前可达的人，time 数组中保存消息到对应人的最小时间。因为有时间顺序，所以用heap，每个记录最早时间，碰到更早的就更新，heap保证了时间排序

#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <utility>
#include <unordered_map>

using namespace std;

using Person = pair<int, int>;
using Pass = tuple<int, int, int>;

vector<int> message_pass(vector<Pass> passes, int n) {
	// construct graph
	vector<vector<Person>> adjs(n);
	for (auto[src, dst, time] : passes) {
		adjs[src].push_back(make_pair(dst, time));
		adjs[dst].push_back(make_pair(src, time));
	}

	auto cmp = [](const Person& p1, const Person& p2) {return p1.second > p2.second;};
	priority_queue<Person, vector<Person>, decltype(cmp)> q(cmp);
	vector<int> first_known(n, INT_MAX);

	q.push(make_pair(0, 0));
	first_known[0] = 0;
	while (!q.empty()) {
		auto [p, t] = q.top();
		q.pop();

		// already known
		if (t > first_known[p]) continue;

		for (auto [next, time]: adjs[p]) {
			// could not pass message before known
			if (time < first_known[p]) continue;

			// update next person first known
			if (time < first_known[next]) {
				first_known[next] = time;
				q.push(make_pair(next, time));
			}
		}
	}

	return first_known;
}

int main() {
	// case 1
	int n1 = 4;
	vector<Pass> passes1{{0, 1, 10}, {1, 2, 20}, {2, 3, 5}};
	auto knows1 = message_pass(passes1, n1);
	for (int i = 0; i < n1; ++i) {
		cout << i << ":" << knows1[i] << endl;
	}

	// case 2
	int n2 = 4;
	vector<Pass> passes2{{0, 1, 50},  {0, 2, 100}, {1, 2, 60}, {1, 3, 70}, {2, 3, 65}};
	auto knows2 = message_pass(passes2, n2);
	for (int i = 0; i < n2; ++i) {
		cout << i << ":" << knows2[i] << endl;
	}
	return 0;
}

"""
def main(L):
    L.sort(key = lambda e: e[2])

    know = set()
    know.add('A')

    i = 0
    while i < len(L):

        # get meetings for next time T
        u, v, t = L[i]
        edges = [(u, v)]
        nodes = set([u, v])

        # merge circles within same timestamp
        i += 1
        while i < len(L) and L[i][2] == t:
            u, v, _ = L[i]
            edges.append((u, v))
            nodes.add(u)
            nodes.add(v)
            i += 1

        # build graph
        G = {}
        for u in nodes:
            G[u] = set()

        for u, v in edges:
            G[u].add(v)
            G[v].add(u)

        # BFS
        visited = {u: False for u in nodes}
        q = list(nodes & know)
        for u in q:
            visited[u] = True

        while q:
            u = q.pop(0)  # use deque can optimize this to O(1)
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        # update know
        for u, val in visited.items():
            if val:
                know.add(u)

    return list(know)


if __name__ == "__main__":
    L = [
        ['A', 'B', 10],
        ['B', 'C', 20],
        ['C', 'D', 5]
    ]

    ans = main(L)
    print(ans)