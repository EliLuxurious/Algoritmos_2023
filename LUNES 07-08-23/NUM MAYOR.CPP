#include <iostream>
using namespace std;
int main()
{
    int num1, num2, num3;

    //Leer tres numeros de entrada
    cout << "Ingresa el primer numero: ";
    cin >> num1;
    cout << "Ingresa el segundo numero: ";
    cin >> num2;
    cout << "Ingresa el tercer numero: ";
    cin >> num3;

    //Determinar el numero mayor
    if (num2 > num1 && num2 > num3)
    {
        cout << "El mayor numero es: " << num2;
    }
    else if (num3 > num1 && num3 > num2)
    {
        cout << "El mayor numero es: " << num3;
    }
    else
    {
        cout << "El mayor numero es: " << num1;
    }

    return 0;
}