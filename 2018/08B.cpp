#include <bits/stdc++.h>

using namespace std;

typedef struct node {
	int n_children, n_metadata, value;
	vector<node> children; 
	vector<unsigned int> references;
} Node;

int calculate_value(Node& r) {
	if (!r.value) {
		for (unsigned int i = 0; i < r.references.size(); ++i) {
			if (r.references[i] >= r.children.size()) {
				continue;
            }
			r.value += calculate_value(r.children[r.references[i]]);
		}
	}
	return r.value;
}

void create(Node& r) {
    int n, m, tmp;
    cin >> n >> m;
    r.n_children = n;
    r.n_metadata = m;
    r.value = 0;
    if (!r.n_children) {
        for (int j = 0; j < r.n_metadata; ++j) {
            cin >> tmp;
            r.value += tmp;
        }
        return;
    }
    for (int i = 0; i < r.n_children; ++i) {
        Node p;
        create(p);
        r.children.push_back(p);
    }
    for (int j = 0; j < r.n_metadata; ++j) {
        cin >> tmp;
        r.references.push_back(tmp-1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    Node r;
    create(r);
    cout << calculate_value(r);

	return 0;
}
