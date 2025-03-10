#include <stdio.h>
#include <string.h>

#define N_COMPARE 14

int main() {
    char *buffer = NULL;
    int len;
    getline(&buffer, &len, stdin);
    
    char compare[N_COMPARE];
    strncat(compare, buffer, N_COMPARE-1);
    
    int i;
    char *res;
    for (i = N_COMPARE-1; i < strlen(buffer); i++) {
        res = strchr(compare, (int)buffer[i]);
        if (!res) {
            for (int j = 0; j < N_COMPARE-1; j++) {
                res = strchr(&compare[j+1], (int)compare[j]);
                if (res) {
                    break;
                }
            }
            if (!res) {
                break;
            }
        }
        compare[i % (N_COMPARE-1)] = buffer[i];
    }

    printf("%d", i+1);
    return 0;
}
