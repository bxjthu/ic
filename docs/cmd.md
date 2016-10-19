# 使用命令行工具 

Python 是个脚本语言, 在很多情况下, 适合在命令行终端中执行Python程序. 
因此，我们需要了解一些在终端中如何用命令行工具操作计算机的技巧.

Windows, Mac OS, Linux三种常见操作系统的命令行工具各不相同. 

<hr>

## Windows

### DIR —— 显示磁盘目录命令 

功能：显示指定目录下的文件和子目录。
格式：“DIR [盘符:] [路径] [/P] [/W] [/S]”

使用说明：

/P：分屏的方式显示，每显示完一页提示用户按任意键继续显示。
/W：以宽行的方式显示文件和子目录，在纯DOS系统下，每行显示五个文件。
/S：连同子目录下的文件一同显示。

示例:

显示D:\Data目录下的所有内容

```
dir d:\Data
```


### CD —— 改变当前目录 

功能：改变当前目录，不带任何参数时，显示当前目录的完整路径
格式：CD [盘符:][路径名][子目录名]

使用说明：

1. 如果省略路径和子目录名则显示当前目录；
2. 若输入“CD \”，则返回到根目录；
3. 若输入“CD ..”格式，则返回到上一级目录

示例:

进入D盘Data目录

```
D:
cd D:\Data
```


### MKDIR —— 建立子目录 

功能：在磁盘中创建新的子目录
格式：MKDIR [盘符:][路径名]〈子目录名〉

使用说明：

1. “盘符”：指定要建立子目录的磁盘驱动器字母，若省略，则为当前驱动器；
2. “路径名”：要建立的子目录的上级目录名，若缺省则建在当前目录下。
3. 可以一次性建立多个接连式目录

示例:

在当前目录下建立一个名为test1的子目录

```
mkdir test1
```

### RMDIR —— 删除子目录

功能：从指定的磁盘删除空的子目录。
格式：RD [盘符:][路径名]<子目录名>[/S]

RD是RMDIR的缩写, 两者一样

使用说明：

1. 子目录在删除前必须是空的，也就是说需要先进入该子目录，使用DEL（删除文件的命令）
将其子目录下的文件删空，然后再返回到上一级目录，用RMDIR命令删除该了目录本身；

删除D:\Data\test1 子目录

```
rmdir d:\data\test1
```

### DEL —— 文件删除

功能：删除一个或多个文件。
格式：DEL [盘符:]<路径>[文件名]

使用说明：

1. 此命令不能够删除只读(R)，隐藏(H)，系统(S)文件；
2. 可使用通配符`*,?`。

示例:

删除D:\Data下面所有的后缀为exe的文件

```
del D:\Data\*.exe
```

### COPY —— 文件复制命令 

功能：利用COPY命令复制文件,连接多个文件。
格式：COPY <源文件名全称> [目标文件名全称]

使用说明：

1. COPY命令中源文件名必须指出，不可以省略；
2. 复制时，目标文件名可以与源文件名相同，称作“同名拷贝”此时目标文件名可以省略；
3. 复制时，目标文件名也可以与源文件名不相同，称作“异名拷贝”，此时，目标文件名
不能省略；
4. 复制时，还可以将几个文件合并为一个文件，称为“合并拷贝”，格式如下：

COPY [源盘][路径]〈源文件名1〉〈源文件名2〉…[目标盘][路径]〈目标文件名〉

5. 文件名中允许使用通配符`* ?`，可同时复制多个文件；

示例:

将当前目录下的hello.py 复制为hello2.py

```
copy hello.py hello2.py
```

将当前目录下的hello.py 复制到C:\

```
copy hello.py c:\
```

### XCOPY —— 目录复制

功能：复制指定的目录和目录下的所有文件连同目录结构到另一个目录及对应的子目录下。
格式：XCOPY [源盘:][源路径名] [目标盘:][目标路径名] [/S][/V][/E]

使用说明：

1. XCOPY是COPY的扩展，可以把指定的目录连文件和目录结构一并拷贝；
2. 使用时源盘符、源目标路径名、源文件名至少指定一个；
3. 选用/S时对源目录下及其子目录下的所有文件进行COPY。除非指定/E参数，否则不会拷贝空目录，
若不指定/S参数，则XCOPY只拷贝源目录本身的文件，而不涉及其下的子目录；
4. 选用/V参数时，对的拷贝的扇区都进行较验，但速度会降低。

### MOVE —— 移动目录或文件

功能：移动文件和重命名文件与目录。
格式：要移动一个或多个文件：MOVE [/Y | /-Y] [盘符:][源路径名]文件名[,...] 目标路径名
要重命名目录：MOVE [/Y | /-Y] [盘符:][源路径名]目录名1 目录名2

使用说明：

1. [盘符:][源路径名]文件名 指定要移动的文件的位置和名称。
目标路径名 指定文件的新位置。目标可以包含一个驱动器号和冒号、一个目录名或组合。
如果只移动一个文件，并在移动时将其重命名，还可以包括文件名。
2. [盘符:][源路径名] 目录名1 指定要重命名的目录。
目录名2 指定目录的新名称。
3. /Y 不使用确认是否要覆盖现有目标文件的提示。
/-Y 使用确认是否要覆盖现有目标文件的提示。

示例:

将test1目录移动到C:\

```
move test1 c:\
```

### 其它常用命令

TYPE —— 显示文本文件内容命令
REN —— 文件改名命令
CLS —— 清屏幕命令

### 如何获得命令的帮助？

当您不知道某个命令的具体用法时，可以向系统获取其帮助信息，其格式是：＜命令＞ /?
例如，要获得命令dir的帮助，可输入：

```
dir /?
```

### 命令补全

输入全部的命令和路径非常麻烦, 一个方法是自动补全, 输入几个字母后可以按 **TAB**  键,
系统会自动帮你把路径和命令补全.

### 环境变量的设置

第一步:右击“我的电脑”，点击“属性”；

第二步：选择“高级”选项卡，点击“环境变量”， 可以看到环境变量的设置界面。
接下来就可以点击相应地按钮(“新建”，“编辑”和“删除”按钮）来设置环境变量，即“新建”，“编辑”和“删除”环境变量。

注 意：用户环境变量和系统环境变量的区别。用户环境变量只对当前用户有效，在环境变量的设置界面中，上半部分显示的是“XXX的用户变量（U）”， 这就是用户XXX的环境变量，它只对用户XXX有效；而系统环境变量则对系统所有用户皆有效，在设置界面下半部分显示的“系统变量（S）”就是该系统的系 统环境变量。
Path环境变量包含了可执行程序的搜索路径，其设置过程如下：

选中“Path”环境变量；
点击“编辑”，然后在“变量值”中添加自己要添加的目录，各目录之间用分号(；)来隔开。

1. 显示环境变量PATH
```
echo %PATH%
```

2. 显示所有环境变量
```
set 
```

## Mac OS