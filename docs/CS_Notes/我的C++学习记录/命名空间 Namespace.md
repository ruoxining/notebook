命名空间：
名称name可以是符号常量，变量，函数，结构，枚举，类和对象等。

定义
```cpp
namespace A{
	int a = 100;
}

namespace B{
	int b = 200;
}

void test(){
	
	cout << A::a << endl;
	cout << B::a << endl;
}
```

- namespace必须是全局的，不能在函数中定义namespace
- namespace可以嵌套，可以在namespace中定义namespace
    ```cpp
    namespace A{
    	int a = 100;
    	namespace B{
    		int a = 2000;
    		}
    }
    
    void test(){
    	cout << A::a << endl;
    	cout << A::B::a << endl;
    }
    ```
    
- namespace是开放的，即可以随时把新成员加入已有的namespace中
    ```cpp
    namespace A{
    	int a = 100;
    	int b = 200;
    }
    // 将c添加到已有的namespace中
    namespace A{
    	int c = 300;
    }
    
    void test(){
    	cout << A::a << endl;
    	cout << A::c << endl;
    }
    ```
    
- namespace可以存放变量和函数
    
    ```cpp
    namespace A{
    	int a = 100;
    	void func(){
    		cout << a << endl;
    	}
    }
    
    void test(){
    	cout << a << endl;
    	A::func();
    }
    ```
    
- namespace中的函数可以在namespace外定义
    ```cpp
    namespace A{
    	int a = 100;
    	void func();
    }
    
    // 成员函数
    void A::func(){
    	cout << a << endl;
    }
    // 普通函数
    void funcb(){
    	cout << A::a << endl;
    }
    
    void test(){
    	A::func();
    	funcb();
    }
    ```
    

## 什么时候需要使用namespace？

- 可以使不同用户在相同工程下的名称相同的变量分隔开来，可以使效率更高
- 使用命名空间可以更清晰明了地表明用户定义的变量、函数在哪个地方
- 不同作用域下使定义的变量函数更严谨

变量名冲突的解决方法

如果全局变量与局部变量冲突，那么按就近原则来使用。（？）
