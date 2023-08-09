#include <iostream>
using namespace std;
int main() {

    int n;
    int num = 2; //Determinamos num desde 2

    cout << "Ingresa un numero: ";
    cin >> n;

    cout << "Numeros primos del 1 al " << n << ":" << endl;

    while (num <= n) {
        bool esPrimo = true;
        int i = 2;

        //Comprobar si el numero es primo
        while (i * i <= num) {
            if (num % i == 0) {
                esPrimo = false;
                break;
            }
            i= i + 1;
        }

        //Imprimir el numero primo
        if (esPrimo) {
            cout << num << " ";
        }

        num++;
    }

    return 0;
}