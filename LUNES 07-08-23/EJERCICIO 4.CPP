//EJERCICIO 4
//Calcular si un año es bisiesto
#include <iostream>
using namespace std;
int main() {
    int anio;
    //Ingreso del año
    cout << "Ingrese un año: ";
    cin >> anio;

    //Verificar si el año es divisible por 4, 100, 400
    if ((anio % 4 == 0 && anio % 100 != 0) || anio % 400 == 0) {
        cout << anio << " es un año bisiesto." <<endl;
    } else {
        cout << anio << " no es un año bisiesto." <<endl;
    }

    return 0;
}