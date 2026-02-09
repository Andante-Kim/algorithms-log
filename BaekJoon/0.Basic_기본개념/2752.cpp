// 2752번: 세수정렬
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c;
    int vec[3];

    cin >> a >> b >> c;
    vec[0] = a;
    vec[1] = b;
    vec[2] = c;

    sort(vec, vec+3);

    for (int i = 0; i < 3; i++) cout << vec[i] << ' ';

    return 0;
}