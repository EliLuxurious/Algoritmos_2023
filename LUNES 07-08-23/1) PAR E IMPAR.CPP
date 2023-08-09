//EJERCICIO 1
//Determinar si un número par o impar
#include <iostream>
using namespace std;
int main(){
    int num;
    //Ingresar un numero
    cout<<"Escribir un numero: ";
    cin>>num;
    //Comparar si el numero es par
    if(num%2 ==0){
        cout<<"El numero es par";
    }
    else{
        cout<<"El numero no es par";
    }
    return 0;
}