//EJERCICIO 5
//Mientras el numero sea mayor que cero sumar los digitos del numero
#include <iostream>
using namespace std;

int main() {
    int numero, suma = 0, digito;
    //ingresar datos
    cout << "Ingrese un numero: ";
    cin >> numero;
    //Verificacion que el nunmero sera meyor que 0
    while (numero > 0) {
        digito = numero % 10;
        suma += digito;
        numero /= 10;
    }
    //En caso que el numero sea menor que 0, suma = 0
    cout << "La suma de los digitos es: " << suma << endl;

    return 0;
}