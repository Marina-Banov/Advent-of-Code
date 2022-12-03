#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main() {
    char *line = NULL;
    int len = 0;
    int line_size = 0;
    int result = 0;
    int group = 0;
    int occurences[52] = {0};

    while ((line_size = getline(&line, &len, stdin)) != -1) {
        group++;
        
        for (int i = 0; i < line_size; ++i) {
            char c = line[i];
            int code = isupper(c) ? c - 'A' + 26 : c - 'a';

            if (occurences[code] == group-1) {
                if (group == 3) {
                    result += code + 1;
                    group = 0;
                    memset(occurences, 0, sizeof occurences);
                    break;
                }
                occurences[code]++;
            }
        }
    }

    printf("%d", result);
    return 0;
}
