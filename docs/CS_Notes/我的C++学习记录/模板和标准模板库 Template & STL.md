# 模板Template
需求：让我们的代码独立于具体的类型工作。

我们写出一个适用于所有类型的数据结构的类或算法（函数），在真正需要使用时生成一个适用于所需类型的实例。这种编程范式称为范型编程。

模板类的写法
```cpp
template<typename T>
class Container{
	T *data;
	unsigned size, capa;
piblic:
	Container(unsigned capa = 512): data(new T[capa]){}
	~Container() {delete[] data;}
	T& operator[](unsigned index) {return data[index];}
}
```

这里template T表明它接受一个类型作为参数，名字是T。在模板的定义内部我们可以使用到这个类型变量T。

特化：根据模板生成实际的类的过程
```cpp
Container<int> ci;
Container<double> cd;
```

模板函数要怎么写
```cpp
template<typename T>
T abs(T x) {return x>0?x:-x;}
```

模板运算符重载怎么写
```cpp
template<typename T>
class Container {
	T* data;
	unsigned size = 0, capa;

public: 
	Container(unsigned capa = 512) : data(new T[capa]), capa(capa){}
	~Container(){delete[] data;}

	T& operator[](unsigned index) {return data[index];}
	const T& operator[](unsigned idnex) const {return data[index];}

	unsigned getSize() const {return size;}
	unsigned getCapa() const {return capa;}

	Container &add(T val){
	data[size++] = val;
	return *this;
	}
};

template<typename T>
ostream & operator<<(ostream& os, const Container<T>&c){
	for (unsigned i = 0; i < c.getSize(); i++){
		os << c[i] << ' ';
	return os;
	}
}
```

