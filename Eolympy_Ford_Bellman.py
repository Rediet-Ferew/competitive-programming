#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>

using namespace std;

int main() {
    unordered_map<int, vector<pair<int, int>>> graph;
    int n, e;
    cin >> n >> e;

    for (int i = 0; i < e; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
    }

    vector<int> visited(n + 1, numeric_limits<int>::max());
    visited[1] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
    minHeap.push({0, 1});

    while (!minHeap.empty()) {
        int weight = minHeap.top().first;
        int node = minHeap.top().second;
        minHeap.pop();

        if (visited[node] < weight) {
            continue;
        }

        for (auto neighbor : graph[node]) {
            int neigh = neighbor.first;
            int neigh_w = neighbor.second;
            int w = neigh_w + weight;

            if (w < visited[neigh]) {
                visited[neigh] = w;
                minHeap.push({w, neigh});
            }
        }
    }

    for (int idx = 1; idx <= n; idx++) {
        if (visited[idx] == numeric_limits<int>::max()) {
            visited[idx] = 30000;
        }
    }

    for (int idx = 1; idx <= n; idx++) {
        cout << visited[idx] << " ";
    }

    return 0;
}
