#include <bits/stdc++.h>

using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> vec;
    int a;
    for(int i = 0; i < 5; i++){
        cin >> a;
        vec.push_back(a);
    }
    
    sort(vec.begin(), vec.end());
    cout << accumulate(vec.begin(), vec.end(), 0)/5 << '\n';
    cout << vec[2];

    return 0;
}