#include <bits/stdc++.h>

using namespace std;

typedef struct {
    string adjacent;
    char result;
} rule;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string state;
    cin >> state >> state >> state;
    string padding = "........................................................................................................................................................................................................";
    int offset = padding.length();
    state = padding + state + padding;
    
    vector<rule> rules;
    rule r;
    char c;
    while (cin >> r.adjacent >> c >> c >> r.result) {
        rules.push_back(r);
    }

    int i, result;
    int prev = 0;
    int diff = 0;

    for (i = 0; i < 200; ++i) {
        string new_state = "";

        for (unsigned int j = 0; j < state.length(); ++j) {
            string cmp_string = ".....";
            for (unsigned int i = 0; i < 5; ++i) {
                if (j-2+i >= 0 && j-2+i < state.length()-1) {
                    cmp_string[i] = state[j-2+i];
                }
            }
            for (unsigned int h = 0; h < rules.size(); ++h) {
                if (cmp_string == rules[h].adjacent) {
                    new_state += rules[h].result;
                    break;
                }
                if (h == rules.size()-1) {
                    new_state += '.';
                }
            }
        }
        state = new_state;

        result = 0;
        for (unsigned int j = 0; j < state.length(); ++j) {
            if (state[j] == '#') {
                result += j - offset;
            }
        }

        if (result-prev == diff) {
            break;
        }
        diff = result-prev;
        prev = result;
    }
    
    cout << result + (50000000000 - i-1) * diff;
    return 0;
}
