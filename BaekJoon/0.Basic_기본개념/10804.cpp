#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b;
    vector<int> cards = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
    vector<int> temp;

    for(int i = 0; i < 10; i++){
        cin >> a >> b;
        for(int k = b - 1; k > a - 2; k--) temp.push_back(cards[k]);

        for(int t = a - 1; t < b; t++) cards[t] = temp[t - a + 1];
        temp = {};
    }

    for(int l = 0; l < 20; l++) cout << cards[l] << ' ';

    return 0;
}