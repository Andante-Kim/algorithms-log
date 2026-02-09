// 9498번 : 시험 성적
#include <bits/stdc++.h>
using namespace std;
int main() {
    int score;
    cin >> score;

    if(score > 89) cout << 'A' << '\n';
    else if(score > 79) cout << 'B' << '\n';
    else if(score > 69) cout << 'C' << '\n';
    else if(score > 59) cout << 'D' << '\n';
    else cout << 'F';
}  