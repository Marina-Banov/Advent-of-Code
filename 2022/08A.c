#include <stdio.h>

#define MAX_SIZE 100

enum Direction { Left, Right, Up, Down };

int compare_visibility(int area[MAX_SIZE][MAX_SIZE], int t_i, int t_j, int border, enum Direction dir) {
    int i = t_i;
    int j = t_j;

    int *compare_dim = (dir == Up || dir == Down) ? &i : &j;
    int increment = (dir == Right || dir == Down) ? 1 : -1;

    int height = area[t_i][t_j];
    do {
        *compare_dim += increment;
    } while (area[i][j] < height && *compare_dim != border);

    return *compare_dim == border;
}

int main() {
    char *line = NULL;
    int len;
    int lineSize;
    int area[MAX_SIZE][MAX_SIZE];
    int n_rows = 0;
    int n_cols;

    while ((lineSize = getline(&line, &len, stdin)) != -1) {
        n_cols = lineSize-1;
        for (int j = 0; j < n_cols; j++) {
            area[n_rows][j] = line[j]-'0';
        }
        n_rows++;
    }

    int count = 2*n_cols + 2*n_rows - 4;
    for (int i = 1; i < n_rows-1; i++) {
        for (int j = 1; j < n_cols-1; j++) {
            if (compare_visibility(area, i, j, -1, Up) ||
                compare_visibility(area, i, j, -1, Left) ||
                compare_visibility(area, i, j, n_cols, Right) ||
                compare_visibility(area, i, j, n_rows, Down)) {
                count++;
            }
        }
    }

    printf("%d", count);
    return 0;
}
