#include <stdio.h>

#define MAX_SIZE 100
#define max(x, y) (((x) > (y)) ? (x) : (y))

enum Direction { Left, Right, Up, Down };

int viewing_distance(int area[MAX_SIZE][MAX_SIZE], int t_i, int t_j, int border, enum Direction dir) {
    int i = t_i;
    int j = t_j;

    int *compare_dim = (dir == Up || dir == Down) ? &i : &j;
    int increment = (dir == Right || dir == Down) ? 1 : -1;

    int res = 0;
    int height = area[t_i][t_j];
    do {
        res++;
        *compare_dim += increment;
    } while (area[i][j] < height && *compare_dim != border);

    return res;
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

    int res = 0;
    for (int i = 1; i < n_rows-1; i++) {
        for (int j = 1; j < n_cols-1; j++) {
            int scenic_score = 
                viewing_distance(area, i, j, 0, Up) *
                viewing_distance(area, i, j, 0, Left) *
                viewing_distance(area, i, j, n_cols-1, Right) *
                viewing_distance(area, i, j, n_rows-1, Down);
            res = max(res, scenic_score);
        }
    }

    printf("%d", res);
    return 0;
}
