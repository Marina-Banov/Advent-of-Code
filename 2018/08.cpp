#include <bits/stdc++.h>
#include <fstream>

using namespace std;

typedef struct node {
	int nChildren, nMetadata, value;
	vector<node> children;
	vector<unsigned int> references;
} Node;

int partOne(ifstream& file) {
    stack<pair<int, int>> data;
    int nChildren, nMetadata, result = 0, tmp;
    file >> nChildren >> nMetadata;
    pair<int, int> root(nChildren, nMetadata);
    data.push(root);
    while (!data.empty()) {
        for (int i = 0; i < data.top().first; ++i) {
            file >> nChildren >> nMetadata;
            pair<int, int> root(nChildren, nMetadata);
            if (!nChildren) {
                data.top().first--;
                for (int j = 0; j < nMetadata; ++j) {
                    file >> tmp;
                    result += tmp;
                }
                break;
            }
            data.push(root);
        }
        if (data.top().first) {
            continue;
        }
        for (int j = 0; j < data.top().second; ++j) {
            file >> tmp;
            result += tmp;
        }
        data.pop();
        if (!data.empty()) {
            data.top().first--;
        }
    }
    return result;
}

void partTwoCreate(Node& root, ifstream& file) {
    int n, m, tmp;
    file >> n >> m;
    root.nChildren = n;
    root.nMetadata = m;
    root.value = 0;
    if (!root.nChildren) {
        for (int j = 0; j < root.nMetadata; ++j) {
            file >> tmp;
            root.value += tmp;
        }
        return;
    }
    for (int i = 0; i < root.nChildren; ++i) {
        Node p;
        partTwoCreate(p, file);
        root.children.push_back(p);
    }
    for (int j = 0; j < root.nMetadata; ++j) {
        file >> tmp;
        root.references.push_back(tmp-1);
    }
}

int partTwoTraverse(Node& root) {
	if (!root.value) {
		for (unsigned int r : root.references) {
			if (r >= root.children.size()) {
				continue;
            }
			root.value += partTwoTraverse(root.children[r]);
		}
	}
	return root.value;
}

int partTwo(ifstream& file) {
    file.seekg(ios::beg);
    Node root;
    partTwoCreate(root, file);
    return partTwoTraverse(root);
}

int main() {
    ifstream file("input");

    cout << partOne(file) << endl;
    cout << partTwo(file) << endl;
    return 0;
}
