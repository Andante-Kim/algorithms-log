#include <bits/stdc++.h>

using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int num;
    vector<int> odd_num;

    for(int i = 0; i < 7; i++){
        cin >> num;
        if(num % 2 != 0) odd_num.push_back(num);
    }

    if(odd_num.size() == 0) cout << -1 << '\n';
    else{
        sort(odd_num.begin(), odd_num.end());
        cout << accumulate(odd_num.begin(), odd_num.end(), 0) << '\n';
        cout << odd_num[0] << '\n';
    }
}