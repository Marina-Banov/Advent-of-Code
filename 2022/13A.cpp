#include <bits/stdc++.h>
#include <vector>

using namespace std;

vector<string> get_vector(const string s) {
    vector<string> v;
    string curr = "";
    for (auto c = s.begin()+1; c != s.end()-1; ++c) {
        if (*c == ',' && curr.length() > 0) {
            v.push_back(curr);
            curr = "";
        } else if (*c == '[') {
            int i = 1;
            while (i) {
                curr += *c;
                c++;
                if (*c == '[') {
                    i++;
                }
                if (*c == ']') {
                    i--;
                }
            }
            curr += *c;
            v.push_back(curr);
            curr = "";
        } else if (isdigit(*c)) {
            curr += *c;
        }
    }
    if (curr.length() > 0) {
        v.push_back(curr);
    }
    return v;
}

int compare(const string l, const string r) {
    vector<string> left = get_vector(l);
    vector<string> right = get_vector(r);
    for (unsigned int i = 0; i < left.size(); i++) {
        if (i >= right.size()) {
            return 1;
        }
        if (left[i][0] != '[' && right[i][0] != '[') {
            if (stoi(left[i]) == stoi(right[i])) {
                continue;
            }
            return (stoi(left[i]) < stoi(right[i])) ? -1 : 1;
        }
        if (left[i][0] == '[' && right[i][0] == '[') {
            int list_order = compare(left[i], right[i]);
            if (list_order == 0) {
                continue;
            }
            return list_order;
        }
        if (left[i][0] != '[' && right[i][0] == '[') {
            return compare("[" + left[i] + "]", right[i]);
        }
        if (left[i][0] == '[' && right[i][0] != '[') {
            return compare(left[i], "[" + right[i] + "]");
        }
    }
    return (left.size() == right.size()) ? 0 : -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int res = 0, i = 0;
    string s1, s2;
    while (!cin.eof()) {
        getline(cin, s1);
        getline(cin, s2);
        if (compare(s1, s2) < 0) {
            res += i / 2 + 1;
        }
        i += 2;
        getline(cin, s1);
    }
    cout << res;
    return 0;
}
