#include <stdio.h>

int main() {
    int a, b, c, d;
    int result = 0;

    while (scanf("%d-%d,%d-%d ", &a, &b, &c, &d) == 4) {
        if (a >= c && b <= d || a <= c && b >= d) {
            result++;
        }
    }

    printf("%d", result);
    return 0;
}
