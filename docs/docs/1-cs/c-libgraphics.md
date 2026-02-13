# C大程 libgraphics 文档 使用记录

⚠️ 没写完 TODO

## 已知问题

- 只能与windows系统中的dec++或vs兼容。windows虚拟机不行。

## DevC++图形编程过程

- 使用已有的工程直接打开
- 新建文件方法：
    - →新建
    - →选择加入当前工程
    - →修改Makefile.win，在末尾加入（自己实践的时候这步不加好像也行）
        
        ```cpp
        gratest1.o:gratest1.c
        $(CC) -c gratest1.c -o gratest1.o $(CFLAGS)
        ```
        

## 函数库

graphics.h 仅提供以下少量画图函数接口

```c
InitGraphics();
MovePen(x, y);
DrawLine(dx, dy);
DrawArc(r, start, sweep);
GetWindowWidth();
GetWindowHeight();
GetCurrentX();
GetCurrentY();
```

我们将在下面介绍这些接口的用法。

### 初始化操作

在main.c里需要进行如下初始化

```c
#include "graphics.h"
#include "extragraph.h"
#include "imgui.h"

void Main()        // 注意这里需要使用大写Main
{
	Set WindowTitle("Your Title");
	InitGraphics();  // 调用了图形模式
}
```

InitGraphics(); 这个函数会打开一个空的图形窗口。

### 窗口

以下四个函数都不需要传入参数，分别返回窗口宽、高，当前X、Y坐标。

```c
GetWindowWidth();
GetWindowHeight();

GetCurrentX();
GetCurrentY();
```

#### 好的编写习惯

应该先定义一些常量，给这些常量取名字

```c
#define HouseHeight 2.0
#define HouseWidth 3.0
#define AtticHeight 0.7
#define DoorWidth 0.4
#define DoorKnobRadius 0.03
#define DoorKnobInset 0.07
#define PaneHeight 0.25
#define PaneWidth 0.2
#define FirstFloorWindows 0.3
#define SecondFloorWindows 1.25
```

### 画图形的

#### MovePen

将笔移动到(x, y)该坐标。注意当画图形时，后面几个函数的相对位移，都是相对于这个函数设置的笔坐标移动的。

```cpp
MovePen(double x, double y);
```

#### DrawLine

在画线之前一定要MovePen();

```cpp
DrawLine(double dx, double dy);
```

画线的方向：

横坐标最左边是0，向右增大

纵坐标最下面是0，向上增大

可以理解为我们在第一象限

#### DrawArc

在画弧之前一定要MovePen();

```cpp
DrawArc(double r, double start, double sweep);
```

#### 我们应当把画矩形封装成一个新的函数

```c
void DrawBox (double x, double y, double width, double height)
{
	MovePen(x, y);
	DrawLine(0, height);
	DrawLine(width, 0);
	DrawLine(0, height);
	DrawLine(-width, 0);
}
```

```c
void DrawCenteredBox(double x, double y, double width, double height)
{
	DrawBox(w - width/2, y - height/2, width, height);
}
```

#### 画圆的函数

```c
void DrawCenteredCircle(double x, double y, double r)
{
	MovePen(x + r, y);
	DrawArc(r, 0, 360);
}
```

### 文字

从当前位置开始输出文本串

```c
DrawTextString(string);
```

这个函数用于获取某个字符串长度

```cpp
double stringLen = TextStringWidth(string); 
```

### 查看回调函数类型

```c
typedef void(* KeyboardEventCallback)(int key, int event);
```

## 定时器

### 时间回调函数

```cpp
registerTimerEvent(mytimer);  //获取电脑时钟信息返回给mytimer
startTimer(0, (int)(1000/speed));  // 要讨论传进来的timer是什么
```

### 定时器消息回调函数

```c
void TimerEventProcess(int timerID);
```

示例

```c
typedef enum
{
	LabelTimer,
	BoxTimer,
} MyTimer;
```

```c
void mytimer(int  timerID)
{
	switch (timerID)
	{
	case LabelTimer:
		label_x += 0.5;
		if (label_x > 5.0) 
			label_x = 1.0;
		display();
		break;
	case BoxTimer:
		box_y += 0.5;
		if (box_y > 5.0) box_y = 1.0;
		display();
		break;
		break;
	}
}
```

```c
registerTimerEvent(mytimer);
startTimer(LabelTimer, 100);
startTimer(BoxTimer, 200);
```

## 鼠标

### 鼠标消息回调函数

```c
void MouseEventProcess(int x, int y, int button, int event);
```

x, y - 位置坐标

button - 按下的是哪个键

event - 按下，松开，移动等事件

```c
void myMouseEvent (int x, int y, int button, int event)
{
	mouse_x = ScaleXInches(x);   // 这个函数在extragraph库里
	mouse_y = ScaleYInches(y);
	display();
}
```

需要在Main()里添加这一行

```c
registerMouseEvent(myMouseEvent);
```

在display()里

```c
void display()
{
	double w = 1.0;
	double h = GetFontHeight() * 2;
	// 清除屏幕
	DisplayClear();
	// draw a square
	SetPenColor("Red");
	drawLabel(label_x, label_y, "Lable is Here");
	
	//draw a rect/box to trace the mouse
	//drawRectangle(mouse_x, mouse_y, w, h, 0);
	SetPenColor("Blue");
	drawBox(mouse_x, mouse_y, w, h, 1, "This box follows the mouse", 'L', "Red");
}
```

## 使用linkedlist库

```c
#include "linkedlist.h"
```

创建一个 linkedlist 名叫 g_polylines

```c
linkedlistADT g_polylines = NULL;

g_polylines = NewLinkedList();
display();
```

```c
void display()
{
	linkedlistADT poly = NextNode(g_polylines, g_polylines);
	
	SetPenColor("Blue");
	if (poly) {
		Point * p = (Point*) NodeObj(g_polylines, poly);
		double lx = p->x;
		double ly = p->y;
		MovePen(lx, ly);
		while (poly = NextNode(g_polylines, poly))
		{
			p = (Point*) NodeObj(g_polylines, poly);
			DrawLine(p->x - lx, p->y - ly);
			lx = p->x;
			ly = p->y;
		}
	}
}
```

## 使用button和键盘

这次需要用到的库

```c
#include <windows.h>
#include <winuser.h>
#include "graphics.h"
#include "extgraph.h"
#include "imgui.h"
#include "linkedlist.h"
```

### 字符输入回调函数

```c
void charEventProcess(char c);
```

c - 输入字符的ASCII码

### 键盘回调函数

```c
void KeyboardEventProcess(int key, int event);
```

key - 哪个键

event - 按下还是松开

示例

在Main()中

```c

```

```c
void myKeyboardEvent(int key, int event)
{
	uiGetKeyboard(key, event); // needed for using simpleGUI
	display();

	switch (event)
	{
	case KEY_UP:
		if (key == VK_F1)
			g_add_point = !g_add_point;

		break;

	default:
		break;
	}
}
```

## 颜色库

自带的颜色列表

```cpp
char colorlist[100][100] = {”Black”, “Dark Gray”, “Gray”, “Light Gary”, “White”, “Brown”, “Red”, “Orange”, “Yellow”, “Green”, “Blue”, “Violet”, “Magenta”, “Cyan”};
const int colorNumber = 14;
```

自定义颜色

颜色会被加入颜色库，RGB的取值范围都是[0, 1]而不是[0, 256)

```cpp
DefineColor("Color Name", R, G, B);
```

## libgraphics其它常用的东西