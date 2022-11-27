#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int twos = 0, threes = 0;
    
    while (cin >> s) {
        vector <pair <char, int> > letters;
        for (unsigned int i = 0; i < s.length(); ++i) {
            bool already_searched = false;
            for (unsigned int k = 0; k < letters.size(); ++k) {
                if (s[i] == letters[k].first) {
                    already_searched = true;
                    break;
                }
            }
            
            if (already_searched) {
                continue;
            }
            
            letters.push_back(make_pair(s[i], 1));
            for (unsigned int j = i+1; j < s.length(); ++j) {
                if (s[j] == s[i]) {
                    letters.back().second++;
                }
            }
        }
        
        bool yes2 = false, yes3 = false;
        for (unsigned int k = 0; k < letters.size(); ++k) {
            if (!yes2 && letters[k].second == 2) {
                twos++;
                yes2 = true;
            }
            if (!yes3 && letters[k].second == 3) {
                threes++;
                yes3 = true;
            }
        }
    }

    cout << twos * threes;
    return 0;
}
