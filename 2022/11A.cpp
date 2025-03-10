#include <bits/stdc++.h>

using namespace std;

#define N_ROUNDS 20


typedef struct {
    vector<int> items;
    char op;
    int worry_factor;
    int test, test_true, test_false;
    int inspected = 0;
} Monkey;


void read_input(vector<Monkey> *monkeys) {
    Monkey m;
    int i;
    while (scanf("Monkey %d: ", &i) == 1) {
        string str(100, ' ');
        scanf("Starting items: %100[0-9, ]s", &str[0]);
        stringstream ss(str);
        string s;
        while (getline(ss, s, ',')) {
            m.items.push_back(stoi(s));
        }
        scanf(" Operation: new = old %c %s ", &m.op, &s[0]);
        try {
            m.worry_factor = stoi(s);
        } catch (const invalid_argument& ia) {
            m.op = '^';
            m.worry_factor = 2;
        }
        scanf("Test: divisible by %d ", &m.test);
        scanf("If true: throw to monkey %d ", &m.test_true);
        scanf("If false: throw to monkey %d ", &m.test_false);
        monkeys->push_back(m);
        m.items.clear();
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<Monkey> monkeys;
    read_input(&monkeys);
    
    for (int i = 0; i < N_ROUNDS; i++) {
        for (auto& monkey : monkeys) {
            for (auto item: monkey.items) {
                if (monkey.op == '+') {
                    item += monkey.worry_factor;
                } else if (monkey.op == '*') {
                    item *= monkey.worry_factor;
                } else {
                    item *= item;
                }
                item /= 3;
                int next_monkey = item % monkey.test ? monkey.test_false : monkey.test_true;
                monkeys[next_monkey].items.push_back(item);
            }
            monkey.inspected += monkey.items.size();
            monkey.items.clear();
        }
    }

    sort(
        monkeys.begin(), monkeys.end(),
        [](Monkey m1, Monkey m2) { return m1.inspected > m2.inspected; }
    );
    cout << monkeys[0].inspected * monkeys[1].inspected;
    return 0;
}
