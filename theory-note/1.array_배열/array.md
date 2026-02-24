# 0. 정의와 성질
**배열** : 메모리 상에 원소를 연속하게 배치한 자료 구조

배열의 성질
1. O(1)에 k번쨰 원소를 확인/변경 가능
    * 배열은 메모리 상에 원소를 연속하게 배치한 자료구조 -> k번째 원소의 위치를 바로 계산할 수 있음
2. 추가적으로 소모되는 메모리의 양(=overhead)가 거의 없음
3. 메모리 상에 데이터들이 붙어있어서 캐시 적중률(Cache hit rate)가 높음
4. 메모리 상에 연속한 구간을 잡아야 해서 할당에 제약이 걸림


# 1. 기능과 구현

* 임의의 위치에 있는 원소를 확인/변경 = O(1)
* 원소를 끝에 추가 = O(1)
* 마지막 원소를 제거 = O(1)
* 임의의 위치에 원소를 추가/임의 위치의 원소 제거 = O(N)
    ```C++
    #include <bits/stdc++.h>
    using namespace std;

    void insert(int idx, int num, int arr[], int& len){

    }

    void erase(int idx, int arr[], int& len){
        
    }

    int main(void){
        int arr[10] = {10, 50, 40, 30, 70, 20};
        int len = 6;
        insert(3, 60, arr, len);  // 10 50 40 60 30 70 20
        erase(4, arr, len); // 10 50 40 60 70 20
    }
    ```

# 2. STL vector

# 3. 연습 문제