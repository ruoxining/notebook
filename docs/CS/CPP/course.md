# Courses 听课

## 关于CS106B和CS106L
CS106B偏简单，相当于ZJU的数据结构+C++的STL用法一块讲，另外再讲一些FDS的算法。
CS106L是专门讲C++进阶特性的。

因为在听CS106B之前学过FDS，CS106B花一天速通了一下，重复内容有点多，截下了一幅图。
![](STL.png)


CS106L提供的C++学习路线图
![](C++roadmap.png)


## ZJU课程

### 课程参考资料
[CPP Reference](https://en.cppreference.com/w/)
[Standard  C++](https://isocpp.org/)
[CppCon](https://www.youtube.com/user/CppCon)

### 上课心得
我跟的是cx老师的班，应该是教得最好的一档orz 
但是上课内容仍不能覆盖作业和期末的内容，觉得听课内容只能起到一个骨架作用，课后需要花上课2至3倍的时间自学自己整理笔记，多读多写代码，不然期末会遇到没见过的特性，会有点惨orz（像我一样）

###  面向对象四大特性
- 抽象
- 封装
- 继承
- 多态

### 类和对象/构造函数和析构函数
#### class 与 struct 的比较
- 类是C++对C中结构的扩展
- C语言中的struct是数据成员集合，C++中的类是数据成员和成员函数的集合
- 类是一种构造数据类型
- 类将数据和与之关联的数据封装在一起，形成一个整体，具有良好的外部接口可以防止数据未经授权的访问，提供了模块之间的独立性。

#### 类的结构：数据成员和成员函数
##### 类的声明格式
```
class Name
{
	public:
		public_data;
		public_functions;
	protected:
		protected_data;
		protected_functions;
	private:
		private_data;
		private_functions;
}
```

- private是类的私有部分，只能由本类的成员函数访问，来自外部的任何访问都是非法的。
- public是类的共有部分，对外完全开放，可以由外部任意访问。
- protected是类的保护部分，可以由本类和本类的派生类的成员函数访问，其它访问都是非法的。

##### 习惯
- 类声明格式的三个部分不一定全都有，但至少有其中的一个部分。
- 一般将数据成员声明为私有成员，成员函数声明为共有成员。
- private处于类中的第一部分时，private关键字可以省略。
- 数据成员可以是任何数据类型，但不能用auto regitser或extern进行声明。
- 不能在类声明中给数据成员赋值，只有在类对象定义之后才能给数据成员赋值。

#### 类外定义
返回类型 类名::成员函数名（参数表）
{
	// 函数体
}

#### 内联函数和外联函数
- 内联函数是定义在类体里的成员函数，即该函数的函数体放在类体里。编译时会直接用函数定义替换调用代码，提升运行速度。内联函数像定义优化了的宏。
- 外联函数是说明在类体里，定义在类体外的函数。只要在函数定义时前面加上inline就可以变成内联函数，必须和函数体放在一起。
- 内联函数可以加inline也可以不加inline。

#### 对象
可以把相同数据结构和相同操作集的对象看作属于同一类。对象是类的实例。

##### 对象的定义
- 可以直接在声明类的同时定义（全局变量），也可以类名+定义。
- 只声明类不声明对象时不分配存储空间，声明对象后才分配存储空间。

##### 对象中成员的访问
对象名.数据成员名（是 对象名.类名::成员名 的缩写）
对象名.成员函数名（参数表）
```cpp
class Sample
{
    public:
        int k;
        int geti(){return i;}
        int getj(){return j;}
        int getk(){return k;}
    
    private:
        int i;
    
    protected:
        int j;
};

int main()
{
    Sample a;
    a.i;        // 非法
    a.j:        // 非法
    a.k;        // 合法
}
```

#### 类的作用域
- 一个类的所有成员都在类的作用域中，一个类的任何成员可以访问该类的其他成员。
- 一个类的成员函数可以不受限制地访问该类的成员，在类的外部就不行。

#### 构造函数与析构函数
类的构造函数是类的一个特殊成员函数，没有返回类型（不是void），可以有参数，函数名和类名一样。当创建类的一个新对象时，自动调用构造函数，完成初始化工作。

### Namespace
#### 什么是namespace？
是单一的全局名字空间。防止在一个空间中相同的名字引起冲突。
例子：
```cpp
namespace myown1
{
	string user_name = "myown1";
}

namespace myown2
{
	string user_name = "myown2";
}

int main()
{
	// using namespace myown1; 
	cout << "\\n" << "Hello, "
	<< myown1::user_name
	<< "...and goodbye!\\n"

	cout << "\\n" << "Hello, "
	<< myown2::user_name
	<< "...and goodbye!\\n"

	return 0;
}
```

关键词using将一个名字空间变为可见，不会覆盖当前的namespace。

### 继承与派生类
- 继承：保持已有类的特性而构造新类的过程。被继承的类称为基类/父类。
- 派生：在已有类的基础上新增自己的特性而产生新类的过程。派生出的类称为派生类。

|目的|代码的重用和代码的扩充|
|---|---|
|继承种类|单继承/多继承|
|继承内容|除构造函数/析构函数/私有成员外的所有成员|

##### 继承的访问控制
派生类继承了基类中除构造函数和析构函数之外的所有成员。派生类的成员包括：
- 继承基类的成员
- 派生类定义时声明的成员

从已有类派生出新类时，可以在派生类内完成以下几种功能：
- 增加新的数据成员
- 增加新的成员函数
- 重新定义基类中已有的成员函数
- 可以改变现有成员的属性

声明一个派生类的一般格式
```cpp
class 派生类名:继承方式 基类名
{
		// 派生类新增的数据成员和成员函数
};
```

三种继承方式
```cpp
class employee: public person
{};

// default
class employee: private person
{};

class employee: protected person
{};
```

基类成员在派生类中的访问属性

|在基类中的访问属性|继承方式|在派生类中的访问属性|解释|
|---|---|---|---|
|private|public|inaccessible|基类中private的对象在类外当然不可访问|
|private|private|inaccessible||
|private|protected|inaccessible||
|public|public|public|基类不管|
|public|private|private||
|public|protected|protected||
|protected|public|protected|权限会被继承方式缩小而不会放大|
|protected|private|private||
|protected|protected|protected||

派生类对基类的访问规则
- 内部访问：由派生类中新增成员对基类继承来的成员的访问。
- 对象访问：在派生类外部，通过派生类的对象对从基类继承来的成员的访问。

|基类成员|private成员|public成员|protected成员|
|---|---|---|---|
|内部访问|不可访问|可访问|可访问|
|对象访问|不可访问|不可访问|不可访问|

私有继承举例
```cpp
class Point
{
	public:
		void InitP(float x = 0, float y = 0)
		{
			this->X = x;
			this->Y = y;
		}
		void Move(float offX, float offY)
		{
			X += offX;
			Y += offY;
		}
		float GetX() const{return X;}
		float GetY() const{return Y;}
	private:
		float X, Y;
};

class Rectangle: private Point // 派生类声明
{
	public: //新增外部接口
		void InitR(float x, float y, float w, float h)
		{
			InitR(x, y);
			W = w;
			H = h;
		} // 
		void Move(float xOff, float yOff)
		{
			Point::
		}
}
```


