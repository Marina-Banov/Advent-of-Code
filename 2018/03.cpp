#include <bits/stdc++.h>
#include <fstream>

#define MAX_SIZE 1000

using namespace std;

typedef struct {
    int id, startRow, startCol, rowSize, colSize;
} Claim;

int partOne(vector<Claim>& claims) {
    short int fabric[MAX_SIZE][MAX_SIZE] = {0};
    int result = 0;
    for (Claim cl : claims) {
        for (int i = 0; i < cl.rowSize; ++i) {
            for (int j = 0; j < cl.colSize; ++j) {
                if (fabric[cl.startRow+i][cl.startCol+j] == 1) {
                    result++;
                }
                fabric[cl.startRow+i][cl.startCol+j]++;
            }
        }
    }
    return result;
}

int partTwo(vector<Claim>& claims) {
    short int fabric[MAX_SIZE][MAX_SIZE] = {0};
    vector<bool> overlaps;
    for (Claim cl : claims) {
        bool overlap = false;
        for (int i = 0; i < cl.rowSize; ++i) {
            for (int j = 0; j < cl.colSize; ++j) {
                if (fabric[cl.startRow+i][cl.startCol+j] != 0) {
                    overlap = true;
                    overlaps[fabric[cl.startRow+i][cl.startCol+j]-1] = true;
                }
                fabric[cl.startRow+i][cl.startCol+j] = cl.id;
            }
        }
        overlaps.push_back(overlap);
    }
    for (unsigned int id = 0; id < overlaps.size(); ++id) {
        if (!overlaps[id]) {
            return id + 1;
        }
    }
    return 0;
}

int main() {
    ifstream file("input");
    vector<Claim> claims;
    Claim cl;
    char c;
    while (file >> c >> cl.id >> c >> cl.startCol >> c >> cl.startRow >> c >> cl.colSize >> c >> cl.rowSize) {
        claims.push_back(cl);
    }

    cout << partOne(claims) << endl;
    cout << partTwo(claims) << endl;
    return 0;
}
