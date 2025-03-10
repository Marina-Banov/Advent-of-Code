#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRLEN 64

int main() {
    char *line = malloc(MAX_STRLEN * sizeof(char));
    int len = 0;
    int line_size = 0;
    char *lines[10];
    int i = 0;
    while ((line_size = getline(&line, &len, stdin)) != 1) {
        lines[i] = malloc(MAX_STRLEN * sizeof(char));
        strcpy(lines[i++], line);
    }
    free(line);

    int n_stacks = lines[i-1][strlen(lines[i-1])-3] - '0';
    free(lines[i-1]);
    char *stacks[n_stacks];
    for (int j = 0; j < n_stacks; j++) {
        stacks[j] = malloc(MAX_STRLEN * sizeof(char));
        strcpy(stacks[j], "");
    }
    for (int j = i-2; j >= 0; j--) {
        for (int k = 0; k < n_stacks; k++) {
            if (lines[j][1+k*4] != ' ') {
                strncat(stacks[k], &lines[j][1+k*4], 1);
            }
        }
        free(lines[j]);
    }

    int n_crates, from, to;
    while (scanf("move %d from %d to %d\n", &n_crates, &from, &to) == 3) {
        int index_to_remove = strlen(stacks[from-1]) - n_crates;
        strcat(stacks[to-1], &stacks[from-1][index_to_remove]);
        stacks[from-1][index_to_remove] = '\0';
    }

    for (int j = 0; j < n_stacks; j++) {
        printf("%c", stacks[j][strlen(stacks[j])-1]);
        free(stacks[j]);
    }
    return 0;
}
