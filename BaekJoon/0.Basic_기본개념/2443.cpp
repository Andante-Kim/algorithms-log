#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;

    for(int i = n - 1; i > -1; i--){
        for(int t = n - i; t > 1; t--) cout << ' ';
        for(int l = 0; l < 2*i+1; l++) cout << "*";
        cout << '\n';
    }

    return 0;
}