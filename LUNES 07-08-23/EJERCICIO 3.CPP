//EJERCICIO 3
//Calcular el área del triangulo
#include <iostream>
using namespace std;
int main(){
    float base, altura, area;
    //Definir los datos
    cout <<"Ingresar la base del triangulo: ";
    cin>>base;
    cout<<"Ingresa laa altura del triangulo: ";
    cin>>altura;

    //calcular el area
    area = (base*altura)/2;
    //Mostrar datos
    cout<<"El area del triangulo es: "<<area;
    return 0;
}