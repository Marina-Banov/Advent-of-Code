#include <bits/stdc++.h>

using namespace std;

void addr(array <int,6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] + registers[rb];
}

void addi(array <int,6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] + vb;
}

void mulr(array <int,6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] * registers[rb];
}

void muli(array <int,6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] * vb;
}

void banr(array <int,6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] & registers[rb];
}

void bani(array <int,6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] & vb;
}

void borr(array <int,6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] | registers[rb];
}

void bori(array <int,6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] | vb;
}

void setr(array <int,6>& registers, int ra, int rc) {
    registers[rc] = registers[ra];
}

void seti(array <int,6>& registers, int va, int rc) {
    registers[rc] = va;
}

void gtir(array <int,6>& registers, int va, int rb, int rc) {
    registers[rc] = (va > registers[rb]) ? 1 : 0;
}

void gtri(array <int,6>& registers, int ra, int vb, int rc) {
    registers[rc] = (registers[ra] > vb) ? 1 : 0;
}

void gtrr(array <int,6>& registers, int ra, int rb, int rc) {
    registers[rc] = (registers[ra] > registers[rb]) ? 1 : 0;
}

void eqir(array <int,6>& registers, int va, int rb, int rc) {
    registers[rc] = (va == registers[rb]) ? 1 : 0;
}

void eqri(array <int,6>& registers, int ra, int vb, int rc) {
    registers[rc] = (registers[ra] == vb) ? 1 : 0;
}

void eqrr(array <int,6>& registers, int ra, int rb, int rc) {
    registers[rc] = (registers[ra] == registers[rb]) ? 1 : 0;
}

typedef struct {
    string s;
    int a, b, c;
} instruction;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    array <int,6> registers = {0};
    int x;
    vector <instruction> all;
    instruction one;

    cin >> one.s >> x;
    while (cin >> one.s >> one.a >> one.b >> one.c) {
        all.push_back(one);
    }

    int start_ip = registers[x];
    while (start_ip < (int) all.size() && start_ip > -1) {
        registers[x] = start_ip;
        one = all[start_ip];
        
        if (one.s == "addr") addr(registers, one.a, one.b, one.c);
        if (one.s == "addi") addi(registers, one.a, one.b, one.c);
        if (one.s == "mulr") mulr(registers, one.a, one.b, one.c);
        if (one.s == "muli") muli(registers, one.a, one.b, one.c);    
        if (one.s == "banr") banr(registers, one.a, one.b, one.c);
        if (one.s == "bani") bani(registers, one.a, one.b, one.c);
        if (one.s == "borr") borr(registers, one.a, one.b, one.c);
        if (one.s == "bori") bori(registers, one.a, one.b, one.c);
        if (one.s == "setr") setr(registers, one.a, one.c       );    
        if (one.s == "seti") seti(registers, one.a, one.c       );    
        if (one.s == "gtir") gtir(registers, one.a, one.b, one.c);
        if (one.s == "gtri") gtri(registers, one.a, one.b, one.c);
        if (one.s == "gtrr") gtrr(registers, one.a, one.b, one.c);
        if (one.s == "eqir") eqir(registers, one.a, one.b, one.c);
        if (one.s == "eqri") eqri(registers, one.a, one.b, one.c);
        if (one.s == "eqrr") eqrr(registers, one.a, one.b, one.c);

        start_ip = registers[x];
        start_ip++;
    }

    cout << registers[0];
    return 0;
}
