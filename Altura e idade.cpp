#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int idade = 0;
    float altura = 0;
    
    cin >> idade;
    cout << "A sua idade eh: " << idade << endl;
    
    cin >> altura;
    cout << fixed << setprecision(2) << "A sua altura eh: " << altura << endl;
    
    return 0;
}
