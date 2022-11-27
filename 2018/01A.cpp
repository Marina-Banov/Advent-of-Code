#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int sum = 0, val;
    while (cin >> val) {
        sum += val;
    }

    cout << sum;
    return 0;
}
