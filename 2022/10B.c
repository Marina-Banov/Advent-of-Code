#include <stdio.h>
#include <string.h>

#define N_ROWS 6
#define N_COLS 40

char draw_pixel(int cycle, int x) {
	return (cycle >= x-1 && cycle <= x+1) ? '#' : ' ';
}

int main() {
    char crt[N_ROWS*N_COLS];
    char* line = NULL;
    int x = 1;
    int cycle = 0;
    int len;
    int lineSize;

    while ((lineSize = getline(&line, &len, stdin)) > 0) {
    	crt[cycle] = draw_pixel(cycle % N_COLS, x);
        cycle++;

        if (strstr(line, "addx")) {
            int value;
            sscanf(line, "addx %d ", &value);
    		crt[cycle] = draw_pixel(cycle % N_COLS, x);
            cycle++;
            x += value;
        }
    }

    for (int i = 0; i < N_ROWS; i++) {
	    for (int j = 0; j < N_COLS; j++) {
	    	printf("%c", crt[i*N_COLS+j]);
	    }
	    printf("\n");
    }

    return 0;
}
