#include <bits/stdc++.h>
#include <fstream>

using namespace std;

typedef struct {
    int year, month, day, hour, minute;
    string s;
} Record;

typedef struct {
    char graph[60];
} Shift;

typedef struct {
    int id, timeAsleep;
    pair<int, int> resultMinute;
    vector<Shift> shifts;
} Guard;

int partOne(vector<Guard>& guards) {
    Guard resultGuard;
    resultGuard.timeAsleep = 0;
    for (Guard g : guards) {
        if (g.timeAsleep > resultGuard.timeAsleep) {
            resultGuard = g;
        }
    }
    pair<int, int> resultMinute(0, 0), tmp;
    for (int j = 0; j < 60; ++j) {
        tmp.first = j;
        tmp.second = 0;
        for (Shift s : resultGuard.shifts) {
            if (s.graph[j] == '#') {
                tmp.second++;
            }
        }
        if (tmp.second > resultMinute.second) {
            resultMinute = tmp;
        }
    }
    return resultGuard.id * resultMinute.first;
}

int partTwo(vector<Guard>& guards) {
    Guard resultGuard;
    pair<int,int> tmp;
    for (Guard& g : guards) {
        for (int j = 0; j < 60; ++j) {
            tmp.first = j;
            tmp.second = 0;
            for (Shift s : g.shifts) {
                if (s.graph[j] == '#') {
                    tmp.second++;
                }
            }
            if (tmp.second > g.resultMinute.second) {
                g.resultMinute = tmp;
            }
        }
        if (g.resultMinute.second > resultGuard.resultMinute.second) {
            resultGuard = g;
        }
    }
    return resultGuard.id * resultGuard.resultMinute.first;
}

bool compare(Record a, Record b) {
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

void addInfo(unsigned int lastMinute, vector<Guard>& guards, Shift s, int id) {
    Guard newGuard;
    newGuard.id = id;
    newGuard.timeAsleep = 0;
    for (unsigned int i = 0; i < lastMinute; ++i) {
        if (s.graph[i] == '#') {
            newGuard.timeAsleep++;
        }
    }
    for (unsigned int i = lastMinute; i < 60; ++i) {
        s.graph[i] = '.';
    }
    for (Guard& g : guards) {
        if (newGuard.id == g.id) {
            g.shifts.push_back(s);
            g.timeAsleep += newGuard.timeAsleep;
            return;
        }
    }
    newGuard.shifts.push_back(s);
    guards.push_back(newGuard);
}

vector<Guard> getGuards(vector<Record>& records) {
    Shift s;
    vector<Guard> guards;
    unsigned int lastMinute = 0, id = 0;
    for (unsigned int i = 0; i < records.size(); ++i) {
        string c = records[i].s.substr(1,5);
        if (c == "Guard") {
            if (i) {
                addInfo(lastMinute, guards, s, id);
            }
            id = 0;
            for (int j = 8; records[i].s[j] != ' '; ++j) {
                id *= 10;
                id += records[i].s[j] - '0';
            }
            lastMinute = 0;
        } else if (c == "falls") {
            for (signed int j = lastMinute; j < records[i].minute; ++j) {
                s.graph[j] = '.';
            }
            lastMinute = records[i].minute;
        } else if (c == "wakes") {
            for (signed int j = lastMinute; j < records[i].minute; ++j) {
                s.graph[j] = '#';
            }
            lastMinute = records[i].minute;
        }
    }
    addInfo(lastMinute, guards, s, id);
    return guards;
}

int main() {
    ifstream file("input");
    vector<Record> records;
    Record r;
    char c;
    while (file >> c >> r.year >> c >> r.month >> c >> r.day >> r.hour >> c >> r.minute >> c && getline(file, r.s)) {
        records.push_back(r);
    }
    sort(records.begin(), records.end(), compare);
    vector<Guard> guards = getGuards(records);

    cout << partOne(guards) << endl;
    cout << partTwo(guards) << endl;
    return 0;
}
