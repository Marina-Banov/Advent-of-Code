#include <stdio.h>

#define shape(me) me + 1
#define outcome(opponent, me) ((me - opponent + 4) % 3) * 3

int main() {
    char opponent, me;
    int result = 0;

    while (scanf("%c %c\n", &opponent, &me) == 2) {
        opponent -= 'A';
        me -= 'X';
        result += shape(me) + outcome(opponent, me);
    }

    printf("%d", result);
    return 0;
}
