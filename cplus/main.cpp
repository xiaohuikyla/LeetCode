#include <iostream>
#include "292NimGame.h"

using namespace std;

int main(){

    int num;
    NimGame s;
    cout << "Please input the nim number:" ;
    cin >> num;
    cout << "The result is:" << s.canWinNim(num) << endl;
    return 0;
}
