#include <stdio.h>
#include <string.h>

void check_signal_strength(int cycle, int x, int* res) {
    int compare_array[] = { 20, 60, 100, 140, 180, 220 };
    for (int i = 0; i < 6; i++) {
        if (cycle == compare_array[i]) {
            *res += x * cycle;
            return;
        }
    }
}

int main() {
    char* line = NULL;
    int x = 1;
    int cycle = 0;
    int len;
    int lineSize;
    int res = 0;

    while ((lineSize = getline(&line, &len, stdin)) > 0) {
        cycle++;
        check_signal_strength(cycle, x, &res);

        if (strstr(line, "addx")) {
            int value;
            sscanf(line, "addx %d ", &value);
            cycle++;
            check_signal_strength(cycle, x, &res);
            x += value;
        }
    }

    printf("%d", res);
    return 0;
}
