#include <stdio.h>

#define max(x, y) (((x) > (y)) ? (x) : (y))

int main() {
    int ch;
    int n = 0;
    int current_calories = 0;
    int max_calories = 0;

    while ((ch = getchar()) != EOF) {
        if (ch == '\n') {
            if (n == 0) {
                max_calories = max(max_calories, current_calories);
                current_calories = 0;
            }
            current_calories += n;
            n = 0;
            continue;
        }
        n *= 10;
        n += ch - '0';
    }
    max_calories = max(max_calories, current_calories + n);

    printf("%d", max_calories);
    return 0;
}
