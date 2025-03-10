#include <bits/stdc++.h>

using namespace std;

void addr (array <int,4> registers_a, int ra, int rb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra] + registers_a[rb];
    if (registers_a == registers_b) {
        instructions[0] = true;
    }
}

void addi (array <int,4> registers_a, int ra, int vb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra] + vb;
    if (registers_a == registers_b) {
        instructions[1] = true;
    }
}

void mulr (array <int,4> registers_a, int ra, int rb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra] * registers_a[rb];
    if (registers_a == registers_b) {
        instructions[2] = true;
    }
}

void muli (array <int,4> registers_a, int ra, int vb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra] * vb;
    if (registers_a == registers_b) {
        instructions[3] = true;
    }
}

void banr (array <int,4> registers_a, int ra, int rb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra] & registers_a[rb];
    if (registers_a == registers_b) {
        instructions[4] = true;
    }
}

void bani (array <int,4> registers_a, int ra, int vb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra] & vb;
    if (registers_a == registers_b) {
        instructions[5] = true;
    }
}

void borr (array <int,4> registers_a, int ra, int rb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra] | registers_a[rb];
    if (registers_a == registers_b) {
        instructions[6] = true;
    }
}

void bori (array <int,4> registers_a, int ra, int vb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra] | vb;
    if (registers_a == registers_b) {
        instructions[7] = true;
    }
}

void setr (array <int,4> registers_a, int ra, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = registers_a[ra];
    if (registers_a == registers_b) {
        instructions[8] = true;
    }
}

void seti (array <int,4> registers_a, int va, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = va;
    if (registers_a == registers_b) {
        instructions[9] = true;
    }
}

void gtir (array <int,4> registers_a, int va, int rb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = (va > registers_a[rb]) ? 1 : 0;
    if (registers_a == registers_b) {
        instructions[10] = true;
    }
}

void gtri (array <int,4> registers_a, int ra, int vb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = (registers_a[ra] > vb) ? 1 : 0;
    if (registers_a == registers_b) {
        instructions[11] = true;
    }
}

void gtrr (array <int,4> registers_a, int ra, int rb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = (registers_a[ra] > registers_a[rb]) ? 1 : 0;
    if (registers_a == registers_b) {
        instructions[12] = true;
    }
}

void eqir (array <int,4> registers_a, int va, int rb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = (va == registers_a[rb]) ? 1 : 0;
    if (registers_a == registers_b) {
        instructions[13] = true;
    }
}

void eqri (array <int,4> registers_a, int ra, int vb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = (registers_a[ra] == vb) ? 1 : 0;
    if (registers_a == registers_b) {
        instructions[14] = true;
    }
}

void eqrr (array <int,4> registers_a, int ra, int rb, int rc, array <int,4> registers_b, bool instructions[]) {
    registers_a[rc] = (registers_a[ra] == registers_a[rb]) ? 1 : 0;
    if (registers_a == registers_b) {
        instructions[15] = true;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    array <int, 4> registers_before, registers_after;
    int n_op, a, b, c;
    int h = 0;
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

        bool instructions[16] = {false};
        
        addr(registers_before, a, b, c, registers_after, instructions);    
        addi(registers_before, a, b, c, registers_after, instructions);        
        mulr(registers_before, a, b, c, registers_after, instructions);    
        muli(registers_before, a, b, c, registers_after, instructions);    
        banr(registers_before, a, b, c, registers_after, instructions);    
        bani(registers_before, a, b, c, registers_after, instructions);    
        borr(registers_before, a, b, c, registers_after, instructions);    
        bori(registers_before, a, b, c, registers_after, instructions);    
        setr(registers_before, a, c, registers_after, instructions);    
        seti(registers_before, a, c, registers_after, instructions);    
        gtir(registers_before, a, b, c, registers_after, instructions);    
        gtri(registers_before, a, b, c, registers_after, instructions);    
        gtrr(registers_before, a, b, c, registers_after, instructions);    
        eqir(registers_before, a, b, c, registers_after, instructions);    
        eqri(registers_before, a, b, c, registers_after, instructions);    
        eqrr(registers_before, a, b, c, registers_after, instructions);    
        
        int calc = 0;
        for (int j = 0; j < 16; ++j) {
            if (instructions[j]) {
                calc++;    
            }
        }

        if (calc >= 3) {
            h++;
        }
        getline(cin, status_before);
    }

    while(getline(cin, op));
    
    cout << h;
    return 0;
}
