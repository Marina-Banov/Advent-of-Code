#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    vector<char> polymer;
    char c;
    while (cin >> c) {
        polymer.push_back(c);
    }
    
    unsigned int min_size = 10000;
    for (char i = 'a'; i <= 'z'; ++i) {
        unsigned int k = 0;
        vector<char> v(polymer);
        for (unsigned int j = 0; j < v.size(); ++j) {
            if (v.at(j) == i || i - v.at(j) == 'a'-'A') {
                v.erase(v.begin() + j);
                j--;
            }
        }

        stack<char> s;
        while (k < v.size()) {
            c = v[k];
            if (!s.empty() && abs(c - s.top()) == 'a'-'A') {
                s.pop();
            } else {
                s.push(c);
            }
            k++;
        }

        if (s.size() < min_size) {
            min_size = s.size();
        }
    }

    cout << min_size;
    return 0;
}