## Reference
[7 模板 (I) - 基本知识与 STL 使用 - 咸鱼暄的代码空间](https://xuan-insr.github.io/cpp/cpp_restart/7_template/#71-%E5%BC%95%E5%85%A5%E6%B3%9B%E5%9E%8B%E7%BC%96%E7%A8%8B)


# 可变参数模板 template<class …T>
C++11的新特性
对参数高度泛化，可以表示0到任意个任意类型的参数。

语法
```cpp
template <class ...T>  // 声明一个参数包，这个参数包中包含0到任意一个参数模板
void f(T... args);     // 在模板定义的右边，可以将参数包展开成一个一个独立参数
```

最大的难点：如何展开可变模板参数

打印参数个数：
```cpp
template<class ...T>
void f(T... args)
{
		cout << sizeof...(args) << endl;
}

f();
f(1, 2);
f(1, 2.5, "");
```

递归方式展开参数包
```cpp
#include <iostream>
using namespace std;

// 递归终止函数
void print(){
	cout << "empty" << endl;
}

// 展开函数
template<class T, class ...Args>
void print(T head, Args... rest){
	cout << "parameter" << head << endl;
	print(rest...);
}

int main(){
	print(1, 2, 3, 4);
	return 0;
}
```

上述例子会输出每一个参数，直到空时输出empty。展开参数包的函数有两个，一个是递归函数，另一个是递归终止函数，参数包Args…在展开的过程中递归调用自己，每调用一次，参数包中的参数就少一个，直到所有参数都展开为止。当没有参数时，则调用非模板函数print()终止递归过程。

终止函数也可以写成
```cpp
template<class T>
void print(T t){
	cout << t << endl;
}
```

可变模板参数求和
```cpp
template<typename T>
T sum(T t){
	return t;
}
template<typename T, typename ... Types>
T sum(T first, Types ...rest){
	return first + sum<T> (rest...);
}

sum(1, 2, 3, 4);
```

递归函数展开参数包是一种标准做法，也比较好理解，但是缺点时必须要一个重载的（同名）递归终止函数来终止递归。

或者不递归方式，这种方式需要借助逗号表达式和初始化列表。前面的print可以这么写
```cpp
template<class T>
void printarg(T t){
	cout << t << endl;
}

template <class ...Args>
void expand(Args... args){
	int arr[] = {(printarg(args), 0)...};
}

expand(1, 2, 3, 4);
```

arr这个数组的目的单纯是展开参数包

如果将函数作为参数，就可以支持lambda表达式
```cpp
template<class F, class... Args> void expand(const F& f, Args&&...args){
initializer_list<int>{(f(std::forward< Args>(args)), 0)};
}
expand([](int i){cout << i << endl;}, 1,2,3);
```

可以带任意个数不同的参数，比如std::tuple
```cpp
template<class... Types>
class tuple;
```

模板偏特化和递归方式展开参数包

可变参数模板类的展开一般需要定义两到三个类，包括类声明和偏特化的模板类
```C++
// 前向声明
template<typename... Args>
struct Sum;

// 基本定义
template<typename First, typename... Rest>
struct Sum<First, Rest...>{
	enum { value = Sum<First>::value + Sum<Rest...>::value };
}

// 递归终止
template<typename Last>
struct Sum<Last>{
	enum { value = sizeof(Last) };
}
```



# 标准模板库 STL
STL六大部件：容器（containers），分配器（allocators），算法（algorithm），迭代器（iterator），适配器（adapters），仿函数（functors）

### 常用的容器
vector, deque, list, set/multiset, map/multimap 等

#### 1. Vector
Vector是一种变长数组。
```C++
#include<vector>
using namespace std;

vector<int> name;
vector<double> name;
vector<char> name;
vector<struct node> name;

// 这两个主要有速度上的区别，array非常慢，vector快一些
vector< vector<int> > name; // > >之间要加空格，新标准不用加了
vector<int> array[SIZE]; // 这个不是很常用，因为容易出错，且数组不知道自己的长度，还有std::array
```

访问方式
```C++
// 1. 通过下标
#include<iostream>
#include<vector>
using namespace std;

int main()
{
	vector<int> vi;
	vi.push_back(1);
	cout<<vi[0]<<endl;
	return 0;
}

// 2. 通过迭代器
vector<int>::iterator
vector<double>::iterator

// 例
#include<iostream>
#include<vector>
int main()
{
	vector<int> v;
	for(int i = 0; i < 5; i++)
	{
		v.push_back(i);	
	}
	vector<int>::iterator it=v.begin();
	for(int i = 0; i < v.size(); i++)
	{
		cout << it[i] << " ";
		// 也可以写成 cout << * (it + i) << " ";
	}
	return 0;
}

// 或者优雅的写法
// 因为迭代器不支持 it < v.end()的写法，只能写!=
for (vector<int>::iterator it=v.begin(); it!=v.end();it++)
{
	cout << *it << " ";
}
```
常用函数
```C++
push_back(item) // 在vector后面添加一个元素
pop_back(item) // 在vector后面删除一个元素
size(vector) // 返回元素个数，时间复杂度O(1)
clear(vector) // 清除所有元素，时间复杂度O(N)
insert(position, x) // 在position的地方插入一个x
// 例
v.insert(v.begin()+2, -1); // 相当于在v[2]处插入一个-1
erase(position);
erase(positionBegin, positionEnd);  // 左闭右开
```

#### 2. set
集合是不允许元素重复的无序容器
```C++
#include<set>
using namespace std;

set<int> name;
set<double> name;
set<char> name;
set<struct node> name;
set<set<int> > name;
```
因为无序，set只能通过iterator访问，除了vector和string之外的容器都不能通过下标访问
```C++
set<int>::iterator it;
set<char>::iterator it;
```
常用函数
```C++
st.insert(X);
st.find(X); // 返回set中value所对应的迭代器，也就是value的指针
// 例
set<int>::iterator it = st.find(2);
cout << *it << endl;
// 可以直接写成
cout << *(st.find(2)) << endl;
st.erase(it); // 删除某个地址的元素，时间复杂度O(1)
st.erase(X); // 删除某个元素，时间复杂度O(N)
st.erase(itBegin, itEnd);
st.size();
```

#### 3. deque
deque是由一段定量连续空间构成，一旦要在deque的前端和尾端增加空间，便配置一段连续空间，串在整个deque的头部和尾部.

#### 4. list


#### 5. map/unordered_map


#### 6. string 
```C++
// init
#include<string>
string str;
string str = "Hello";
cin >> str;
cout << str;


// assignment
char cstr1[20];
char cstr2[20] = "jaguar";

string str1;
string str2 = "panther";

cstr1 = cstr2; // illegal
str1 = str2; // legal


// concatenation
string str3;
str3 = str1 + str2;
str1 += str2;
str1 += "a string literal";

// constructors (Ctors)
string (const char *cp, int len);
string (const string& s2, int pos);
string (const string& s2, int pos, int len);

// sub-string
substr (int pos, int len);

// modification
assign (...);
insert (...);
insert (int pos, const string& s);
erase (...);
append (...);
replace (...);
replace (int pos, int len, const string& s);
...

// search
find (const string& s);


// File I/O
#include <ifstream> // read from file
#include <ofstream>  // write to file

// write into file
ofstream File1("...");
File1 << "Hello world" << std::enl;

// read from file
ifstream File2("...");
std::string str;
File2 >> str;
```

### 算法
算法部分主要由`<algorithm> <numeric> <functional>`组成
`<algorithm>`是最大的一个
`<numeric>`体积很小，只包括几个在序列上进行简单数学运算的模板函数
`<functional>`定义了一些模板类，用以声明函数对象


### 迭代器 Iterator
用迭代器可以读取它指向的元素。迭代器名就表示迭代器指向的元素，通过非常量迭代器还能修改其指向的元素。
```C++
#include<iostream> 
#include<vector> 
using namespace std; 
int main() { 
	vector<int> v; 
	for (int n = 0; n < 5; ++n) 
		v.push_back(n); 
	vector<int>::iterator i; 
	for (i = v.begin(); i != v.end(); i++) { 
		cout << *i << " "; // *i 是 i 指向的元素 *i *= 2; 
	} 
}
```
# 类库和STL

STL是范型程序设计的一个范例，含：容器（container）、迭代器（iterator）、算法（algorithm）、函数对象（function object）。类库是类的集合，是一种预定义的面向对象的程序库。

## C++的标准库

using namespace std;

- 基本的运行库：例如支持动态内存分配、运行时类型信息RTTI
- C语言的标准库
- 标准模板库STL
- 输入输出流类库（I/O stream）和字符串
- 数值计算库

## STL中的容器类

容器（container）类是用来容纳、包含一组元素或元素集合的对象的。STL中定义了多种不同类型的容器，例如

- 向量 vector
- 线性表 list
- 队列 queue
- 映射 map
- 集合 set
- 字符串 string
- stack: stack
- associative array: map

### 向量 vector

定义

```cpp
vector<int> iv;
vector<int> cv(5);
vector<int> cv(5, 'x');
vector<int> iv2(iv);
```

使用

```cpp
#include<iostream>
#include<vector>
using namespace std;
int main()
{
	vector<char> v;  // create zero-len vector
	int i;
	
	// put values into a vector
	for (i = 0; i < 10; i++)
		v.push_back('A' + i);
	
	// can access vector contents using subsripting
	for (i = 0; i < 10; i++)
		cout << v[i] << " ";
	cout << endl;

	// access via iterator
	vector<char>::iterator p = v.begin();
	while(p != v.end())
	{
		cout << *p << " ";
		p++;
	}
	return 0;
}
```

### 线性表 list

定义了双向的线性表，又可称为双向链表。list类只支持顺序访问。

```cpp
// sort a list
#include<iostream>
#include<list>
#include<cstdlib>
using namespace std;

int main()
{
	int i;
	list<char> lst;
	// create a list of random characters
	for (i = 0; i < 10; i++)
		list.push_back('A' + (rand()%26));
	
}
```

### 集合 set

```cpp
#include<set>
#include<iostream>
#include<string>
int main()
{
	std::set<std::string> source;
	std::string input;
	for(int i=0;i<6;i++)
	{
		std::cin>>input;
		source.insert(input);
	}
	std::set<std::string>::iterator at = source.begin();
	while(at != source.end())
		std::cour << * at++ << std::endl;
}
```

### multiset

### 映射 map

### 队列 queue

### std::stack

### std::pair

### 字符串string

## 算法库 `<algorithm>

- 排序 sort()
- 查找 find()
- 替换 replace()
- 合并 merge()
- 反序 reverse()
- 统计 count()

### 排序算法sort

```cpp
#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
using namespace std;
void load(vector<string>&);
void print(vector<string>);
const int SIZE = 8;
int main()
{
	vector<string> v(SIZE);
	load(v);
	sort(v.begin(), v.end());  // 指定排序的起止位置
	print(v);
	return 0;
}
// 会按照字母序排序
```

## 迭代器

是一种类似指针的对象，可以使用迭代器来访问容器中的元素。

- 随机访问迭代器 RandIter
- 双向迭代器 BiIter
- 前向迭代器 ForIter
- 输入迭代器 InIter
- 输出迭代器 OutIter

### 反向迭代器 reverse iterator
```C++
#include<list>
#include<iostream>
int main()
{
	using namespace std;
	list<int> c1;
	list<int>::iterator c1_Iter;
	list<int>::reverse_iterator c1_rIter;
	
	c1_rIter = c1.rbegin(); // the last element

}
```


## 参考资料
https://zhuanlan.zhihu.com/p/344558356
LJJ PPT