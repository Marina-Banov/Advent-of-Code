#include <bits/stdc++.h>

using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<pair<int, int>> coords;
    pair<int, int> coord;
    char c;
    int maxx = 0, maxy = 0;
    while (cin >> coord.first >> c >> coord.second) {
        coords.push_back(coord);
        maxy = max(maxy, coord.first);
        maxx = max(maxx, coord.second);
    }

    vector<int> counts(coords.size(), 0);

    for (int i = 0; i <= maxy; ++i) {
        for (int j = 0; j <= maxx; ++j) {
            vector<int> manhattan;
            for (pair<int, int> c : coords) {
                manhattan.push_back(abs(c.first-i) + abs(c.second-j));
            }

            int min_manhattan = *min_element(manhattan.begin(), manhattan.end());
            vector<int> indices;
            for (unsigned int k = 0; k < manhattan.size(); ++k) {
                if (manhattan[k] == min_manhattan) {
                    indices.push_back(k);
                }
            }

            if (indices.size() == 1 && counts[indices[0]] != -1) {
                if (i == 0 || j == 0 || i == maxy || j == maxx) {
                    counts[indices[0]] = -1;
                } else {
                    counts[indices[0]]++;
                }
            }
        }
    }

    cout << *max_element(counts.begin(), counts.end());
    return 0;
}
