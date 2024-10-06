#include <iostream>
using namespace std;

int main() {
    // Declaración de variables enteras
    int a = 10;
    int b = -5;
    int ua = 100;
    long int la = 1234567890;
    short int sa = 200;
    
    // Declaración de variables de punto flotante
    float f = 3.14f;
    double d = 3.14159;
    double ld = 2.718281828459045;

    // Declaración de variables de caracteres
    char c = 'A';
    char uc = 255;

    // Declaración de variables booleanas
    bool flagTrue = true;
    bool flagFalse = false;

 

    // Impresión de las variables
    cout << "int a: " << a << endl;
    cout << "int b: " << b << endl;
    cout << "unsigned int ua: " << ua << endl;
    cout << "long la: " << la << endl;
    cout << "short sa: " << sa << endl;
    cout << "float f: " << f << endl;
    cout << "double d: " << d << endl;
    cout << "double ld: " << ld << endl;
    cout << "char c: " << c << endl;
    cout << "unsigned char uc: " << (int)uc << endl; // casteo para mostrar el valor numérico de uc
    cout << "bool flagTrue: " << flagTrue << endl;
    cout << "bool flagFalse: " << flagFalse << endl;

    return 0;
}
