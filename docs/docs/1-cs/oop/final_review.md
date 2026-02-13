# ZJU 期末复习

面向期末题的相似知识点聚类

#### 构造顺序
（1）main函数以外的对象，全局类定义后直接定义的类对象
（2）main函数内的对象
（3）父类构造
（4）子类类成员
（5）子类构造
析构顺序相反

#### 什么时候生成默认构造函数？
如果已经有构造函数，编译器不会生成默认构造函数
没有的时候也不一定会生成 需要用才生成

#### 重载规则
不能重载的有：
- 作用域操作符::
- 条件操作符?:（应该是问号表达式？）
- 点操作符、类成员指针
- 预处理符号#

只能重载为友元不能成员函数：
- <<和>>
原因是成员函数重载，只能带一个参数，lhs必须是成员自身

但是流操作符左边是cin或cout，重载为友元函数时，可以比成员函数多说明一个形参做lhs

重载和重写都是多态：
重载：运行时多态
重写：编译时多态

static和virtual只能有一个

析构函数不能带参数

#### 子类和父类指针

- 子类指子类：
	如果子类覆盖了父类的成员变量和成员函数，则访问子类的
	没有覆盖的就访问父类的
- 父类指针可以直接指向子类
- 如果不是virtual：访问父类有的成员变量和函数（其实没有的也能，需要一些写法）
	如果是virtual：访问的是子类重写过的版本
- 父类没有的子类新函数就访问不到（由类型大小控制）
- 子类指针不能直接指向父类，需要进行类型转换

#### static_cast和dynamic_cast
- static cast可以父到子，可以子到父，不可以无继承关系的两个类
- dynamic cast不允许父到子（因为不知道子类多了哪些实现，返回空指针），在父类里面有virtual function的时候允许子到父，没有virtual function就不能做。要求父类必须是多态类
- reinterpret cast可以无继承关系的两个类
- const cast只用来remove const


#### 引用
什么时候必须用常引用（const &）：引用型参数应当在能定义为const的情况下尽量定义为const。

使用引用的主要原因：
程序能够修改调用函数中的数据对象
通过传递引用而不是整个数据对象，可以提高程序的运行速度

|   |   |   |
|---|---|---|
||只使用传递过来的值而不修改|需要修改传递过来的值|
|内置数据类型（小型结构）|按值传递|指针传递|
|数组|指针传递|指针传递|
|较大的结构）|指针或引用|指针或引用|
|类/对象|引用传递|引用传递|

引用和指针的区别：
可以把引用理解成一个常量指针，因此引用声明时就必须初始化，一经声明不能再和其它对象绑定。

Copy constructor must pass its first argument by reference


#### 类内静态成员的初始化
const static可以在类内直接初始化，非const static成员需要在类外初始化。

可以调用默认初始化A::n，自动初始化为0。此时调用默认构造不能用n()，否则认为是个函数。或者带初始值初始化A::n(9)

static和const
- 没有static就是const的说法

const的几种形式
```C++
const int& fun(int& a); // 修饰返回值 
int& fun(const int& a); // 修饰形参 
int& fun(int& a) const {} // const成员函数
```

const返回值：是修饰返回值引用类型的时候，为了避免返回值被修改的情况

返回值是引用的函数，这个引用必然不是临时对象的引用，一定是成员变量或者函数参数。（只要参数不需要修改一定加上const）

const参数必须传签名后带const的函数：要把this指针变成const

怎样构成重载
- 不重载的
	```C++
	const int& fun(int& a); // 参数列表没有变 
	int& fun(const int a); // 因为是值传递，不是const的也能type conversion
	```


- 重载的：只看参数列表变没变
```C++
	int& fun(const int& a); // 因为是变量传递，要求检查参数的const，是参数列表变了 
	int& fun(int& a) const {} // 因为隐含参数this的const与否不一样，也是参数列表变了
```
​

#### inline function
代替宏的一种操作，在编译阶段把所有函数名替换成inline function的实现
比函数的优点：不用频繁进栈出栈
比宏的优点：有类型检查，能写多行，能操作类的私有成员
inline关键字只有出现在函数的定义而不是声明前时才有用。
静态绑定 Static Binding 。能够明确运行的是哪个类的方法时会发生静态绑定 。发生在编译时刻，所以又叫早绑定
动态绑定Dynamic Binding 。出现多态，编译器不能明确到底使用哪个类的方法时发生动态绑定 。发生在运行时刻，所以又叫晚绑定 。只有存在 virtual 旦通过指针访问时，才会发生动态绑定

static binding 编译时
```C++
class Animal { 
public: 
	void eat() { 
		cout << "Animal eats" << endl; 
	} 
}; 
class Dog : 
public Animal { 
public: 
	void eat() { 
		cout << "Dog eats" << endl; 
	} 
};
```

dynamic binding 运行时
```C++
class Animal { 
public: 
	virtual void eat() { 
		cout << "Animal eats" << endl; 
	} 
}; 
class Dog : 
public Animal { 
public: 
	void eat() { 
	cout << "Dog eats" << endl; 
	} 
};
```
​

在下面的情况下，构造函数会被调用：
- 对于全局对象，在main()两数运行之前，或者在同一个编译单元内定义的任一函数或对象 被使用之前。在同一个编译单元内，它们的构造两数按照声明的顺序初始化。
- 对于 static local variables， 在第一次运行到它的声明的时候.
- 对于 automatic storage duration 的对象，在其声明被运行时。
- 对于 dynamic storage duration 的对象，在其用 new 表达式创建时。

#### 智能指针

```C++
std::unique_ptr<T> //独占资源所有权的指针。 
std::shared_ptr<T> //共享资源所有权的指针。 
std::weak_ptr<T> //共享资源的观察者，需要和std::shared_ptr 一起使用，不影响资源的生命周期。
```

使用裸指针
所以默认参数是和虚表无关与当前类型有关吗
是的 默认参数不进虚表
→ upcasting的时候

#### upcasting
- 基类指针指子类
- 默认参数是基类的
- 基类的virtual函数，调用子类的
- 基类的virtual函数在下面全都是virtual
- 基类的const和子类非const不是一个函数
- 基类非virtual，用基类指针调调的是基类的
- 基类非virtual，用子类指针调调的是子类的
- 基类中子类不存在函数，子类能调基类的。优先用子类的type conversion
- static在全局初始化后才能用