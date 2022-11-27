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
    pair<int, int> min_most_freq_asleep;
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
    for (unsigned int i = last_min; i < 60; ++i) {
        s.graph[i] = '.';
    }

    for (unsigned int i = 0; i < guards.size(); ++i) {    
        if (g.personal_id == guards[i].personal_id) {
            (guards[i].all).push_back(s);
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
            for (signed int j = last_min; j < records[i].minute; ++j) {
                s.graph[j] = '.';
            }
            last_min = records[i].minute;
        } else if (c == "wakes") {
            for (signed int j = last_min; j < records[i].minute; ++j) {
                s.graph[j] = '#';
            }
            last_min = records[i].minute;
        }
    }
    add_info(last_min, guards, s, id);

    guard max_asleep;
    pair <int,int> tmp;
    for (unsigned int i = 0; i < guards.size(); ++i) {
        for (int j = 0; j < 60; ++j) {
            tmp.first = j;
            tmp.second = 0;
            for (unsigned int k = 0; k < (guards[i].all).size(); ++k) {
                if ((guards[i].all[k]).graph[j] == '#') {
                    tmp.second++;
                }
            }
            if (tmp.second > (guards[i].min_most_freq_asleep).second) {
                guards[i].min_most_freq_asleep = tmp;
            }
        }
        if ((guards[i].min_most_freq_asleep).second > (max_asleep.min_most_freq_asleep).second) {
            max_asleep = guards[i];
        }
    }

    cout << max_asleep.personal_id * (max_asleep.min_most_freq_asleep).first;
    return 0;
}
