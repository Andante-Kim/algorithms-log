#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, time;
    vector<int> times;
    int y = 0, m = 0;

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> time;
        times.push_back(time);
    }

    for(int k = 0; k < n; k++){
        y += times[k] / 30 * 10 + 10;
        m += times[k] / 60 * 15 + 15;
    }

    if(y == m) cout << "Y M " << y;
    else if(y < m) cout << "Y " << y;
    else cout << "M " << m;

    return 0;
}
