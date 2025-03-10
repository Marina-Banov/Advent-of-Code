#include <bits/stdc++.h>

using namespace std;

#define MAX_SIZE 100


int get_array_index(pair<int,int> x, int n_cols) {
    return x.first * n_cols + x.second;
}

pair<int, int> get_matrix_indices(int x, int n_cols) {
    return make_pair(x / n_cols, x % n_cols);
}

typedef struct {
	int weight;
	int array_index;
} Vertex;


vector<Vertex> get_adjacent(
    char area[MAX_SIZE][MAX_SIZE],
    int n_rows, int n_cols,
    pair<int,int> x
) {
    vector<pair<int,int>> candidates = {
        make_pair(x.first-1, x.second),
        make_pair(x.first+1, x.second),
        make_pair(x.first, x.second-1),
        make_pair(x.first, x.second+1)
    };
    vector<Vertex> adjacent;

    for (auto c : candidates) {
        if (
            c.first >= n_rows || c.first < 0 ||
            c.second >= n_cols || c.second < 0 ||
            area[c.first][c.second] - area[x.first][x.second] > 1
        ) {
            continue;
        }
        // weight from adjacent fields is always 1
        adjacent.push_back({ 1, get_array_index(c, n_cols) });
    }
    return adjacent;
}


int dijkstra(char area[MAX_SIZE][MAX_SIZE], int n_rows, int n_cols, int start, int end) {
	auto cmp = [](Vertex v1, Vertex v2) { return v1.weight > v2.weight; };
    priority_queue<
        Vertex,
        vector<Vertex>,
        decltype(cmp)
    > pq(cmp);
    pq.push({ 0, start });
    vector<int> weights(n_rows*n_cols, 999);
    weights[start] = 0;
    auto s = pq.top();

    while (!pq.empty() && s.array_index != end) {
        s = pq.top();
        pq.pop();
 
        auto adjacent = get_adjacent(
        	area, n_rows, n_cols,
        	get_matrix_indices(s.array_index, n_cols)
        );
        for (auto adj : adjacent) {
            if (weights[adj.array_index] > weights[s.array_index] + adj.weight) {
                weights[adj.array_index] = weights[s.array_index] + adj.weight;
                pq.push({ weights[adj.array_index], adj.array_index });
            }
        }
    }
    return s.weight;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string line;
    char area[MAX_SIZE][MAX_SIZE];
    int n_rows = 0, n_cols = 0;
    pair<int,int> start, end;

    while (!cin.eof()) {
        cin >> line;
        n_cols = line.length();
        for (int j = 0; j < n_cols; j++) {
            if (line[j] == 'S') {
                start = make_pair(n_rows, j);
                area[n_rows][j] = 'a';
            } else if (line[j] == 'E') {
                end = make_pair(n_rows, j);
                area[n_rows][j] = 'z';
            } else {
                area[n_rows][j] = line[j];
            }
        }
        n_rows++;
    }

    cout << dijkstra(
        area, n_rows, n_cols,
        get_array_index(start, n_cols),
        get_array_index(end, n_cols)
    );
    return 0;
}
