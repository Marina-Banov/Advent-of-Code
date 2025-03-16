#include <bits/stdc++.h>
#include <fstream>

using namespace std;

long long getScore(int nPlayers, int lastMarble) {
    list<long long> marbles;
    long long val = 0, turn = 0;
    marbles.push_front(val);
    list<long long>::iterator it = marbles.begin();
    vector<long long> points(nPlayers);
    for (int i = 0; i < lastMarble; ++i) {
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
        turn = (turn + 1) % nPlayers;
    }
    return *max_element(points.begin(), points.end());;
}

long long partOne(int nPlayers, int lastMarble) {
    return getScore(nPlayers, lastMarble);
}

long long partTwo(int nPlayers, int lastMarble) {
    return getScore(nPlayers, lastMarble * 100);
}

int main() {
    ifstream file("input");
    int nPlayers = 0, lastMarble = 0;
    string s;
    file >> nPlayers >> s >> s >> s >> s >> s >> lastMarble >> s;
    
    cout << partOne(nPlayers, lastMarble) << endl;
    cout << partTwo(nPlayers, lastMarble) << endl;
    return 0;
}
