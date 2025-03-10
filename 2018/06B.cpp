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

    int result = 0;

    for (int i = 0; i <= maxy; ++i) {
        for (int j = 0; j <= maxx; ++j) {
            int manhattan = 0;
            for (pair<int, int> c : coords) {
                manhattan += abs(c.first-i) + abs(c.second-j);
            }
            if (manhattan < 10000) {
                result++;
            }
        }
    }

    cout << result;
    return 0;
}
