# Python Setup Packages

编写setup.py文件是为了使用Python的setuptools构建安装自己的Python包。
一个setup.py文件应当放在包代码目录下。例如包代码目录为
```yaml
your_package_name/
    __init__.py
    module1.py
    module2.py
    setup.py
```
其中setup.py的写法是
```Python
from setuptools import setup
setup(
    name='YourPackageName',
    version='1.0',
    author='Your Name',
    author_email='your@email.com',
    description='Description of your package',
    packages=['your_package_name'],   # 包的目录列表。如果有多个包，可以使用find_packages()查找
    install_requires=[                # 这些依赖将自动安装 
        'dependency1',
        'dependency2',
    ],
)
```
设置完成后，应当在命令行使用如下方式运行打包
```Command
python setup.py sdist bdist_wheel
```
用如下方式安装
```Command
pip install dist/YourPackageName-1.0.tar.gz
```