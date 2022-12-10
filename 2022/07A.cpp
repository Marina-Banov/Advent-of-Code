#include <bits/stdc++.h>

using namespace std;


class TreeNode {
    private:
        string _name;
        int _size;
        TreeNode* _parent;
        vector<TreeNode*> _children;

    public:
        TreeNode(string name, int size, TreeNode* parent) {
            _name = name;
            _size = size;
            _parent = parent;
        }

        TreeNode* get_parent() { return _parent; }

        void add_child(TreeNode* child) {
            _children.push_back(child);
        }
        TreeNode* get_child(string name) {
            for (auto child : _children) {
                if (child -> _name == name) {
                    return child;
                }
            }
            return NULL;
        }

        int calc_sum(vector<int>* dir_sizes) {
            for (auto child : _children) {
                _size += child -> calc_sum(dir_sizes);
            }
            if (_children.size() > 0) {
                dir_sizes -> push_back(_size);
            }
            return _size;
        }
};


void build_tree(TreeNode* root) {
    string command;
    string dir;
    getline(cin, command);

    while (command.length() > 0) {
        if (command == "$ ls") {
            while (command.length() > 0) {
                getline(cin, command);
                if (command[0] == '$' || command.length() == 0) {
                    break;
                }
                stringstream ss(command);
                string s;
                vector<string> parts;
                while (getline(ss, s, ' ')) {
                    parts.push_back(s);
                }
                TreeNode* child = new TreeNode(
                    parts[1],
                    parts[0] == "dir" ? 0 : stoi(parts[0]),
                    root
                );
                root -> add_child(child);
            }
        } else {
            dir = command.substr(5);
            if (dir == "..") {
                root = root -> get_parent();
            } else if (dir != "/") {
                root = root -> get_child(dir);
            }
            getline(cin, command);
        }
    }

    while (root -> get_parent()) {
        root = root -> get_parent();
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    TreeNode* root = new TreeNode("/", 0, NULL);
    build_tree(root);

    vector<int> dir_sizes;
    root -> calc_sum(&dir_sizes);
    int res = 0;
    for (auto dir : dir_sizes) {
        if (dir <= 100000) {
            res += dir;
        }
    }
    cout << res;
    return 0;
}
