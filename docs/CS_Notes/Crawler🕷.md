解析html的步骤：
- 层次化的数据
- 有多个解析html的三方库，如：lxml，beautifulsoup，htmlparser

## requests
```python
import requests
```

反反爬的
```python
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
```

## Beautifulsoup
### 安装和初始化
```powershell
pip install beautifulsoup4
```

解析的第一步是构建一个beautifulsoup对象
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html_parser')
```

### 介绍
第一个参数html_doc是读取的html文档，第二个参数是解析器，beautifulsoup支持以下解析器

| 解析器 | 使用方法 | 优势 | 劣势 |
| --- | --- | --- | --- |
| Python标准库 | BeautifulSoup(markup, “html.parser”) |  | 中文不行 |
| lxml HTML解析器 | BeautifulSoup(markup, “lxml”) | 快 | C语言库 |
| lxml XML解析器 | BeautifulSoup(markup, [”lxml-xml”]), BeautifulSoup(markup, “xml”) | 快 | C语言库 |
| htmlSlib | BeautifulSoup(markup, “html5lib”) | 准 | 慢 |

BeautifulSoup类的基本元素

| 基本元素 | 说明 |
| --- | --- |
| Tag | 标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾 |
| Name | 标签的名字，即尖括号里的内容 |
| Attribute | 标签的属性，返回一个字典 |
| NavigableString | 标签内的非属性字符串，返回一个String |
| Comment | 标签内字符串的注释部分，一种特殊的Comment类型 |

### 使用方法
访问标签：用soup.<tag>的格式，每次只能返回第一个匹配的tag。

```python
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.head) #<head><title>The Dormouse's story</title><head>
print(soup.head.title) # <title>The Dormouse's story</title>
print(soup.a) # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
```


访问多个标签；使用soup.find_all(’<tag>’)。会返回一个list.

```python
soup.find_all('a')
// [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup.find_all('a')[0]
// <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
```

可以在find_all方法中添加过滤条件。

```python
soup.find_all('a', text = 'Elsie')
// [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.find_all('a', attrs = {'id': 'link1'})
// [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.find_all('a', id = 'link1')
// 但是这样写不适用于所有属性？

soup.find_all('p', class_= 'title')
// [<p class="title"><b>The Dormouse's story</b></p>]
// 这种是CSS选择器
```

### 访问标签内容和属性

通过 name 和 string 可以访问标签的名字和内容，通过 get 和中括号操作符可以访问标签中的属性和值。

```python
print(soup.a)
## <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(soup.a['class'])
## ['sister']

print(soup.a.get('class'))
## ['sister']

print(soup.a.name)
## 'a'

print(soup.a.string)
## 'Elsie'
```

### 解析网页

```python
import requests
import chardet
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url = ""
rqg = requests.get(url, headers = hearders, timeout = 3.0)
rqg.encoding = chardet.detect(rqg.content)['encoding']  # requests 请求过程

# 初始化HTML
html = rqg.content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')  # 生成 BeautifulSoup 对象
print('输出格式化的BeautifulSoup对象：', soup.prettify())

print('名为title的全部字节点：', soup.find_all("title"))

print('title子节点的文本内容:', soup.title.string)
print('使用get_text()获取的文本内容：', soup.title.get())

target = soup.find_all('ul', class_ = 'menu') # 按照CSS类名完全匹配
target = soup.find_all(id = 'menu')  # 传入关键字id，搜索符合条件的节点
target = soup.ul.find_all('a')   # 所有名称为a的节点
```

## lxml的XPath

lxml这个库同时支持HTML和XML的解析，支持XPath解析方式，解析效率高。

使用xpath需要从lxml库中倒入etree模块，需要使用html类对需要匹配的html对象进行初始化。

```python
import requests
import chardet
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url = ""
rqg = requests.get(url, headers = hearders, timeout = 3.0)
rqg.encoding = chardet.detect(rqg.content)['encoding']  # requests 请求过程

# 初始化HTML
html = rqg.content.decode('utf-8')
html = etree.HTML(html, parser = etree.HTMLParser(encoding = 'utf-8'))
```

安装途径

```python
pip install lxml
```

Xpath常用的表达式

| 表达式 | 描述 |
| --- | --- |
| nodename | 选取此节点的所有子节点。 |
| / | 从根节点选取。 |
| // | 从匹配选择的当前节点选择文档中的节点 |
| . | 选取当前节点。 |
| … | 选取当前节点的父节点。 |
| @ | 选取属性。 |

使用表达式定位head和title节点

```python
result = html.xpath('head')  ## 通过名称定为head节点
result1 = html.xpath('/html/heda/title')  ## 按节点层级定位title节点
result2 = html.xpath('//title')  ## 也可以定位title节点
```

Xpath谓词常用的表达式

| 表达式 | 结果 |
| --- | --- |
| xpath(’/body/div[1]’) | 选取body下的第一个div节点 |
| xpath(’/body/div[last()]’) | 选取body下最后一个div节点 |
| xpath(’/body/div[last()-1]’) | 选取body下倒数第二个div节点 |
| xpath(’/body/div[position()<3]’) | 选取body下前两个节点 |
| xpath(’/body/div[@class]’) | 选取body下带有class属性的div节点 |
| xpath(/body/div[@class=”main”]’) | 选取body下class属性为main的div节点 |
| xpath(”/body/div[price>35]”) | 选取body下price元素值大于35的节点 |

## request-html

requests-html理解为可以解析HTML文档的request库

```python
pip install requests-html
```

获取一个user-agent

```python
user_agent = requests_html.user_agent()
```

对JavaScript的支持是requests-html最大的亮点，会用到render函数，需要注意的是第一次使用这个方法，它会先下载Chromium，然后使用Chromium来执行代码，但是下载的时候可能需要一个梯子。

示例

```python
from requests_html import HTMLSession

session = HTMLSession()

def parse():
		r = session.get('http://www.qdaily.com/')
    # 获取首页新闻标签、图片、标题、发布时间
    for x in r.html.find('.packery-item'):
        yield {
            'tag': x.find('.category')[0].text,
            'image': x.find('.lazyload')[0].attrs['data-src'],
            'title': x.find('.smart-dotdotdot')[0].text if x.find('.smart-dotdotdot') else x.find('.smart-lines')[0].text,
            'addtime': x.find('.smart-date')[0].attrs['data-origindate'][:-6]
        }
```

通过简短的几行代码，就可以把整个首页的文章抓取下来。

示例中使用的几个方法：

① find( ) 可以接收两个参数：

第一个参数可以是class名称或ID第二个参数first=True时，只选取第一条数据

② text 获取元素的文本内容

③ attrs 获取元素的属性，返回值是个字典

④ html 获取元素的html内容

使用requests-html来解析内容的好处在于作者都高度封装过了，连请求返回内容的编码格式转换也自动做了，完全可以让代码逻辑更简单直接，更专注于解析工作本身。