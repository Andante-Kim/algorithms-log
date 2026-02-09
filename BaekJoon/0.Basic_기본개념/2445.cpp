#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;

    for(int i = 1; i < n+1; i++){
        for(int k = 0; k < i; k++) cout << '*';
        for(int t = 0; t < (n-i)*2; t++) cout << ' ';
        for(int k = 0; k < i; k++) cout << '*';
        cout << '\n';
    }
    for(int i = n - 1; i > 0; i--){
        for(int k = 0; k < i; k++) cout << '*';
        for(int t = 0; t < (n-i)*2; t++) cout << ' ';
        for(int k = 0; k < i; k++) cout << '*';
        cout << '\n';
    }


    return 0;
}