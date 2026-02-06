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


# 3. 코드 작성 팁