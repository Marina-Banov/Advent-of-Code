#include <bits/stdc++.h>
#include <fstream>

using namespace std;

typedef struct {
    string adjacent;
    char result;
} Rule;

long simulate(string s, vector<Rule>& rules, long n) {
    int result = 0, prev = 0, diff = 0, i = 0;
    long nIter = n;
    if (nIter > 200) {
        nIter = 200;
    }
    string padding = "";
    for (int i = 0; i < nIter; i++) {
        padding += ".";
    }
    string state = padding + s + padding;
    int offset = padding.length();
    for (i = 0; i < nIter; ++i) {
        string newState = "";
        for (unsigned int j = 0; j < state.length(); ++j) {
            string cmpString = ".....";
            for (unsigned int i = 0; i < 5; ++i) {
                if (j-2+i >= 0 && j-2+i < state.length()-1) {
                    cmpString[i] = state[j-2+i];
                }
            }
            for (unsigned int h = 0; h < rules.size(); ++h) {
                if (cmpString == rules[h].adjacent) {
                    newState += rules[h].result;
                    break;
                }
                if (h == rules.size()-1) {
                    newState += '.';
                }
            }
        }
        state = newState;
        result = 0;
        for (unsigned int j = 0; j < state.length(); ++j) {
            if (state[j] == '#') {
                result += j - offset;
            }
        }
        if (result - prev == diff) {
            break;
        }
        diff = result - prev;
        prev = result;
    }
    if (nIter != n) {
        return result + (n - i - 1) * diff;
    }
    return result;
}

long partOne(string state, vector<Rule>& rules) {
    return simulate(state, rules, 20);
}

long partTwo(string state, vector<Rule>& rules) {
    return simulate(state, rules, 50000000000);
}

int main() {
    ifstream file("input");
    string state;
    file >> state >> state >> state;
    vector<Rule> rules;
    Rule r;
    char c;
    while (file >> r.adjacent >> c >> c >> r.result) {
        rules.push_back(r);
    }

    cout << partOne(state, rules) << endl;
    cout << partTwo(state, rules) << endl;
    return 0;
}
