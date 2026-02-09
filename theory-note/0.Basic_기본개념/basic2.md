자료 출처: [바킹독 알고리즘: 기초 코드 작성 요령2](https://blog.encrypted.gg/923)

# 1. STL과 함수 인자
___

## 함수인자

### C언어의 함수 호출 방식

1. Call by Value (값에 의한 호출) : 함수를 호출할 때 실 인자의 값만 복사하여 전달하는 방식
    *  원리: 함수 내부에서 매개변수를 위한 별도의 메모리 공간이 할당된다.
    *  원본 수정: 함수 내부에서 값을 변경해도 호출한 쪽의 원본 변수에는 아무런 영향이 없다.
    *  특징: 데이터의 안전성이 보장되지만, 구조체처럼 큰 데이터를 복사할 경우 메모리 낭비가 발생할 수 있다.

2. Call  by Reference (참조에 의한 호출) : 함수를 호출할 때 변수의 **주소값(Address)** 을 전달하는 방식 (C언어에서는 포인터를 이용해 구현)
    * 원리: 함수 내부에서 포인터 변수를 통해 원본 메모리에 직접 접근한다.
    * 원본 수정: 함수 내부에서 발생한 변경 사항이 원본 변수에 그대로 반영된다.
    * 특징: 복사 비용이 적어 효율적이지만, 원본 데이터가 의도치 않게 수정될 위험이 있다.
```C
#include <stdio.h>

// Call by Value: 값을 복사함
void swapByValue(int a, int b){
    int temp = a;
    a = b;
    b = temp;
    // 함수 종료 시 복사본 a, b는 소멸됨
}

// Call by Reference: 주소를 전달함
void swapByReference(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
    // 원본 메모리 주소에 접근하여 직접 수정함
}

int main() {
    int x = 10, y = 20;

    // 1. 값 전달 방식 호출
    swapByValue(x, y);
    printf("After swapByValue: x = %d, y = %d\n", x, y);
    // 결과: x = 10, y = 20 (변경 없음)

    // 2. 주소 전달 방식 호출
    swapByReference(&x, &y);
    printf("After swapByReference: x = %d, y = %d\n", x, y);
    // 결과: x = 20, y = 10 (변경 완료)

    return 0;
}
```

## 참조자(Reference)

C언어는 원본 변수에 접근하기 위해 반드시 **주소값**을 전달하고, 함수 내부에서 포인터로 이를 역참조해야 한다.

C++에서는 **참조자(Reference)** 라는 개념이 도입되었다. 참조자는 기존 변수에 대한 **별명(Alias)** 과 같다.
1. 참조자의 정의와 선언: 참조자는 변수의 메모리 공간에 또 다른 이름을 붙이는 것이다. 참조자를 통해 값을 변경하면 원본 변수의 값도 함께 변경된다.
    * 선언 방식: `자료형 &참조자명 = 변수명;`
    * 핵심: 참조자는 별도의 메모리 공간을 차지하지 않는 것처럼 동작하며, 선언된 순간부터 원본 변수와 동일시된다.
2. 참조자의 3가지 필수 제약 조건
    1. 반드시 선언과 동시에 초기화해야 함: 대상을 지정하지 않은 참조자는 존재할 수 없다. (`int &ref;` (X))
    2. NULL 참조가 불가능함: 어떠한 변수도 가리키지 않는 상태를 가질 수 없다.
    3. 참조 대상을 변경할 수 없음: 한 번 특정 변수의 별명이 되면, 죽을 때까지 그 변수만 가리킨다. (재할당 불가)
3. [코드 예시]
    ```C
    #include <iostream>

    int main() {
        int target = 100;
        int &ref = target; // target의 별명인 ref 생성

        // 1. 값의 공유
        std::cout << "target: " << target << ", ref: " << ref << std::endl;

        // 2. 참조자를 통한 값 변경
        ref = 200;
        std::cout << "수정 후 target: " << target << std::endl; // 200 출력

        // 3. 주소값 비교
        std::cout << "target 주소: " << &target << std::endl;
        std::cout << "ref 주소: " << &ref << std::endl; // 두 주소는 동일함

        return 0;
    }
    ```
4. 참조자 활용: Call by Reference
    * 함수 매개변수에 참조자를 사용하면 복사 오버헤드 없이 원본 데이터를 직접 다룰 수 있다. 포인터처럼 주소를 넘기기 위해 `&`를 붙이거나 `*`를 쓸 필요가 없어 코드가 매우 깔끔해진다.
    ```C
    void increment(int &n) {
        n++; // 포인터 연산 없이 직접 접근
    }

    int main() {
        int val = 10;
        increment(val); // 일반 변수처럼 전달
        // val은 이제 11
    }
    ```
5. 결론
    * C++에서는 성능과 안전성을 위해 가급적 참조자를 우선적으로 사용하는 것을 권장한다. 하지만 참조 대상이 바뀌어야 하거나 `NULL`을 표현해야 하는 특수한 상황(예: 자료구조 구현 등)에서는 여전히 포인터가 필요하다.

## STL(Standard Template Library) - vector
STL은 C++에서 제공되는 라이브러리로, 다양한 알고리즘과 자료구조가 구현되어 있어 필요한 자료구조를 직접 구현할 필요없이 STL에서 가져다 써서 사용할 수 있다.

vector STL: 
* 원래 C++에서는 배열을 선언할 때 크기를 명시해야 하고, 무조건 해당 크기 안에서만 사용해야 함
* 반면, vector는 일종의 가변 배열로 크기를 마음대로 늘렸다 줄였다 할 수 있다. 
* (+) vector 헤더에 선언되어 있다.

### STL을 함수 인자로 넘길 때
```C++
void func1(vector<int> v) {
    v[10] = 7;
}

int main(void) {
    vector<int> v(100);
    func1(v);
    cout << v[10];
}
// 출력: 0
```
STL도 구조체랑 비슷하게 함수 인자를 실어 보내면 복사본을 만들어서 보내기 때문에 func1 함수에서 바꾼건 원본에 영향을 주지 않는다.

> ! 기억하기 ! : STL을 그냥 쌩으로 함수 인자에 넣으면 복사해서 보낸다

---

```C++
bool cmp1(vector<int> v1, vector<int> v2, int idx) {
    return v1[idx] > v2[idx];
}
// 시간 복잡도: O(N)
```
v1, v2를 인자로 실어서 보낼 때 원본으로 복사본을 만들어야 한다. v1, v2의 크기가 N일 때, N개의 원소를 하나하나 복사하는 과정은 O(N)이 든다. 따라서 이 함수의 시간복잡도는 의도하지 않게 O(N)이 된다.
___
```C++
bool cmp2(vector<int>& v1, vector<int>& v2, int idx) {
    return v1[idx] > v2[idx];
}
// 시간 복잡도: O(1)
```
cmp2 함수에서는 v1, v2의 type을 vector의 reference로 만들엇다. 그러면 cmp2가 호출될 때 복사본을 따로 만들지 않고 참조 대상의 주소 정보만 넘어가므로 시간복잡도는 O(1)이 된다.

# 2. 표준 입출력
* C: scanf/printf
    * C++ string을 처리할 수 없음 : C에서는 문자열을 char*로 다루는데 이보다 C++ string이 월등히 편하다. 따라서 만약 scanf/printf를 쓰면서 C++ string도 사용하고 싶다면 일단 char * 로 입력을 받고 string으로 형 변환을 해서 원하는 작업을 다 끝낸 후에 c_str() 메소드를 이용해 출력하면 된다.
* C++: cin/cout
```C++
int main(void){
    string s = "IWantGoHome..";
    printf("s is %s\n", s);
}
/***result***
s is ?
*************/
```
```C
int main(void) {
    char a[10];
    printf("input: ");
    scanf("%s", a);
    string s(a);  // 혹은 string s = a;
    printf("a is %s\n", a);
    printf("a is %s\n", s.c_str());
}

/*** reslt***
input : test
a is test
a is test
*************/
```
---
scanf, cin을 쓸 때 주의할 점: 모두 공백을 포함한 문자열을 입력할 떄, 공백 앞까지만 입력을 받는다.
* 해결책1. scanf 옵션 사용: scanf에서 줄바꿈(\n)이 나오기 전까지 입력을 받는다는 걸 명시
    ```C
    char al[10];
    scanf("%[^\n]", al);
    ```
* 해결책2. gets 함수(보안상의 이유로 C++14 이상에서는 제거됨)
    ```C
    char a2[10];
    gets(a2);
    puts(a2);
    ```
* 해결책3. getline 함수: 가장 깔끔. 대신 type이 C++ string이어야 함
    ```C
    string s;
    getline(cin, s);
    cout << s;
    ```
> 공백이 포함된 문자열을 받아야 할 떄 단순히 scanf나 cin을 쓰면 안된다!
___
cin/cout에서 주의할 점: scanf/printf와 다르게 cin/cout은 입출력으로 인한 시간초과를 막기 위해서 `ios::sync_with_stdio(0)`, `cin.tie(0)`이라는 두 명령을 실행 시켜야 한다. 이를 해두지 않으면 입/출력 양이 많을 때 시간초과가 날 수 있다.
* `ios::sync_with_stdio(0)`
    * 기본적으로 scanf/printf 등에서 쓰는 C stream과 cin/cout 등에서 쓰는 C++ stream은 분리되어 있다. 따라서 printf와 cout을 번갈아 사용하는 상황을 고려하여 코드의 흐름과 실제 출력이 동일하기 위해 프로그램에서는 C++ stream과 C stream을 동기화하고 있다.
    * 그런데 이 동기화 작업에도 시간이 소요되므로, 만일 C++ stream만 사용한다면 굳이 두 stream을 동기화할 필요가 없다.
    * 따라서 C++ stream만 쓸 떄 동기화를 끊어버려서 프로그램 수행 시간에서 이득을 챙길 수 있는 명령이 `sync_with_stdio(0)`(=`sync_with_stdio(false)`)이다.
    * 대신 동기화를 끊었으면 절대 cout과 printf를 섞어쓰면 안된다. 섞어쓰면 출력 결과가 꼬인다.
* `cin.tie(0)`
    * 버퍼(Buffer)
        * 정의: 버퍼는 데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역이다.
        * 작동 방식: 프로그램이 데이터를 즉시 출력 장치로 보내지 않고 버퍼에 모아두었다가, 버퍼가 가득 차거나 특정 조건(Flush)이 만족되면 한꺼번에 전송한다. 이는 시스템 콜 횟수를 줄여 성능을 향상시킨다.
    * cin.tie(0)의 역할
        * cin과 cout은 기본적으로 묶여(Tied) 있다. 즉, 입력 요청이 들어오면 출력 버퍼를 강제로 비워(Flush) 화면에 내용을 먼저 표시하도록 설계되어 있다.
        * 기본 동작: `cout << "Enter name: "; cin >> name;`상황에서 사용자가 이름을 입력하기 전, "Enter name: "이 화면에 반드시 보여야 하므로 cin은 호출될 때마다 cout의 버퍼를 비운다.
        * 문제점: 알고리즘 풀이처럼 방대한 양의 입력과 출력이 반복되는 경우, 매번 버퍼를 비우는 작업은 상당한 시간 지연을 초래한다.
        * 해결책: `cin.tie(NULL)` 또는 `cin.tie(0)` 을 사용하면 cin과 cout의 연결을 끊어 버퍼를 자동으로 비우지 않게 한다.
```C++
#include <iostream>

using namespace std;

int main() {
    // 입출력 최적화
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    // 반복적인 입출력이 발생할 때 tie를 해제하면 속도가 비약적으로 상승
    while (cin >> n >> m) {
        cout << n + m << "\n"; // endl 대신 "\n" 사용 권장
    }

    return 0;
}
```
___
*endl은 절대 쓰면 안된다..!*

endl은 개행문자("\n")을 출력하고 출력 버퍼를 비우라는 명령이다. 

알고리즘 문제를 풀경우, 어차피 저지는 프로그램이 종료될 때 출력이 어떻게 생겼는지를 가지고 채점을 진행하니까 중간 버퍼를 비우라고 명령을 줄 필요가 없다.

> 순수하게 개행 문자(\n)만 사용하자..!
---

# 3. 코드 작성 팁
## (1) 코딩 테스트와 개발은 다르다. 
* 깔끔한 코드
    ```C++
    #include <iostream>
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, x;
    std::cin >> n >> x;
    int* a= new int[n];
    for(int i = 0; i < n; i++)
        std::cin >> a[i];
    for(int i = 0; i < n; i++)
        if(a[i] < x) std::cout << a[i] << ' ';
    delete[] a;
    ```
* 코딩테스트용 코드
    ```C++
    #include <bits/stdc++.h>

    using namespace std;

    int main(){
        ios::sync_with_stdio(0);
        cin.tie(0);

        int n, x, t;
        cin >> n >> x;
        while(n--){
            cin >> t;
            if(t < x) cout << t << ' ';
        }
    }
    ```

## (2) 출력 맨 마지막 공백 혹은 줄바굼이 추가로 있어도 상관없다.
공백과 줄바꿈이 출력 맨 마지막에 추가로 있어도 정답 처리되므로, 별도로 예외처리할 필요가 없다.

## (3) 디버거는 굳이 사용하지 않아도 된다.
만일 중간 변수를 보고 싶으면 cout이나 printf로 출력을 찍어서 확인하고 디버거는 굳이 사용하지 않는 것을 권장한다.