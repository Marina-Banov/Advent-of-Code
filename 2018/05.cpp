#include <bits/stdc++.h>
#include <fstream>

using namespace std;

unsigned int partOne(vector<char>& polymer) {
    stack<char> s;
    for (char p : polymer) {
        if (!s.empty() && abs(p - s.top()) == 'a' - 'A') {
            s.pop();
        } else {
            s.push(p);
        }
    }
    return s.size();
}

unsigned int partTwo(vector<char>& polymer) {
    unsigned int minSize = polymer.size();
    for (char i = 'a'; i <= 'z'; ++i) {
        vector<char> v(polymer);
        for (unsigned int j = 0; j < v.size(); ++j) {
            if (v.at(j) == i || i - v.at(j) == 'a' - 'A') {
                v.erase(v.begin() + j);
                j--;
            }
        }
        minSize = min(partOne(v), minSize);
    }
    return minSize;
}

int main() {
    ifstream file("input");
    vector<char> polymer;
    char p;
    while (file >> p) {
        polymer.push_back(p);
    }

    cout << partOne(polymer) << endl;
    cout << partTwo(polymer) << endl;
    return 0;
}
