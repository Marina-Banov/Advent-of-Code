#include <bits/stdc++.h>
#include <fstream>

using namespace std;

pair<int, int> getMaxCoord(vector<pair<int, int>>& coords) {
    pair<int, int> result(0, 0);
    for (pair<int, int> c : coords) {
        result.first = max(result.first, c.first);
        result.second = max(result.second, c.second);
    }
    return result;
}

int partOne(vector<pair<int, int>>& coords) {
    pair<int, int> maxCoord = getMaxCoord(coords);
    vector<int> counts(coords.size(), 0);
    for (int i = 0; i <= maxCoord.first; ++i) {
        for (int j = 0; j <= maxCoord.second; ++j) {
            vector<int> manhattan;
            for (pair<int, int> c : coords) {
                manhattan.push_back(abs(c.first-i) + abs(c.second-j));
            }
            int minManhattan = *min_element(manhattan.begin(), manhattan.end());
            vector<int> indices;
            for (unsigned int k = 0; k < manhattan.size(); ++k) {
                if (manhattan[k] == minManhattan) {
                    indices.push_back(k);
                }
            }
            if (indices.size() == 1 && counts[indices[0]] != -1) {
                if (i == 0 || j == 0 || i == maxCoord.first || j == maxCoord.second) {
                    counts[indices[0]] = -1;
                } else {
                    counts[indices[0]]++;
                }
            }
        }
    }
    return *max_element(counts.begin(), counts.end());
}

int partTwo(vector<pair<int, int>>& coords) {
    pair<int, int> maxCoord = getMaxCoord(coords);
    int result = 0;
    for (int i = 0; i <= maxCoord.first; ++i) {
        for (int j = 0; j <= maxCoord.second; ++j) {
            int manhattan = 0;
            for (pair<int, int> c : coords) {
                manhattan += abs(c.first-i) + abs(c.second-j);
            }
            if (manhattan < 10000) {
                result++;
            }
        }
    }
    return result;
}

int main() {
    ifstream file("input");
    vector<pair<int, int>> coords;
    pair<int, int> coord;
    char c;
    while (file >> coord.first >> c >> coord.second) {
        coords.push_back(coord);
    }

    cout << partOne(coords) << endl;
    cout << partTwo(coords) << endl;
    return 0;
}
