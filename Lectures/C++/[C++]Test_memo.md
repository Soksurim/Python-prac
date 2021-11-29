# **test_memo**

___

### **복사, 이동 생성자 사용 예시**
```cpp
#include <iostream>
#include <cstring>
using namespace std;

class A
{
    int a;

public:
    A(int n) : a{n}
    {
        printf("값 저장됨. a : %d\n", n);
    }
    A(A &v) : a{v.a}
    {
        printf("복사 생성자 호출됨. a : %d\n", v.a);
    }
    A(A &&v) : a{v.a}
    {
        printf("이동 생성자 호출됨. a : %d\n", v.a);
    }
    ~A()
    {
        printf("객체 삭제\n");
    }
    void p()
    {
        printf("프린트 a : %d\n", this->a);
    }
    A r(A a)
    {
        return a;
    }
};

int main()
{
    A a(1);      // 값 저장됨.
    A b(a);      // 복사 생성자 호출됨. a : 1
    A c(b.r(a)); // 복사 생성자 호출됨. a : 1
                 // 이동 생성자 호출됨. a : 1

    c.p(); // 프린트 a : 1

    // 객체 삭제
    // 객체 삭제
    // 객체 삭제
    // 객체 삭제
    return (0);
}
```

___

### **# 동일한 객체로 얕은 복사시 데이터 깨짐**
[ref_link](https://hombody.tistory.com/317)
```cpp
#include <iostream>
using namespace std;
#include "VecF.h"
int main()
{
    float a[3] = {1, 2, 3};
    VecF v1(3, a); // 1, 2, 3을 저장하는 벡터
    VecF v2{v1};   // v1을 복사
    v1.print();
    cout << endl; // [ 1 2 3 ]
    v2.print();
    cout << endl; // [ 1 2 3 ]

    VecF t = v1.add(v2);
    v1 = t;
    v1.print(); // [ 2 4 6 ]

    v1 = v1.add(v2); // v1을 참조하며 v1 객체를 수정 -> 깨짐.
    v1.print();      // [ 2.38953e-038 2.38778e-038 9 ]

    return 0;
}
```

___


```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char const *argv[])
{
    int *p2;
    int p[] = {1, 2, 3};
    p2 = new int[5];
    memset(p2, 0, sizeof(int) * 5);
    memcpy(p2, p, sizeof(int) * 3);

    while (*p2)
    {
        cout << *(p2++) << endl; // 1 2 3
    }
    return 0;
}
```