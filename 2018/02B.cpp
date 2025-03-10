#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s, res;
    vector <string> ids;
    bool found = false;

    while (!found && cin >> s) {
        for (unsigned int i = 0; i < ids.size(); ++i) {
            int differ = 0;
            for (unsigned int j = 0; j < s.length(); ++j) {
                if (s[j] != ids[i][j]){
                    differ++;
                }
                if (differ > 1) {
                    break;
                }
            }

            if (differ == 1) {
                res = ids[i];
                found = true;
                break;
            }
        }
        ids.push_back(s);
    }
    
    for (unsigned int j = 0; j < s.length(); ++j) {
        if (s[j] == res[j]) {
            cout << s[j];
        }
    }
    return 0;
}
