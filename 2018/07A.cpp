#include <bits/stdc++.h>
#include <algorithm>
#include <string>

using namespace std;
using namespace placeholders;

typedef struct {
    char name;
    string dependencies;
} Task;

string critical_path(vector<Task> remaining) {
    string completed = "";
    unsigned int i = 0;
    auto in_string = [&](char c) { return completed.find(c) < completed.length(); };

    while (remaining.size()) {
        i = 0;
        while (i < remaining.size()) {
            if (all_of(
                remaining[i].dependencies.begin(), remaining[i].dependencies.end(),
                in_string
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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<Task> all_tasks;
    string s;

    auto task_not_found = [&](vector<Task>::iterator task_it, char name) {
        return all_tasks.size() == 0 || 
            (task_it == all_tasks.end() && task_it->name != name);
    };

    while (getline(cin, s)) {
        char dep_name = s[5];
        auto dep_task_it = find_if(
            all_tasks.begin(), all_tasks.end(), 
            [=](Task t) { return t.name == dep_name; }
        );
        if (task_not_found(dep_task_it, dep_name)) {
            all_tasks.push_back({ dep_name, "" });
        }

        char task_name = s[36];
        auto task_it = find_if(
            all_tasks.begin(), all_tasks.end(),
            [=](Task t) { return t.name == task_name; }
        );
        if (task_not_found(task_it, task_name)) {
            all_tasks.push_back({ task_name, string(1, dep_name) });
        } else {
            task_it->dependencies += dep_name;
        }
    }

    sort(
        all_tasks.begin(), all_tasks.end(),
        [](Task t1, Task t2) { return t1.name < t2.name; }
    );

    cout << critical_path(all_tasks);
    return 0;
}
