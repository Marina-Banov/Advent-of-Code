#include <bits/stdc++.h>
#include <fstream>

using namespace std;

#define MAX_SIZE 300

int getPowerLevel(int i, int j, int id) {
    int result = (i + 10) * j + id;
    result = result * (i + 10) % 1000;
    return result / 100 - 5;
}

string partOne(int id) {
    int grid[MAX_SIZE][MAX_SIZE] = {0};
    pair<pair<int, int>, int> max, tmp;
    max.second = 0;
    for (int i = 1; i < MAX_SIZE; ++i) {
        for (int j = 1; j < MAX_SIZE; ++j) {
            grid[i][j] = getPowerLevel(i, j, id);
            if (i <= 2 || j <= 2) {
                continue;
            }
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
    return to_string(max.first.first) + "," + to_string(max.first.second);
}

string partTwo(int id) {
    int grid[MAX_SIZE][MAX_SIZE] = {0};
    pair<pair<int, int>, pair<int, int>> max, tmp;
    max.second.second = 0;
    for (int i = 1; i < MAX_SIZE; ++i) {
        for (int j = 1; j < MAX_SIZE; ++j) {
            grid[i][j] = getPowerLevel(i, j, id);
            pair<pair<int, int>, pair<int, int>> singleMax;
            singleMax.second.second = 0;
            int border = min(i, j);
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
                if (tmp.second.second > singleMax.second.second) {
                    singleMax = tmp;
                }
            }
            if (singleMax.second.second > max.second.second) {
                max = singleMax;
            }
        }
    }
    return to_string(max.first.first) + "," + to_string(max.first.second) + "," + to_string(max.second.first);
}

int main() {
    ifstream file("input");
    int id;
    file >> id;

    cout << partOne(id) << endl;
    cout << partTwo(id) << endl;
    return 0;
}
