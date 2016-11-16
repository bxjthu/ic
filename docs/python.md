# Python and Python IDE

---

<a name="install"></a>
## 安装 Python 工作环境

&nbsp;

* 方式1: 安装 Python3 及各个软件包

首先安装 [Python3](https://www.python.org). 

Python 官网有很多不错的资源和文档, 包括如何[安装](https://www.python.org/about/gettingstarted/), 以及如何[选择IDE](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments), [选择编辑器](https://wiki.python.org/moin/PythonEditors), 等等

然后通过 `pip/pip3` 命令安装所需的软件包, 比如

```bash
$ pip install jupyter
```

* 方式2: 安装 Anaconda

[Anaconda](https://www.continuum.io)是一个包含了很多科学实验、工程设计、数据分析所需软件包的Python平台, Anaconda 自带了Python 环境, 不需要再单独安装.  

Anaconda比较大, 还可以只安装 miniconda, 通过[清华大学镜像](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/) 安装需要的软件包(numpy, scipy, matplotlib等).

---

<a name="editors"></a>
## 编辑器

&nbsp;

Quora有一个关于选择Python Editor的专题: <a href="https://www.quora.com/Whats-a-good-Python-editor-IDE">What's a good Python editor/IDE?</a>

* Python IDLE
* Sublime Text
* Github Atom
* TextEdit(MacOS)
* Vim/Emacs (适合专业程序员)


---
<a name="ides"></a>
## 集成开发环境IDE

&nbsp;

Wikipedia 有一篇专题: <a href="https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments#Python">Python IDE比较</a>

* [Jupyter](https://jupyter.org) 推荐: ★★★★☆

    * ipython: Anaconda提供了一个`ipython` 脚本, 运行后进入 ipython 终端交互界面.
      或者运行 `python3 -m IPython` 也可以进入 ipython 终端交互界面.

    * jupyter notebook: [安装jupyer](https://jupyter.readthedocs.io/en/latest/install.html), 启动后在浏览器中进入Notebook 可视交互界面

* [PyCharm](https://www.jetbrains.com/pycharm/) 推荐: ★★★★

* [Spyder](https://pythonhosted.org/spyder/) 推荐: ★★★★


---
<a name="online"></a>
## 在线使用 Python 

&nbsp;

推荐: ★★★★★

地址: [http://iwork.pku.edu.cn](http://iwork.pku.edu.cn)

用北大账号登录, 填写完整信息后可成为正式用户, 在线使用Jupyer notebook编写Python程序,
进行数据分析, 生成可视图表等.


---
<a name="style"></a>
## Python 编程风格

&nbsp;

[PEP8](https://www.python.org/dev/peps/pep-0008/)是官方给出的Python编程风格描述, 请务必详细阅读. 一个更简短的描述在[这里](pep8.org).

下面是一个 [foobar.py](/demos/foobar.py) 的例子, 可以此为模板修改自己的程序:

```python
#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does.

__author__ = "Zhangsan"
__pkuid__  = "1600012345"
__email__  = "zhangsan@pku.edu.cn"
"""

import math


def foo(par1, par2):
    """description of foo, using what par1 and par2, return what
    """
    pass


def main():
    """main module
    """
    foo(1, 2)


if __name__ == '__main__':
    main()
```

可以安装一个 pep8 软件包帮助检查代码是否符合[PEP8](https://www.python.org/dev/peps/pep-0008/) 规范.

```
$ pip install pip8
$ pep8 assign1.py
```
