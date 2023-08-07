//EJERCICIO 7
#include <iostream>
using namespace std;
int main()
{
    int num1, num2;
    //Leer dos numeros de entrada
    cout << "Ingresa el primer numero: ";
    cin >> num1;
    cout << "Ingresa el segundo numero: ";
    cin >> num2;

    //Calcular el MCD
    while (num2 != 0)
    {
        int resto = num2;
        num2 = num1 % num2;
        num1 = resto;
    }

    //Mostrar el resultado
    cout << "El maximo comun divisor es: " << num1 << endl;

    return 0;
}