#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    stack<char> s;
    char c;
    while (cin >> c) {
        if (!s.empty() && abs(c-s.top()) == 'a'-'A') {
            s.pop();
        } else {
            s.push(c);
        }
    }

    cout << s.size();
    return 0;
}
