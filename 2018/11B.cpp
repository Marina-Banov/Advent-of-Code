#include <bits/stdc++.h>

using namespace std;

#define MAXSIZE 301

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int id;
    cin >> id;
    int grid[MAXSIZE][MAXSIZE];
    pair <pair<int, int>, pair<int, int> > max, tmp;
    max.second.second = 0;
    for (int i = 1; i < MAXSIZE; ++i) {
        for (int j = 1; j < MAXSIZE; ++j) {
            grid[i][j] = i + 10;
            grid[i][j] *= j;
            grid[i][j] += id;
            grid[i][j] *= i + 10;
            grid[i][j] %= 1000;
            grid[i][j] /= 100;
            grid[i][j] -= 5;
            pair <pair<int, int>, pair<int, int> > single_max;
            
            single_max.second.second = 0;
            int border = (i < j) ? i : j;
            
            int last = 0;
            for (int l = 0; l < border; ++l) {
                tmp.first = make_pair(i-l,j-l);
                tmp.second.first = l+1;
                tmp.second.second = 0;
                if (!last) {
                    tmp.second.second = grid[i][j];
                } else {
                    tmp.second.second = last;
                    for (int h = i-l+1; h <= i; ++h) {
                        tmp.second.second += grid[h][j-l];
                    }
                    for (int k = j-l; k <= j; ++k) {
                        tmp.second.second += grid[i-l][k];
                    }
                }

                last = tmp.second.second;
                if (tmp.second.second > single_max.second.second) {
                    single_max = tmp;
                }
            }

            if (single_max.second.second > max.second.second) {
                max = single_max;
            }
        }
    }

    cout << max.first.first << ',' << max.first.second << ',' << max.second.first;
    return 0;
}
