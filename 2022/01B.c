#include <stdio.h>

void compare_three(int current, int *a, int *b, int *c) {
    if (current <= *c) {
        return;
    }

    if (current <= *b) {
        *c = current;
        return;
    }

    *c = *b;

    if (current <= *a) {
        *b = current;
    } else {
        *b = *a;
        *a = current;
    }
}

int main() {
    int ch;
    int n = 0;
    int current_calories = 0;
    int a = 0, b = 0, c = 0;

    while ((ch = getchar()) != EOF) {
        if (ch == '\n') {
            if (n == 0) {
                compare_three(current_calories, &a, &b, &c);
                current_calories = 0;
            }
            current_calories += n;
            n = 0;
            continue;
        }
        n *= 10;
        n += ch - '0';
    }
    compare_three(current_calories + n, &a, &b, &c);

    printf("%d", a + b + c);
    return 0;
}
