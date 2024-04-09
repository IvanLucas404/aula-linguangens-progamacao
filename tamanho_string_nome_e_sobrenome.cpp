#include <iostream>
#include <string>
using namespace std;

int main() {
    string nome, sobrenome;
    int tamanho;
    
    cin >> nome;
    cin >> sobrenome;
    
    tamanho = nome.length() -1;
    
    cout << sobrenome << ", " << nome[0] << "," << nome[tamanho] << endl;
    


    return 0;
}