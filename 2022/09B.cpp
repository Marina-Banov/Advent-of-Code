#include <bits/stdc++.h>

using namespace std;
namespace {
    pair<int,int> operator-(const pair<int,int> &a, const pair<int,int> &b) {
        return make_pair(a.first - b.first, a.second - b.second);
    }
}


bool should_move(pair<int,int> head, pair<int,int> tail) {
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (head.first + i == tail.first && head.second + j == tail.second) {
                return false;
            }
        }
    }
    return true;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    char c;
    int step;
    int i = 0, j = 0;
    vector<pair<int,int>> rope(10, make_pair(i,j));
    set<pair<int,int>> tail_pos;
    tail_pos.insert(rope[rope.size()-1]);

    while (cin >> c >> step) {
        int increment = (c == 'R' || c == 'D') ? 1 : -1;
        int* dimension = (c == 'L' || c == 'R') ? &j : &i;

        for (int k = 0; k < step; k++) {
            *dimension += increment;
            rope[0] = make_pair(i,j);
            for (unsigned int knot = 0; knot < rope.size()-1; knot++) {
                if (!should_move(rope[knot], rope[knot+1])) {
                    break;
                }
                auto diff = rope[knot] - rope[knot+1];
                if (diff.first) {
                    rope[knot+1].first += (diff.first > 0) ? 1 : -1;
                }
                if (diff.second) {
                    rope[knot+1].second += (diff.second > 0) ? 1 : -1;
                }
                if (knot == rope.size()-2) {
                    tail_pos.insert(rope[knot+1]);
                }
            }
        }
    }

    cout << tail_pos.size();
    return 0;
}
