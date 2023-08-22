浅拷贝（默认拷贝函数）：将原对象或原数组的引用直接赋值给新对象、新数组，新对象/新数组只是原对象的一个引用。
深拷贝：创建一个新的对象和数组，将原对象的各项属性的“值”（数组里的所有元素）拷贝过来。是“值”而不是引用。

使用时注意：
深拷贝会在堆内存里另外申请空间来储存数据，从而解决了指针悬挂问题。当数据成员中有指针时，必须使用深拷贝。

深拷贝的写法
```cpp
class MyString
{
	private:
	   char *str;
	public:
	   MyString(const char *p=nullstr)//缺省构造函数
	       :str(nullptr)
	  {
	     if(p!=nullptr)
	    {
	      int len=strlen(p)+1;
	      str=new char[len];
	      strcpy_s(str,lrn,p);
	     }
	  }
	 
	   MyString(const MyString& ms)//拷贝构造函数，深拷贝
	  {
		 int n = strlen(ms.str) + 1;
		 *str = new char[n];
		 strcpy_s = (str, n, ms.str);
	     //int *str
	     // this->str=new int(*ms.str)
	  }
	 
	   ~MyString()//析构函数
	  {
	  }
}；
```