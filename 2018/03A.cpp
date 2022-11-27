#include <bits/stdc++.h>

using namespace std;

#define MAXSIZE 1000

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    pair<bool, bool> fabric[MAXSIZE][MAXSIZE];
    for (int i = 0; i < MAXSIZE; ++i) {
        for (int j = 0; j < MAXSIZE; ++j) {
            fabric[i][j].first = false;
            fabric[i][j].second = false;
        }
    }
    
    int id, start_row, start_col, end_row, end_col, res = 0;
    char c;
    while (cin >> c >> id >> c >> start_col >> c >> start_row >> c >> end_col >> c >> end_row) {
        end_row += start_row;
        end_col += start_col;
        for (int i = start_row; i < end_row; ++i) {
            for (int j = start_col; j < end_col; ++j) {
                if (fabric[i][j].first && !(fabric[i][j].second)) {
                    res++;
                    fabric[i][j].second = true;
                } else {
                    fabric[i][j].first = true;
                }
            }
        }
    }
    
    cout << res;
    return 0;
}
