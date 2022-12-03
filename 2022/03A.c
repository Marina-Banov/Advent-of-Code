#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main() {
    char *line = NULL;
    int len = 0;
    int line_size = 0;
    int result = 0;

    while ((line_size = getline(&line, &len, stdin)) != -1) {
        int occurences[52] = {0};
        
        for (int i = 0; i < line_size; ++i) {
            char c = line[i];
            int code = isupper(c) ? c - 'A' + 26 : c - 'a';

            if (i < (line_size-1) / 2) {
                occurences[code]++;
                continue;
            }

            if (occurences[code] > 0) {
                result += code + 1;
                break;
            }

            occurences[code]--;
        }
    }

    printf("%d", result);
    return 0;
}
