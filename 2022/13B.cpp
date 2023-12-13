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

int get_order(vector<string> v, string s) {
    return find(v.begin(), v.end(), s) - v.begin() + 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<string> packets;
    while (!cin.eof()) {
        string s;
        getline(cin, s);
        if (s.size() > 0) {
            packets.push_back(s);
        }
    }
    packets.push_back("[[2]]");
    packets.push_back("[[6]]");
    sort(packets.begin(), packets.end(), [](string a, string b){
        return compare(a, b) < 0;
    });
    cout << get_order(packets, "[[2]]") * get_order(packets, "[[6]]");
    return 0;
}
