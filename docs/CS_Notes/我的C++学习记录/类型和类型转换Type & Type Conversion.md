## Type info 库
```cpp
#include <typeinfo>
```

简介
- 和sizeof这类操作符一样，typeid是c++的关键字之一
- typeid操作符返回的结果是名为type_info的标准库类型的对象的引用（在头文件typeinfo中定义）
- c++并没有规定typeid实现标准，各个编译器可能会不一样
- 编译器会为每一种typeid操作的类型生成一份保存在数据段的type_info数据
- 每种类型的type_info数据长度依赖于类型名称，至少9个字节

用法
- \== 和!=操作
```cpp
#include <iostream>
#include <typeinfo>

struct Base{};
struct Derived: Base {};
struct Poly_Base {virtual void Member(){}};
struct Poly_Derived: Poly_Base {};

typedef int my_int_type;

int main()
{
	std::cout << std::boolalpha;
	
	std::cout << "int vs my_int_type: ";
	std::cout << (typeid(int) == typeid(my_int_type)) << '\\n';

	std::cout << "Base vs Derived: ";
	std::cout << (typeid(Base) == typeid(Derived)) << '\\n'; // 输出false

	Base* pbase = new Derived;

}
```

- name操作：获取type的名字，这个名字是c风格的字符串指针

```cpp
#include <iostream>
#include <typeinfo>

struct Base{}
struct Derived: Base{};
template <class T>
void swap(T a, T b){
	std::cout << "T is: " << typeid(T).name() << '\\n';
	T temp = a;
	a = b;
	b = temp;
}

int main(){
	
	int i;
	int* ptr;
	std::cout << "int is: " << typeid(int).name() << '\\n';
	std::cout << "  i is: " << typeid(i).name() << '\\n';

}
```

参考
[C++中的typeInfo用法总结_非晚非晚的博客-CSDN博客](https://blog.csdn.net/QLeelq/article/details/116054654)

## 类型转换
### const_cast
```cpp
const_cast<new_type>(expression);
```

- returns a value of type new_type
- 将对象的常量性转除（cast away the constness）

```cpp
#include <iostream>
 
struct type
{
    int i;
 
    type(): i(3) {}
 
    void f(int v) const
    {
        // this->i = v;                 // compile error: this is a pointer to const
        const_cast<type*>(this)->i = v; // OK as long as the type object isn't const
    }
};
 
int main()
{
    int i = 3;                 // i is not declared const
    const int& rci = i;
    const_cast<int&>(rci) = 4; // OK: modifies i
    std::cout << "i = " << i << '\\n';
 
    type t; // if this was const type t, then t.f(4) would be undefined behavior
    t.f(4);
    std::cout << "type::i = " << t.i << '\\n';
 
    const int j = 3; // j is declared const
    [[maybe_unused]]
    int* pj = const_cast<int*>(&j);
    // *pj = 4;      // undefined behavior
 
    [[maybe_unused]]
    void (type::* pmf)(int) const = &type::f; // pointer to member function
    // const_cast<void(type::*)(int)>(pmf);   // compile error: const_cast does
                                              // not work on function pointers
}
```

### dynamic_cast
```cpp
dynamic_cast<new_type>(expression);
```

- returns a value of type new_type
- 安全向下转型”safe downcasting”
- 用来决定对象是否属于继承体系中的某个类型
- exclusively for handling polymorphism

```cpp
#include <iostream>
 
struct V
{
    virtual void f() {} // must be polymorphic to use runtime-checked dynamic_cast
};
 
struct A : virtual V {};
 
struct B : virtual V
{
    B(V* v, A* a)
    {
        // casts during construction (see the call in the constructor of D below)
        dynamic_cast<B*>(v); // well-defined: v of type V*, V base of B, results in B*
        dynamic_cast<B*>(a); // undefined behavior: a has type A*, A not a base of B
    }
};
 
struct D : A, B
{
    D() : B(static_cast<A*>(this), this) {}
};
 
struct Base
{
    virtual ~Base() {}
};
 
struct Derived: Base
{
    virtual void name() {}
};
 
int main()
{
    D d; // the most derived object
    A& a = d; // upcast, dynamic_cast may be used, but unnecessary
 
    [[maybe_unused]]
    D& new_d = dynamic_cast<D&>(a); // downcast
    [[maybe_unused]]
    B& new_b = dynamic_cast<B&>(a); // sidecast
 
    Base* b1 = new Base;
    if (Derived* d = dynamic_cast<Derived*>(b1); d != nullptr)
    {
        std::cout << "downcast from b1 to d successful\\n";
        d->name(); // safe to call
    }
 
    Base* b2 = new Derived;
    if (Derived* d = dynamic_cast<Derived*>(b2); d != nullptr)
    {
        std::cout << "downcast from b2 to d successful\\n";
        d->name(); // safe to call
    }
 
    delete b1;
    delete b2;
}
```

### reinterpret_cast
```cpp
reinterpret_cast<new_type>(expression)
```

- returns a value of type new_type
- 意图执行低级转型，实际动作取决于编译器→不可移植
- 不常见
- most dangerous cast

```cpp
#include <cassert>
#include <cstdint>
#include <iostream>
 
int f() { return 42; }
 
int main()
{
    int i = 7;
 
    // pointer to integer and back
    std::uintptr_t v1 = reinterpret_cast<std::uintptr_t>(&i); // static_cast is an error
    std::cout << "The value of &i is " << std::showbase << std::hex << v1 << '\\n';
    int* p1 = reinterpret_cast<int*>(v1);
    assert(p1 == &i);
 
    // pointer to function to another and back
    void(*fp1)() = reinterpret_cast<void(*)()>(f);
    // fp1(); undefined behavior
    int(*fp2)() = reinterpret_cast<int(*)()>(fp1);
    std::cout << std::dec << fp2() << '\\n'; // safe
 
    // type aliasing through pointer
    char* p2 = reinterpret_cast<char*>(&i);
    std::cout << (p2[0] == '\\x7' ? "This system is little-endian\\n"
                                 : "This system is big-endian\\n");
 
    // type aliasing through reference
    reinterpret_cast<unsigned int&>(i) = 42;
    std::cout << i << '\\n';
 
    [[maybe_unused]] const int &const_iref = i;
    // int &iref = reinterpret_cast<int&>(
    //     const_iref); // compiler error - can't get rid of const
    // Must use const_cast instead: int &iref = const_cast<int&>(const_iref);
}
```

### static_cast
```cpp
static_cast<new_type>(expression)
```

- returns a value of type new_type
- 强转
- static_cast is the first cast should attempt to use.
- can cast through inheritance hierarchies.
```C++
struct B {}; 
struct D : B { 
	B b; 
}; D d; 
B& br1 = d; 
B& br2 = d.b; 
static_cast<D&>(br1); // OK: lvalue denoting the original d object 
static_cast<D&>(br2); // UB: the b subobject is not a base class subobject
```