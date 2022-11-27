#include <bits/stdc++.h>

using namespace std;

#define MAX_ENTRY 125000

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int sum = 0, val;
    vector<int> values;
    bool frequencies[2*MAX_ENTRY];
    memset(frequencies, false, 2*MAX_ENTRY);

    while (cin >> val) {
        if (frequencies[sum + MAX_ENTRY]) { 
            cout << sum;
            return 0;
        } else {
            frequencies[sum + MAX_ENTRY] = true;
        }
        values.push_back(val);
        sum += val;
    }

    unsigned int i = 0;
    while (1) {
        if (frequencies[sum + MAX_ENTRY]) {
            cout << sum;
            break;
        } else {
            frequencies[sum + MAX_ENTRY] = true;
        }

        if (i == values.size()) {
            i = 0;
        }
        sum += values[i++];
    }

    return 0;
}
