#include <bits/stdc++.h>
#include <fstream>

#define MAX_SIZE 125000

using namespace std;

int partOne(vector<int>& changes) {
    int result = 0;
    for (int change : changes) {
        result += change;
    }
    return result;
}

int partTwo(vector<int>& changes) {
    bool values[2 * MAX_SIZE] = {false};
    values[MAX_SIZE] = true;
    int result = 0;
    int i = 0;
    while (true) {
        result += changes[i];
        if (values[result + MAX_SIZE]) {
            return result;
        }
        values[result + MAX_SIZE] = true;
        i = (i + 1) % changes.size();
    }
    return 0;
}

int main() {
    ifstream file("input");
    int change;
    vector<int> changes;
    while (file >> change) {
        changes.push_back(change);
    }

    cout << partOne(changes) << endl;
    cout << partTwo(changes) << endl;
    return 0;
}
