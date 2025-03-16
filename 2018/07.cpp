#include <bits/stdc++.h>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;
using namespace placeholders;

typedef struct {
    char name;
    string dependencies;
} Task;

string partOne(vector<Task> remaining) {
    string completed = "";
    unsigned int i = 0;
    auto inString = [&](char c) { return completed.find(c) < completed.length(); };
    while (remaining.size()) {
        i = 0;
        while (i < remaining.size()) {
            if (all_of(
                remaining[i].dependencies.begin(), remaining[i].dependencies.end(),
                inString
            )) {
                completed += remaining[i].name;
                remaining.erase(remaining.begin() + i);
                break;
            }
            i++;
        }
    }
    return completed;
}

int partTwo(vector<Task>& tasks) {
    return 0;
}

vector<Task> getTasks(vector<string> instructions) {
    vector<Task> tasks;
    auto taskNotFound = [&](vector<Task>::iterator taskIt, char name) {
        return tasks.size() == 0 ||
            (taskIt == tasks.end() && taskIt->name != name);
    };
    for (string i : instructions) {
        char depName = i[5];
        auto depTaskIt = find_if(
            tasks.begin(), tasks.end(),
            [=](Task t) { return t.name == depName; }
        );
        if (taskNotFound(depTaskIt, depName)) {
            tasks.push_back({ depName, "" });
        }
        char taskName = i[36];
        auto taskIt = find_if(
            tasks.begin(), tasks.end(),
            [=](Task t) { return t.name == taskName; }
        );
        if (taskNotFound(taskIt, taskName)) {
            tasks.push_back({ taskName, string(1, depName) });
        } else {
            taskIt->dependencies += depName;
        }
    }
    sort(
        tasks.begin(), tasks.end(),
        [](Task t1, Task t2) { return t1.name < t2.name; }
    );
    return tasks;
}

int main() {
    ifstream file("input");
    vector<string> instructions;
    string i;
    while (getline(file, i)) {
        instructions.push_back(i);
    }
    vector<Task> tasks = getTasks(instructions);

    cout << partOne(tasks) << endl;
    cout << partTwo(tasks) << endl;
    return 0;
}
