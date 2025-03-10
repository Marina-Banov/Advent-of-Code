#include <bits/stdc++.h>

using namespace std;

#define MAXSIZE 1000

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    short int fabric[MAXSIZE][MAXSIZE] = {0};
    vector <bool> all_overlaps;
    bool one_overlaps;
    char c;
    int id, start_col, start_row, end_col, end_row;

    while (cin >> c >> id >> c >> start_col >> c >> start_row >> c >> end_col >> c >> end_row) {
        one_overlaps = false;
        end_row += start_row;
        end_col += start_col;
        for (int i = start_row; i < end_row; ++i) {
            for (int j = start_col; j < end_col; ++j) {
                if (fabric[i][j] != 0) {
                    one_overlaps = true;
                    all_overlaps[fabric[i][j]-1] = true;
                }
                fabric[i][j] = id;
            }
        }
        all_overlaps.push_back(one_overlaps);
    }

    for (unsigned int h = 0; h < all_overlaps.size(); ++h) {
        if (!all_overlaps[h]) {
            cout << h+1;
            break;
        }
    }
    return 0;
}
