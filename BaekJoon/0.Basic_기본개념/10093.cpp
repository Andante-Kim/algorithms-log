// 입력값 10^9 이상이면 long long 쓰기

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long a, b;

    cin >> a >> b;
    long long n1 = min(a, b);
    long long n2 = max(a, b);

    if (n1 == n2 || n1 + 1 == n2) cout << 0 << '\n';
    else {
        cout << n2 - n1 - 1 << '\n';
        for (long long i = n1 + 1; i < n2; i++) cout << i << ' ';
    }

    return 0;
}