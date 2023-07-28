
# 增
按列增加
```python
citys = ['ny','zz','xy']
df.insert(0,'city',citys) #在第0列，加上column名称为city，值为citys的数值。
jobs = ['student','AI','teacher']
df['job'] = jobs #默认在df最后一列加上column名称为job，值为jobs的数据。
df.loc[:,'salary'] = ['1k','2k','2k','2k','3k'] #在df最后一列加上column名称为salary，值为等号右边数据。
```

按行增加
```python
df.loc[4] = ['zz','mason','m',24,'engineer’]#若df中没有index为“4”的这一行的话，该行代码作用是往df中加一行index为“4”，值为等号右边值的数据。若df中已经有index为“4”的这一行，则该行代码作用是把df中index为“4”的这一行修改为等号右边数据。
df_insert = pd.DataFrame({'name':['mason','mario'],'sex':['m','f'],'age':[21,22]},index = [4,5])
ndf = df.append(df_insert,ignore_index = True) #返回添加后的值，并不会修改df的值。ignore_index默认为False，意思是不忽略index值，即生成的新的ndf的index采用df_insert中的index值。若为True，则新的ndf的index值不使用df_insert中的index值，而是自己默认生成。
```

# 删
删除行
```python
df.drop([1,3],axis = 0,inplace = False)#删除index值为1和3的两行，
```

删除列
```python
df.drop(['name'],axis = 1,inplace = False) #删除name列。
del df['name'] #删除name列。
ndf = df.pop('age’)#删除age列，操作后，df都丢掉了age列,age列返回给了ndf。
```

# 改
改行列标题
```python
df.columns = ['name','gender','age'] #尽管我们只想把’sex’改为’gender’，但是仍然要把所有的列全写上，否则报错。
df.rename(columns = {'name':'Name','age':'Age'},inplace = True) #只修改name和age。inplace若为True，直接修改df，否则，不修改df，只是返回一个修改后的数据。
df.index = list('abc')#把index改为a,b,c.直接修改了df。
df.rename({1:'a',2:'b',3:'c'},axis = 0,inplace = True)#无返回值，直接修改df的index。
```

改数值
```python
df.loc[1,'name'] = 'aa' #修改index为‘1’，column为‘name’的那一个值为aa。
df.loc[1] = ['bb','ff',11] #修改index为‘1’的那一行的所有值。
df.loc[1,['name','age']] = ['bb',11]    #修改index为‘1’，column为‘name’的那一个值为bb，age列的值为11。
```

使用iloc[row_index, column_index]
```python
df.iloc[1,2] = 19#修改某一无素
df.iloc[:,2] = [11,22,33] #修改一整列
df.iloc[0,:] = ['lily','F',15] #修改一整行
```

## 筛选数据方法loc、iloc
```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200315', periods = 5)
df = pd.DataFrame(np.arange(20).reshape(5,4), index = dates, columns = ['A', 'B','C','D'])
print(df)
```

```Text
#输出
A   B   C   D
2020-03-15   0   1   2   3
2020-03-16   4   5   6   7
2020-03-17   8   9  10  11
2020-03-18  12  13  14  15
2020-03-19  16  17  18  19
```


```python
print(df['A'])
```

```Text
#输出
2020-03-15     0
2020-03-16     4
2020-03-17     8
2020-03-18    12
2020-03-19    16
Freq: D, Name: A, dtype: int64
```


```python
print(df.A)
```

```
#输出
2020-03-15     0
2020-03-16     4
2020-03-17     8
2020-03-18    12
2020-03-19    16
Freq: D, Name: A, dtype: int64
```

跨越多行或者多列
```python
print(df[0:3])
```

```
#输出
A  B   C   D
2020-03-15  0  1   2   3
2020-03-16  4  5   6   7
2020-03-17  8  9  10  11

```


```python
print(df['20200315' : '20200317'])
```

```
#输出
A  B   C   D
2020-03-15  0  1   2   3
2020-03-16  4  5   6   7
2020-03-17  8  9  10  11

```


## loc纯标签筛选

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200315', periods = 5)
df = pd.DataFrame(np.arange(20).reshape(5,4), index = dates, columns = ['A', 'B','C','D'])
print(df)
print('\n')
print(df.loc['20200315'])    #打印某一行的标签
print('\n')
print(df.loc[:,['A', 'B']])   #打印A、B属性的所有行
print('\n')
print(df.loc['20200315', ['A', 'B','C']])
```


```
#输出
             A   B   C   D
2020-03-15   0   1   2   3
2020-03-16   4   5   6   7
2020-03-17   8   9  10  11
2020-03-18  12  13  14  15
2020-03-19  16  17  18  19

A    0
B    1
C    2
D    3
Name: 2020-03-15 00:00:00, dtype: int64

             A   B
2020-03-15   0   1
2020-03-16   4   5
2020-03-17   8   9
2020-03-18  12  13
2020-03-19  16  17

A    0
B    1
C    2
Name: 2020-03-15 00:00:00, dtype: int64

```


# 查
## 遍历
iterrows(): 按行遍历，将DataFrame的每一行迭代为(index, Series)对，可以通过row[name]对元素进行访问。
itertuples(): 按行遍历，将DataFrame的每一行迭代为元祖，可以通过row[name]对元素进行访问，比iterrows()效率高。
iteritems():按列遍历，将DataFrame的每一列迭代为(列名, Series)对，可以通过row[index]对元素进行访问。
