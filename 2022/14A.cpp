#include <bits/stdc++.h>
#include <regex>

using namespace std;


vector<string> split(string str, string delimiter) {
    regex regexz(delimiter);
    return {sregex_token_iterator(str.begin(), str.end(), regexz, -1),
            sregex_token_iterator()};
}

vector<vector<pair<int,int>>> read_input() {
    int min_cols = 999;
    int n_rows = 0, n_cols = 0;

    int x, y;
    vector<vector<pair<int,int>>> paths;
    vector<pair<int,int>> path;

    string path_s;
    while (!cin.eof()) {
        getline(cin, path_s);
        auto coords_s = split(path_s, " -> ");
        for (auto c : coords_s) {
            sscanf(c.c_str(), "%d,%d", &x, &y);
            path.push_back(make_pair(y,x));
            n_rows = max(n_rows, y);
            min_cols = min(min_cols, x);
            n_cols = max(n_cols, x);
        }
        paths.push_back(path);
        path.clear();
    }

    paths.push_back({make_pair(0, n_rows), make_pair(min_cols, n_cols)});
    return paths;
}

char** get_matrix(int n_rows, int n_cols, vector<vector<pair<int,int>>> paths, int col_offset) {
    char** matrix = new char*[n_rows];
    for (int i = 0; i < n_rows; ++i) {
        matrix[i] = new char[n_cols];
        memset(matrix[i], '.', n_cols*sizeof(char));
    }

    for (auto path : paths) {
        for (auto p = path.begin(); p < path.end()-1; p++) {
            int x = min(p->second, (p+1)->second);
            int y = min(p->first, (p+1)->first);
            int n_rocks = max(abs((p+1)->second - p->second), abs((p+1)->first - p->first));
            int *dimension = (p->first == (p+1)->first) ? &x : &y;
            for (int j = 0; j <= n_rocks; j++) {
                matrix[y][x+col_offset] = '#';
                *dimension += 1;
            }
        }
    }
    return matrix;
}

bool is_free(char **matrix, int i, int j) {
    return matrix[i][j] == '.';
}

bool valid_coords(int n_rows, int n_cols, int i, int j) {
    return i >= 0 && i < n_rows-1 && j >= 1 && j < n_cols-1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    auto paths = read_input();
    auto borders = *(paths.end()-1);
    paths.pop_back();
    int n_rows = borders[0].second + 1;
    int min_cols = borders[1].first;
    int n_cols = borders[1].second - min_cols + 1;

    char **matrix = get_matrix(n_rows, n_cols, paths, -min_cols);
    matrix[0][500-min_cols] = '+';

    int count = 0;
    pair<int,int> sand(0, 500-min_cols);  // source_of_sand
    while (valid_coords(n_rows, n_cols, sand.first, sand.second)) {
        if (is_free(matrix, sand.first+1, sand.second)) {
            sand.first++;
        } else if (is_free(matrix, sand.first+1, sand.second-1)) {
            sand.first++;
            sand.second--;
        } else if (is_free(matrix, sand.first+1, sand.second+1)) {
            sand.first++;
            sand.second++;
        } else {
            matrix[sand.first][sand.second] = 'o';
            count++;
            sand = make_pair(0, 500-min_cols);
        }
    }

    cout << count;
    return 0;
}
