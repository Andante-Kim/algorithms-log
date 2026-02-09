#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;

    for(int i = n; i > 0; i--){
        for(int space = 0; space < n - i; space++) cout << ' ';
        for(int star = 2 * i - 1; star > 0; star--) cout << '*';
        cout << '\n';
    }
    for(int k = 2; k < n + 1; k++){
        for(int space_2 = n - k; space_2 > 0; space_2--) cout << ' ';
        for(int star_2 = 0; star_2 < 2 * k - 1; star_2++) cout << '*';
        cout << '\n';
    }
}