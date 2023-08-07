//EJERCICIO 6
//Pago mensual de una hipoteca
#include <iostream>
#include <cmath>
using namespace std;
int main(){
    float monto, interesAnual, cantidadAhos, tasaMensual, tasaInteres;
    float pagoMensual, plazo;
    cout<<"Ingresar el monto del prestamo: ";
    cin>>monto;
    cout<<"Ingresar la tasa de interes anual: ";
    cin>>interesAnual;
    cout<<"Ingresar cantidad de años: ";
    cin>>cantidadAhos;
     // Calcular la tasa de interés mensual
    tasaInteres = interesAnual;
    tasaMensual = tasaInteres / 12 / 100;

    // Calcular el número total de pagos (meses)
    plazo = cantidadAhos * 12;

    // Calcular el valor del importe a cancelar en cada periodo
    pagoMensual = monto * (tasaMensual / (1 - pow(1 + tasaMensual, -plazo)));
    cout << "El pago mensual es: " << pagoMensual << endl;
    return 0;
}