#include <bits/stdc++.h>

using namespace std;

#define MAXSIZE 301

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int id;
    cin >> id;
    int grid[MAXSIZE][MAXSIZE];
    pair <pair<int, int>, int> max, tmp;

    max.second = 0;
    for (int i = 1; i < MAXSIZE; ++i) {
        for (int j = 1; j < MAXSIZE; ++j) {
            grid[i][j] = i + 10;
            grid[i][j] *= j;
            grid[i][j] += id;
            grid[i][j] *= i + 10;
            grid[i][j] %= 1000;
            grid[i][j] /= 100;
            grid[i][j] -= 5;

            if (i > 2 && j > 2) {
                tmp.first = make_pair(i-2,j-2);
                tmp.second = 0;

                for (int h = i-2; h <= i; ++h) {
                    for (int k = j-2; k <= j; ++k) {
                        tmp.second += grid[h][k];
                    }
                }

                if (tmp.second > max.second) {
                    max = tmp;
                }
            }
        }
    }

    cout << (max.first).first << ',' << (max.first).second;
    return 0;
}
