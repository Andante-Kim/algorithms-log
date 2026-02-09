#include <bits/stdc++.h>

using namespace std;
int main() {
    vector<int> vec;
    int tall;
    int a, b;
    int sum;

    for(int i = 0; i < 9; i++){
        cin >> tall;
        vec.push_back(tall);
    }
    sort(vec.begin(), vec.end());

    for(a = 0; a < 9; a++){
        for(b = a+1; b < 9; b++){
            sum = accumulate(vec.begin(), vec.end(), 0) - vec[a] - vec[b];
            if(sum == 100) break;
        }
        if(sum == 100){
            vec.erase(vec.begin() + b);
            vec.erase(vec.begin() + a);
            for(int k = 0; k < 7; k++) cout << vec[k] << '\n';
            break;
        }
    }

    return 0;
}