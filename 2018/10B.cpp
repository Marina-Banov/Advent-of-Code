#include <bits/stdc++.h>

using namespace std;

#define MESSAGE_H 10
#define MAXSIZE 51000

typedef struct {
    pair<int, int> pos, vel;
} star;

typedef struct {
    pair<int, int> tl, br;
} border;

void defineSkyBorder(star one, border& skyBorder) {
    if (one.pos.first < skyBorder.tl.first) {
        skyBorder.tl.first = one.pos.first;
    }
    if (one.pos.second < skyBorder.tl.second) {
        skyBorder.tl.second = one.pos.second;
    }
    if (one.pos.first > skyBorder.br.first) {
        skyBorder.br.first = one.pos.first;
    }
    if (one.pos.second > skyBorder.br.second) {
        skyBorder.br.second = one.pos.second;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<star> message;
    star one;
    while (scanf("position=<%d,%d> velocity=<%d,%d>\n", &one.pos.first, &one.pos.second, &one.vel.first, &one.vel.second) > 0) {
        message.push_back(one);
    }

    int res = 0;
    border skyBorder;
    do {
        skyBorder.tl.first = MAXSIZE, skyBorder.tl.second = MAXSIZE, skyBorder.br.first = -MAXSIZE, skyBorder.br.second = -MAXSIZE;
        for (unsigned int i = 0; i < message.size(); ++i) {
            message[i].pos.first += message[i].vel.first;
            message[i].pos.second += message[i].vel.second;
            defineSkyBorder(message[i], skyBorder);
        }
        res++;
    } while (abs(skyBorder.br.second - skyBorder.tl.second) > MESSAGE_H);

    cout << res;
    return 0;
}
