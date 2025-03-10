#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    stack < pair <int, int> > data;
    int children_count, metadata_count, sum = 0, tmp;

    cin >> children_count >> metadata_count;
    pair<int, int> r(children_count, metadata_count);
    data.push(r);
    
    while (!data.empty()) {
        for (int i = 0; i < data.top().first; ++i) {
            cin >> children_count >> metadata_count;
            pair<int, int> r(children_count, metadata_count);
            if (!children_count) {
                (data.top().first)--;
                for (int j = 0; j < metadata_count; ++j) {
                    cin >> tmp;
                    sum += tmp;
                }
                break;
            }
            data.push(r);
        }

        if (!data.top().first) {
            for (int j = 0; j < data.top().second; ++j) {
                cin >> tmp;
                sum += tmp;
            }

            data.pop();
            
            if (!data.empty()) {
                (data.top().first)--;
            }
        }
    }

    cout << sum;
    return 0;
}
