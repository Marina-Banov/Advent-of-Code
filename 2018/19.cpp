#include <bits/stdc++.h>
#include <fstream>

using namespace std;

typedef struct {
    string s;
    int a, b, c;
} instruction;

void addr(array<int, 6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] + registers[rb];
}

void addi(array<int, 6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] + vb;
}

void mulr(array<int, 6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] * registers[rb];
}

void muli(array<int, 6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] * vb;
}

void banr(array<int, 6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] & registers[rb];
}

void bani(array<int, 6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] & vb;
}

void borr(array<int, 6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] | registers[rb];
}

void bori(array<int, 6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] | vb;
}

void setr(array<int, 6>& registers, int ra, int rc) {
    registers[rc] = registers[ra];
}

void seti(array<int, 6>& registers, int va, int rc) {
    registers[rc] = va;
}

void gtir(array<int, 6>& registers, int va, int rb, int rc) {
    registers[rc] = va > registers[rb];
}

void gtri(array<int, 6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] > vb;
}

void gtrr(array<int, 6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] > registers[rb];
}

void eqir(array<int, 6>& registers, int va, int rb, int rc) {
    registers[rc] = va == registers[rb];
}

void eqri(array<int, 6>& registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] == vb;
}

void eqrr(array<int, 6>& registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] == registers[rb];
}

int partOne(int ip, vector<instruction>& instructions) {
    array<int, 6> registers = {0};
    int startIp = registers[ip];
    while (startIp < (int) instructions.size() && startIp > -1) {
        registers[ip] = startIp;
        instruction i = instructions[startIp];
             if (i.s == "addr") addr(registers, i.a, i.b, i.c);
        else if (i.s == "addi") addi(registers, i.a, i.b, i.c);
        else if (i.s == "mulr") mulr(registers, i.a, i.b, i.c);
        else if (i.s == "muli") muli(registers, i.a, i.b, i.c);
        else if (i.s == "banr") banr(registers, i.a, i.b, i.c);
        else if (i.s == "bani") bani(registers, i.a, i.b, i.c);
        else if (i.s == "borr") borr(registers, i.a, i.b, i.c);
        else if (i.s == "bori") bori(registers, i.a, i.b, i.c);
        else if (i.s == "setr") setr(registers, i.a, i.c     );
        else if (i.s == "seti") seti(registers, i.a, i.c     );
        else if (i.s == "gtir") gtir(registers, i.a, i.b, i.c);
        else if (i.s == "gtri") gtri(registers, i.a, i.b, i.c);
        else if (i.s == "gtrr") gtrr(registers, i.a, i.b, i.c);
        else if (i.s == "eqir") eqir(registers, i.a, i.b, i.c);
        else if (i.s == "eqri") eqri(registers, i.a, i.b, i.c);
        else if (i.s == "eqrr") eqrr(registers, i.a, i.b, i.c);
        startIp = registers[ip];
        startIp++;
    }
    return registers[0];
}

int partTwo(int ip, vector<instruction>& instructions) {
    return 0;
}

int main() {
    ifstream file("input");
    int ip;
    vector<instruction> instructions;
    instruction i;
    file >> i.s >> ip;
    while (file >> i.s >> i.a >> i.b >> i.c) {
        instructions.push_back(i);
    }

    cout << partOne(ip, instructions) << endl;
    cout << partTwo(ip, instructions) << endl;
    return 0;
}
