#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int vec[3];
    char answer[5] = {'D', 'C', 'B', 'A', 'E'};
    int a, b, c, d;
    
    for(int i = 0; i < 3 ; i++){
        cin >> a >> b >> c >> d;
        vec[i] = a + b + c + d;
    }

    for(int k = 0; k < 3; k++) cout << answer[vec[k]] << '\n';
}