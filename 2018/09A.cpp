#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n_players = 0, last_marble = 0;
    string s;
    cin >> n_players >> s >> s >> s >> s >> s >> last_marble >> s;

    list<int> marbles;
    int val = 0, turn = 0;
    marbles.push_front(val);
    list<int>::iterator it = marbles.begin();
    vector<int> points(n_players);

    for (int i = 0; i < last_marble; ++i) {
        val++;
        if (val % 23) {
            ++it;
            if (it == marbles.end()) {
                it = marbles.begin();
            }
            ++it;
            it = marbles.insert(it, val);
        } else {
            points[turn] += val;
            for (int j = 0; j < 7; ++j) {
                if (it == marbles.begin()) {
                    it = marbles.end();
                }
                --it;
            }
            points[turn] += *it;
            it = marbles.erase(it);
        }

        turn++;
        if (turn == n_players) {
            turn = 0;
        }
    }

    int max_points = 0;
    for (int i = 0; i < n_players; ++i) {
        if (points[i] > max_points) {
            max_points = points[i];
        }
    }

    cout << max_points;
    return 0;
}
