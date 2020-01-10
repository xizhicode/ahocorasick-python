
# ahocorasick-python


ac自动机python的实现，可用于python2 python3等主流python发行版，对标准的ac自动机算法进行了完善 优化(主要是改进了结果的准确性)。<br/>
注意：为了保证结果的准确性，请安装使用最新版。



## 1.如何安装


#### pip 安装（推荐）
```commandline
pip install  ahocorasick-python
```
#### 源码安装
```commandline
git clone  https://github.com/xizhicode/ahocorasick-python.git
cd ahocorasick-python && python setup.py install
```


### 2.如何使用

注： 此处python3为例，python2也是类似的结果<br/>

#### 简单检索
```python
import  ahocorasick     # 导入包
tree = ahocorasick.AhoCorasick("test","book","oo","ok", "k") # 构建ac自动机
print(tree.search("test book")) # 检索
```
输出结果：
```python
{'test', 'k', 'oo', 'book', 'ok'}
```


#### 检索并返回结果字符所在的位置（可以用于字符替换等场景）
```python
import  ahocorasick     # 导入包
tree = ahocorasick.AhoCorasick("test","book","oo","ok", "k") # 构建ac自动机
print(tree.search("test book",True)) # 检索
```
输出结果：
```python
{('k', (8, 9)), ('book', (5, 9)), ('oo', (6, 8)), ('ok', (7, 9)), ('test', (0, 4))}
```