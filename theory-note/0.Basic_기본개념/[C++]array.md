# C++ 배열의 기초부터 동적 배열까지

## 1. 정적 배열 (Static Array)
선언과 동시에 크기가 결정되며, 프로그램 실행 도중에는 크기를 변경할 수 없는 배열이다.
* 특징: 메모리의 스택(stack) 영역에 할당된다.
* 한계: 컴파일 타임에 크기를 정해야 하므로, 사용자 입력을 받아 크기를 결정하는 것이 불가능하거나 메모리 낭비가 심할 수 있다.
* 선언: `자료형 배열명[크기]`

## 2. 동적 배열(Dynamic Array) - `new` 연산자
프로그램 실행 중(Runtime)에 필요한 만큼 메모리를 할당받는 방식이다.
* 메커니즘: 메모리의 힙(Heap) 영역을 사용한다.
* 특징: 사용자가 원하는 시점에 메모리를 할당하고, 더 이상 필요 없을 때 직접 해제해야 한다.
* 메모리 해제: `delete[]` 연산자를 누락하면 메모리 누수(Memory Leak)가 발생한다. 

## 3. 예시 코드를 통한 비교 분석
```C++
#include <iostream>

int main() {
    // 1. 정적 배열: 크기가 5로 고정
    int staticArr[5] = {1, 2, 3, 4, 5};

    // 2. 동적 배열: 실행 중 크기 결정
    int size;
    std::cin >> size;

    int* dynamicArr = new int[size]; // 힙 영역에 할당

    for (int i = 0; i < size; i++) {
        dynamicArr[i] = i + 1;
    }

    // 할당된 메모리 해제 (필수)
    delete[] dynamicArr; 

    return 0;
}
```

## 4. 현대적 동적 배열: `std::vector`
C++ 표준 라이브러리(STL)에서 제공하는 컨테이너로, 메모리 관리의 복잡함을 자동화한 스마트한 동적 배열이다.
* 자동 리사이징: 데이터가 추가되어 공간이 부족하면 스스로 크기를 키운다.
* 자동 해제: 객체가 범위를 벗어나면 소멸자가 호출되어 메모리를 자동으로 해제한다.
* 주요 함수: 
    * `push_back()`: 맨 뒤에 요소 추가
    * `size()`: 현재 요소 개수 밭환
    * `capacity()`: 할당된 전체 메모리 공간 크기 반환
```c++
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // 1. 벡터 선언
    vector<int> vec;

    // 2. 데이터 추가
    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(30);

    // 3. 데이터 접근 및 수정
    cout << "첫 번째 요소: " << vec[0] << endl; // 배열처럼 접근 가능
    vec[1] = 25; // 값 수정

    // 4. 정보 확인
    cout << "현재 크기(size): " << vec.size() << endl;       // 3
    cout << "할당 용량(capacity): " << vec.capacity() << endl; // 할당된 공간 크기

    // 5. 전체 순회 (현대적 방식)
    cout << "전체 원소: ";
    for (int num : vec) {
        cout << num << " ";
    }
    cout << endl;

    // 6. 데이터 삭제
    vec.pop_back(); // 마지막 원소(30) 삭제
    cout << "pop_back 후 size: " << vec.size() << endl; // 2

    return 0;
}
```

## 5. 요약 및 비교
|구분|정적 배열|동적 배열(`new`)|`std::vector`|
|---|---|---|---|
|할당 영역|스택(Stack)|힙(Heap)|힙(Heap)|
|크기 결정|컴파일 타임|런타임|런타임 (가변)|
|메모리 해제|자동|수동(`delete[]`)|자동
|권장 상황|크기가 작고 고정됨|특수한 저수준 관리|일반적인 모든 상황