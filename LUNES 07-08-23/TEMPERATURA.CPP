//EJERCICIO 2
//Convertir temperatura en grados Celsius a fahrenhei
#include <iostream>
using namespace std;
int main (){
    float temp, fah;
    //Ingresar datos
    cout<<"INgresat una temperatura en grados celsios: ";
    cin>>temp;
    //Calcular la formula
    fah=(temp*9/5)+32;
    //Mostrar la temperatura
    cout<<"La temperatura en fahrenhei "<<fah<<endl;
    return 0;
}