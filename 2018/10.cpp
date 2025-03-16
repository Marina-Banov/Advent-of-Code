#include <bits/stdc++.h>

#define MESSAGE_H 10
#define MESSAGE_W 62
#define MAX_SIZE 51000

using namespace std;

typedef struct {
    pair<int, int> pos, vel;
} Star;

typedef struct {
    pair<int, int> tl, br;
} Border;

int getSkyBorder(Border& skyBorder, vector<Star>& stars) {
    int steps = 0;
    do {
        skyBorder.tl.first = MAX_SIZE, skyBorder.tl.second = MAX_SIZE, skyBorder.br.first = -MAX_SIZE, skyBorder.br.second = -MAX_SIZE;
        for (Star& s : stars) {
            s.pos.first += s.vel.first;
            s.pos.second += s.vel.second;
            skyBorder.tl.first = min(skyBorder.tl.first, s.pos.first);
            skyBorder.tl.second = min(skyBorder.tl.second, s.pos.second);
            skyBorder.br.first = max(skyBorder.br.first, s.pos.first);
            skyBorder.br.second = max(skyBorder.br.second, s.pos.second);
        }
        steps++;
    } while (abs(skyBorder.br.second - skyBorder.tl.second) > MESSAGE_H);
    return steps;
}

string partOne(char sky[MESSAGE_H][MESSAGE_W], vector<Star>& starsOriginal) {
    vector<Star> stars(starsOriginal);
    Border skyBorder;
    getSkyBorder(skyBorder, stars);
    for (Star s : stars) {
        sky[s.pos.second - skyBorder.tl.second][s.pos.first - skyBorder.tl.first] = '#';
    }
    string result = "";
    for (int i = 0; i < MESSAGE_H; ++i) {
        for (int j = 0; j < MESSAGE_W; ++j) {
            result += sky[i][j];
        }
        result += "\n";
    }
    return result;
}

int partTwo(char sky[MESSAGE_H][MESSAGE_W], vector<Star>& stars) {
    Border skyBorder;
    return getSkyBorder(skyBorder, stars);
}

int main() {
    FILE *file = fopen("input", "r");
    char sky[MESSAGE_H][MESSAGE_W];
    for (int i = 0; i < MESSAGE_H; ++i) {
        for (int j = 0; j < MESSAGE_W; ++j) {
            sky[i][j] = ' ';
        }
    }
    vector<Star> stars;
    Star s;
    while (fscanf(file, "position=<%d,%d> velocity=<%d,%d>\n", &s.pos.first, &s.pos.second, &s.vel.first, &s.vel.second) > 0) {
        stars.push_back(s);
    }

    cout << partOne(sky, stars) << endl;
    cout << partTwo(sky, stars) << endl;
    return 0;
}
