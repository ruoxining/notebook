# 继承 Inheritance

is_a 逻辑
```cpp
#include <...>

class B{
public:
	int f(int i) {cout << "f(int)"; return i+1; }
};

class D: public B{
public:
	using B::f;  // 保证不会覆盖掉B中的f
	double f(double d)  
}

```

访问控制：private和protected继承
```cpp
int a;
class X{
	int a;
};

class XX: public X{
	void 
}
```

虚继承

向上转型
```cpp
Base *pb = &derived;
```

这个不一定可行
```cpp
Shape s = c;   // object slicing
s = c;         // copy assignment
```

virtual 关键字

说明一个 non-static member function 是一个 virtual function

行为可以被派生类override（重写/覆盖）

Base::vf，子类有一个名字、参数列表
```cpp
struct Base {
	virtual void print() {cout << "Base\\n"; }
};

struct Derived: public Base{
	void 
}
```

virtual call 只关心对象的类型，call对应类的函数

只要调用虚函数就是虚调用
```cpp
virtual void do_draw() = 0;   // 是纯虚函数，不必有实现，但是可以有实现
```

如果有至少一个纯虚函数，是抽象类，抽象类不能用于声明成员，只能作为基类

final 关键字：不能被重写，不能被继承

虚函数的通常实现：virtual table (vtable)

static vtable 虚表
```cpp
class Der: public Base {
public:
	virtual arbiturary_return_type vir0{}
	virtual arbiturary_return_type vir1{}
	virtual arbiturary_return_type vie2{}
}
```

它的虚函数表
```cpp
FunctionPtr Der::__vtable[5]{
	&Der::vir0, &Der::vir1, &Der::vir2, &Base::vir3, &Base::vir4
}
```

好像实际上相当于这么call的
```cpp
b.__vptr[3](b);
```

template和OOP的区别，语义不一样。