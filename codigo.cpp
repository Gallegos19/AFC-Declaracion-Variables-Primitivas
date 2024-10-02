#include <iostream>
using namespace std;

int a ;
int main() {
    int a = 10;
    float b = 5.5;
    char c = 'A';
    double d = 10.99;
    bool is_valid = true;

    int valid123 = 100;
    float customFloat = 9.8;
    char validChar = 'B';
    double e4 = 4.0e3;

    // Operaciones para evitar warnings
    cout << a << " " << b << " " << c << " " << d << " " << is_valid << endl;
    cout << valid123 << " " << customFloat << " " << validChar << " " << e4 << endl;

    return 0;
}
