#include <bits/stdc++.h>

using namespace std;

array<int,4> addr (array <int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] + registers[rb];
    return registers;
}

array<int,4> addi (array <int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] + vb;
    return registers;
}

array<int,4> mulr (array <int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] * registers[rb];
    return registers;
}

array<int,4> muli (array <int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] * vb;
    return registers;
}

array<int,4> banr (array <int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] & registers[rb];
    return registers;
}

array<int,4> bani (array <int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] & vb;
    return registers;
}

array<int,4> borr (array <int,4> registers, int ra, int rb, int rc) {
    registers[rc] = registers[ra] | registers[rb];
    return registers;
}

array<int,4> bori (array <int,4> registers, int ra, int vb, int rc) {
    registers[rc] = registers[ra] | vb;
    return registers;
}

array<int,4> setr (array <int,4> registers, int ra, int rc) {
    registers[rc] = registers[ra];
    return registers;
}

array<int,4> seti (array <int,4> registers, int va, int rc) {
    registers[rc] = va;
    return registers;
}

array<int,4> gtir (array <int,4> registers, int va, int rb, int rc) {
    registers[rc] = (va > registers[rb]) ? 1 : 0;
    return registers;
}

array<int,4> gtri (array <int,4> registers, int ra, int vb, int rc) {
    registers[rc] = (registers[ra] > vb) ? 1 : 0;
    return registers;
}

array<int,4> gtrr (array <int,4> registers, int ra, int rb, int rc) {
    registers[rc] = (registers[ra] > registers[rb]) ? 1 : 0;
    return registers;
}

array<int,4> eqir (array <int,4> registers, int va, int rb, int rc) {
    registers[rc] = (va == registers[rb]) ? 1 : 0;
    return registers;
}

array<int,4> eqri (array <int,4> registers, int ra, int vb, int rc) {
    registers[rc] = (registers[ra] == vb) ? 1 : 0;
    return registers;
}

array<int,4> eqrr (array <int,4> registers, int ra, int rb, int rc) {
    registers[rc] = (registers[ra] == registers[rb]) ? 1 : 0;
    return registers;
}

array <int, 16> define_pairs(bool instructions[16][16]);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    array <int, 4> registers_before, registers_after;
    bool instructions[16][16] = {false};
    int n_op, a, b, c;
    string status_before, op, status_after;

    while(1) {
        getline(cin, status_before);
        if (status_before.length() <= 1) {
            break;
        }

        int j = 9;
        for (int i = 0; i < 4; ++i) {
            registers_before[i] = status_before[j] - '0';
            j += 3;
        }

        getline(cin, op);
        n_op = stoi(op);
        a = op[2 + ((n_op >= 10) ? 1 : 0)] - '0';
        b = op[4 + ((n_op >= 10) ? 1 : 0)] - '0';
        c = op[6 + ((n_op >= 10) ? 1 : 0)] - '0';

        getline(cin, status_after);
        j = 9;
        for (int i = 0; i < 4; ++i) {
            registers_after[i] = status_after[j] - '0';
            j += 3;
        }

        if (addr(registers_before, a, b, c) == registers_after) instructions[n_op][ 0] = true;
        if (addi(registers_before, a, b, c) == registers_after) instructions[n_op][ 1] = true;
        if (mulr(registers_before, a, b, c) == registers_after) instructions[n_op][ 2] = true;
        if (muli(registers_before, a, b, c) == registers_after) instructions[n_op][ 3] = true;
        if (banr(registers_before, a, b, c) == registers_after) instructions[n_op][ 4] = true;
        if (bani(registers_before, a, b, c) == registers_after) instructions[n_op][ 5] = true;
        if (borr(registers_before, a, b, c) == registers_after) instructions[n_op][ 6] = true;
        if (bori(registers_before, a, b, c) == registers_after) instructions[n_op][ 7] = true;
        if (setr(registers_before, a, c)    == registers_after) instructions[n_op][ 8] = true;
        if (seti(registers_before, a, c)    == registers_after) instructions[n_op][ 9] = true;
        if (gtir(registers_before, a, b, c) == registers_after) instructions[n_op][10] = true;
        if (gtri(registers_before, a, b, c) == registers_after) instructions[n_op][11] = true;
        if (gtrr(registers_before, a, b, c) == registers_after) instructions[n_op][12] = true;
        if (eqir(registers_before, a, b, c) == registers_after) instructions[n_op][13] = true;
        if (eqri(registers_before, a, b, c) == registers_after) instructions[n_op][14] = true;
        if (eqrr(registers_before, a, b, c) == registers_after) instructions[n_op][15] = true;

        getline(cin, status_before);
    }    

    array <int, 16> op_pairs = define_pairs(instructions);
    
    getline(cin,op);
    registers_after = {0};
    while (getline(cin, op)) {
        n_op = stoi(op);
        a = op[2 + ((n_op >= 10) ? 1 : 0)] - '0';
        b = op[4 + ((n_op >= 10) ? 1 : 0)] - '0';
        c = op[6 + ((n_op >= 10) ? 1 : 0)] - '0';
        switch (op_pairs[n_op]) {
            case  0: registers_after = addr(registers_after, a, b, c); break;
            case  1: registers_after = addi(registers_after, a, b, c); break;
            case  2: registers_after = mulr(registers_after, a, b, c); break;
            case  3: registers_after = muli(registers_after, a, b, c); break;
            case  4: registers_after = banr(registers_after, a, b, c); break;
            case  5: registers_after = bani(registers_after, a, b, c); break;
            case  6: registers_after = borr(registers_after, a, b, c); break;
            case  7: registers_after = bori(registers_after, a, b, c); break;
            case  8: registers_after = setr(registers_after, a, c   ); break;
            case  9: registers_after = seti(registers_after, a, c   ); break;
            case 10: registers_after = gtir(registers_after, a, b, c); break;
            case 11: registers_after = gtri(registers_after, a, b, c); break;
            case 12: registers_after = gtrr(registers_after, a, b, c); break;
            case 13: registers_after = eqir(registers_after, a, b, c); break;
            case 14: registers_after = eqri(registers_after, a, b, c); break;
            case 15: registers_after = eqrr(registers_after, a, b, c); break;
        }
    }

    cout << registers_after[0];
    return 0;
}

array <int, 16> define_pairs(bool instructions[16][16]) {
    array <int, 16> pairs;
    int i, j, h = 0;
    pair<int,int> count;

    while (h < 16) {
        for (i = 0; i < 16; ++i) {
            count.first = 0;
            for (j = 0; j < 16; ++j) {
                if (instructions[i][j]) {
                    count.first++;
                    count.second = j;
                }
                if (count.first > 1) {
                    break;
                }
            }

            if (count.first == 1) {
                h++;
                pairs[i] = count.second;
                for (j = 0; j < 16; ++j) {
                    instructions[j][count.second] = false;
                }
            }
            
            count.first = 0;
            
            for (j = 0; j < 16; ++j) {
                if (instructions[j][i]) {
                    count.first++;
                    count.second = j;
                }
                if (count.first > 1) {
                    break;
                }
            }

            if (count.first == 1) {
                h++;
                pairs[count.second] = i;
                for (j = 0; j < 16; ++j) {
                    instructions[count.second][j] = false;
                }
            }
        }
    }
    return pairs;
}
