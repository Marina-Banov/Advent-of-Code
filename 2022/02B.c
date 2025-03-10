#include <stdio.h>

#define shape(opponent, me) ((opponent + me + 2) % 3) + 1
#define outcome(me) me * 3

int main() {
    char opponent, me;
    int result = 0;

    while (scanf("%c %c\n", &opponent, &me) == 2) {
        opponent -= 'A';
        me -= 'X';
        result += shape(opponent, me) + outcome(me);
    }

    printf("%d", result);
    return 0;
}
