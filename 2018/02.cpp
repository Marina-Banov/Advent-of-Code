#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int partOne(vector<string>& ids) {
    int twos = 0;
    int threes = 0;
    for (string s : ids) {
        vector<pair<char, int>> letters;
        for (unsigned int i = 0; i < s.length(); ++i) {
            bool searched = false;
            for (pair<char, int> letter : letters) {
                if (s[i] == letter.first) {
                    searched = true;
                    break;
                }
            }
            if (searched) {
                continue;
            }
            letters.push_back(make_pair(s[i], 1));
            for (unsigned int j = i+1; j < s.length(); ++j) {
                if (s[j] == s[i]) {
                    letters.back().second++;
                }
            }
        }
        bool yes2 = false, yes3 = false;
        for (pair<char, int> letter : letters) {
            if (!yes2 && letter.second == 2) {
                twos++;
                yes2 = true;
            }
            if (!yes3 && letter.second == 3) {
                threes++;
                yes3 = true;
            }
        }
    }
    return twos * threes;
}

string partTwo(vector<string>& ids) {
    string result;
    for (unsigned int i = 0; i < ids.size(); ++i) {
        for (unsigned int j = i; j < ids.size(); ++j) {
            int differ = 0;
            for (unsigned int k = 0; k < ids[i].length(); ++k) {
                if (ids[i][k] != ids[j][k]) {
                    differ++;
                }
                if (differ > 1) {
                    break;
                }
            }
            if (differ != 1) {
                continue;
            }
            for (unsigned int k = 0; k < ids[i].length(); ++k) {
                if (ids[i][k] == ids[j][k]) {
                    result += ids[i][k];
                }
            }
            return result;
        }
    }
    return result;
}

int main() {
    ifstream file("input");
    string s;
    vector<string> ids;
    while (file >> s) {
        ids.push_back(s);
    }

    cout << partOne(ids) << endl;
    cout << partTwo(ids) << endl;
    return 0;
}
