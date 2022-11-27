#include <bits/stdc++.h>

using namespace std;

#define ENTRIES 2000

typedef struct  {
    int month, day, hour, minute;
    string s;
} record;

typedef struct {
    char graph[60];
} shift;

typedef struct {
    int personal_id;
    int asleep;
    vector<shift> all;
} guard;

bool compare(record a, record b) {
    if (a.month == b.month) {
        if (a.day == b.day) {
            if (a.hour == b.hour) {
                return a.minute < b.minute;
            }
            return a.hour < b.hour;
        }
        return a.day < b.day;
    }
    return a.month < b.month;
}

void add_info(unsigned int last_min, vector<guard>& guards, shift s, int id) {
    guard g;
    g.personal_id = id;
    g.asleep = 0;

    for (unsigned int i = 0; i < last_min; ++i) {
        if (s.graph[i] == '#') {
            g.asleep++;
        }
    }
    
    for (unsigned int i = last_min; i < 60; ++i) {
        s.graph[i] = '.';
    }

    for (unsigned int i = 0; i < guards.size(); ++i) {
        if (g.personal_id == guards[i].personal_id) {
            (guards[i].all).push_back(s);
            guards[i].asleep += g.asleep;
            return;
        }
    }

    (g.all).push_back(s);
    guards.push_back(g);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<record> records;
    record r;
    char c;
    int year;
    while (cin >> c >> year >> c >> r.month >> c >> r.day >> r.hour >> c >> r.minute >> c && getline(cin, r.s)) {
        records.push_back(r);
    }
    sort(records.begin(), records.end(), compare);
    
    shift s;
    vector<guard> guards;
    unsigned int last_min = 0, id = 0;

    for (unsigned int i = 0; i < records.size(); ++i) {
        string c = records[i].s.substr(1,5);

        if (c == "Guard") {
            if (i) {
                add_info(last_min, guards, s, id);
            }
            id = 0;
            for (int j = 8; records[i].s[j] != ' '; ++j) {
                id *= 10;
                id += records[i].s[j]-'0';
            }
            last_min = 0;
        } else if (c == "falls") {
            for (int j = last_min; j < records[i].minute; ++j) {
                s.graph[j] = '.';
            }
            last_min = records[i].minute;
        } else if (c == "wakes") {
            for (int j = last_min; j < records[i].minute; ++j) {
                s.graph[j] = '#';
            }
            last_min = records[i].minute;
        }
    }
    add_info(last_min, guards, s, id);

    guard max_asleep;
    max_asleep.asleep = 0;
    for (unsigned int i = 0; i < guards.size(); ++i) {
        if (guards[i].asleep > max_asleep.asleep) {
            max_asleep = guards[i];
        }
    }

    pair <int, int> which_minute(0,0), tmp;
    for (int j = 0; j < 60; ++j) {
        tmp.first = j;
        tmp.second = 0;
        for (unsigned int i = 0; i < (max_asleep.all).size(); ++i) {
            if ((max_asleep.all[i]).graph[j] == '#') {
                tmp.second++;
            }
        }
        if (tmp.second > which_minute.second) {
            which_minute = tmp;
        }
    }
    
    cout << max_asleep.personal_id * which_minute.first;
    return 0;
}
