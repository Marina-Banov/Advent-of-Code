#include <bits/stdc++.h>

using namespace std;

#define MAX_ROWS 4000000


int manhattan(pair<int,int> a, pair<int,int> b) {
    return abs(a.second-b.second) + abs(a.first-b.first);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<pair<int,int>> sensors;
    vector<int> manhattans;
    pair<int,int> s, b;
    char format[] = "Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d ";
    while (scanf(format, &s.second, &s.first, &b.second, &b.first) == 4) {
        sensors.push_back(s);
        manhattans.push_back(manhattan(s, b));
    }

    for (int row = 0; row < MAX_ROWS; row++) {
        vector<pair<int,int>> ranges;
        for (unsigned int i = 0; i < sensors.size(); i++) {
            auto ss = sensors[i];
            int m = manhattans[i];
            if (ss.first - m > row || ss.first + m < row) {
                continue;
            }
            int range = m - abs(ss.first - row);
            ranges.push_back(make_pair(ss.second-range, ss.second+range));
        }
        sort(ranges.begin(), ranges.end());

        for (auto i = ranges.begin()+1; i != ranges.end(); i++) {
            auto a = *i;
            auto b = *(i-1);
            if (a.first >= b.first && a.second <= b.second) {
                ranges.erase(i);
                i--;
            } else if (a.first > b.second) {
                long long res = (a.first + b.second) / 2;
                cout << res * 4000000 + row;
                return 0;
            }
        }
    }

    cout << -1;
    return 0;
}
