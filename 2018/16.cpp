#include <bits/stdc++.h>
#include <fstream>

using namespace std;

typedef struct {
    string before, op, after;
} Sample;

array<int,4> addr(array<int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] + registers[rb];
    return registers;
}

array<int,4> addi(array<int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] + vb;
    return registers;
}

array<int,4> mulr(array<int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] * registers[rb];
    return registers;
}

array<int,4> muli(array<int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] * vb;
    return registers;
}

array<int,4> banr(array<int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] & registers[rb];
    return registers;
}

array<int,4> bani(array<int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] & vb;
    return registers;
}

array<int,4> borr(array<int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] | registers[rb];
    return registers;
}

array<int,4> bori(array<int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] | vb;
    return registers;
}

array<int,4> setr(array<int,4> registers, int ra, int rc) {
    registers[rc] = registers[ra];
    return registers;
}

array<int,4> seti(array<int,4> registers, int va, int rc) {
    registers[rc] = va;
    return registers;
}

array<int,4> gtir(array<int,4> registers, int va, int rb, int rc) {
    registers[rc] = va > registers[rb];
    return registers;
}

array<int,4> gtri(array<int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] > vb;
    return registers;
}

array<int,4> gtrr(array<int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] > registers[rb];
    return registers;
}

array<int,4> eqir(array<int,4> registers, int va, int rb, int rc) {
    registers[rc] = va == registers[rb];
    return registers;
}

array<int,4> eqri(array<int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] == vb;
    return registers;
}

array<int,4> eqrr(array<int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] == registers[rb];
    return registers;
}

int partOne(vector<Sample>& samples, bool instructions[16][16]) {
    int result = 0;
    for (Sample s : samples) {
        if (s.before.length() == 0) {
            break;
        }
        array<int, 4> before;
        for (int i = 0; i < 4; ++i) {
            before[i] = s.before[9 + 3 * i] - '0';
        }
        int offset = stoi(s.op) >= 10;
        int a = s.op[2 + offset] - '0';
        int b = s.op[4 + offset] - '0';
        int c = s.op[6 + offset] - '0';
        array<int, 4> after;
        for (int i = 0; i < 4; ++i) {
            after[i] = s.after[9 + 3 * i] - '0';
        }
        vector<int> map;
        if (addr(before, a, b, c) == after) map.push_back( 0);
        if (addi(before, a, b, c) == after) map.push_back( 1);
        if (mulr(before, a, b, c) == after) map.push_back( 2);
        if (muli(before, a, b, c) == after) map.push_back( 3);
        if (banr(before, a, b, c) == after) map.push_back( 4);
        if (bani(before, a, b, c) == after) map.push_back( 5);
        if (borr(before, a, b, c) == after) map.push_back( 6);
        if (bori(before, a, b, c) == after) map.push_back( 7);
        if (setr(before, a, c)    == after) map.push_back( 8);
        if (seti(before, a, c)    == after) map.push_back( 9);
        if (gtir(before, a, b, c) == after) map.push_back(10);
        if (gtri(before, a, b, c) == after) map.push_back(11);
        if (gtrr(before, a, b, c) == after) map.push_back(12);
        if (eqir(before, a, b, c) == after) map.push_back(13);
        if (eqri(before, a, b, c) == after) map.push_back(14);
        if (eqrr(before, a, b, c) == after) map.push_back(15);
        for (int m : map) {
            instructions[stoi(s.op)][m] = true;
        }
        result += (map.size() >= 3);
    }
    return result;
}

void check(bool instructions[16][16], array<int, 16>& map, int i, bool checkRow) {
    int count = 0, index = -1;
    for (int j = 0; j < 16; ++j) {
        if (checkRow && instructions[i][j] || !checkRow && instructions[j][i]) {
            count++;
            index = j;
        }
        if (count > 1) {
            return;
        }
    }
    if (count == 0) {
        return;
    }
    if (checkRow) {
        map[i] = index;
        for (int j = 0; j < 16; ++j) {
            instructions[j][index] = false;
        }
    } else {
        map[index] = i;
        for (int j = 0; j < 16; ++j) {
            instructions[index][j] = false;
        }
    }
}

array<int, 16> getMap(bool instructions[16][16]) {
    array<int, 16> map;
    for (int k = 0; k < 16; k++) {
        for (int i = 0; i < 16; ++i) {
            check(instructions, map, i, true);
            check(instructions, map, i, false);
        }
    }
    return map;
}

int partTwo(vector<Sample>& samples, bool instructions[16][16]) {
    array<int, 16> map = getMap(instructions);
    array<int, 4> registers = {0};
    for (Sample s : samples) {
        if (s.before.length() != 0) {
            continue;
        }
        int offset = stoi(s.op) >= 10;
        int a = s.op[2 + offset] - '0';
        int b = s.op[4 + offset] - '0';
        int c = s.op[6 + offset] - '0';
        switch (map[stoi(s.op)]) {
            case  0: registers = addr(registers, a, b, c); break;
            case  1: registers = addi(registers, a, b, c); break;
            case  2: registers = mulr(registers, a, b, c); break;
            case  3: registers = muli(registers, a, b, c); break;
            case  4: registers = banr(registers, a, b, c); break;
            case  5: registers = bani(registers, a, b, c); break;
            case  6: registers = borr(registers, a, b, c); break;
            case  7: registers = bori(registers, a, b, c); break;
            case  8: registers = setr(registers, a, c   ); break;
            case  9: registers = seti(registers, a, c   ); break;
            case 10: registers = gtir(registers, a, b, c); break;
            case 11: registers = gtri(registers, a, b, c); break;
            case 12: registers = gtrr(registers, a, b, c); break;
            case 13: registers = eqir(registers, a, b, c); break;
            case 14: registers = eqri(registers, a, b, c); break;
            case 15: registers = eqrr(registers, a, b, c); break;
        }
    }
    return registers[0];
}

int main() {
    ifstream file("input");
    vector<Sample> samples;
    Sample s;
    bool instructions[16][16] = {false};
    while (true) {
        getline(file, s.before);
        if (s.before.length() <= 1) {
            break;
        }
        getline(file, s.op);
        getline(file, s.after);
        samples.push_back(s);
        file.ignore(1, '\n');
    }
    file.ignore(1, '\n');
    s.before = "";
    s.after = "";
    while (getline(file, s.op)) {
        samples.push_back(s);
    }

    cout << partOne(samples, instructions) << endl;
    cout << partTwo(samples, instructions) << endl;
    return 0;
}
