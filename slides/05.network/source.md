class: center, middle

# 05. 计算机网络

### 计算概论B (化学)

&nbsp;
&nbsp;

#### 曹东刚 (caodg@pku.edu.cn)  

办公室: 理科1号楼1809

http://sei.pku.edu.cn/~caodg/course/ic

---

## 内容提要

### <font color="orangered">1. 概述</font> 

### 2. 电信网

### 3. 互联网


---

## 网络规模分类

<img src="images/scale.svg" width=700 style="margin: 00px 50px">

---

## 局域网, Local Area Network

- 范围有限, 最差传输时间有限, 管理简单 

- 两种典型结构:

    - 总线型 (Bus): 如以太网 (Ethernet) 802.3 
    
    - 环形 (Ring): 如 IBM 令牌环 IEEE 802.5


<img src="images/lan.svg" width=700 style="margin: 00px 50px">

---

## 无线局域网: Wi-Fi

- 频段: 2.4GHz (802.11 b/g/n), 5GHz(802.11 n/ac), 等

- 安全: WEP, WPA, WPA2

- 范围: 室内, 校园Wi-Fi, 城市Wi-Fi

- 干扰: 2.4GHz 干扰源很多，如微波炉，蓝牙，其它Wi-Fi设备等

<img src="images/Wi-Fi.gif" width="400" style="margin: 10px 50px">


---
## 城域网, Metropolitan Area Network

- 覆盖一个城市, 典型如有线电视网

<img src="images/man.svg" width=700 style="margin: 00px 50px">

---

## 广域网, Wide Area Network

- 可跨越一个国家

- 主机、交换设备 (路由器)、传输线

<img src="images/wan.svg" width=700 style="margin: 00px 50px">

---

## 互联网, internetwork 或 internet

- 互联网: 一组互相连接的网络

- Internet: 一种特定的、世界范围的互联网, 中文常称为因特网

- 互联网的共同组织形式: 通过一个 WAN 将多个 LAN 组织 起来.

- 通常如果一个网络全部是由一个机构构建并维护, 则认为是 WAN; 如果不同机构各
自构建并维护一部分, 则认为是 互联网.

---

## 互联网ISP之间的关系

<img src="images/Internet_Connectivity.svg" width=750 style="margin: 00px 00px">

---

## 用户接入互联网


<img src="images/Internet_Connectivity_Access_layer.svg" width=750 style="margin: 00px 00px">

---

<img src="images/chinaisp.jpg" width=900 style="margin: 00px -75px">

---

## 网络交互需要一套协议


<img src="images/translate.svg" width=600 style="margin: 00px 50px">

---

## 信息流经协议栈

<img src="images/flow.svg" width=700 style="margin: 00px 50px">

---

## OSI 7层协议栈参考模型


<img src="images/osi.svg" width=550 style="margin: 00px 50px">

---

## 内容提要

### 1. 概述 

### <font color="orangered">2. 电信网</font>

### 3. 互联网


---

## 公共电话交换网络 PSTN 

Public switched telephone network

- 使用电路交换技术的全球最大电话网络

- 包含: 电话线, 光纤, 微波链路, 蜂窝网络, 卫星, 海底线缆等

- 电话网络的发展历史

<img src="images/pstntopo.svg" width=700 style="margin: 10px 50px">

---

## PSTN 电话系统拓扑

- 本地回路, 模拟信号

- 电话机直接通过本地回路连接到端局

- 端局上层是长途交换局

- 局和局之间通过干线连接, 数字信号

<img src="images/pstn.svg" width=700 style="margin: 10px 50px">

---

## 电路交换

- 两部电话通话时, 他们之间建立的是一条物理通信路径, 称为电路

- 在电路交换中, 用户独享一个通信电路, 可以保证服务质量, 但是利用率低, 价格贵

<img src="images/circuit.svg" width=700 style="margin: 20px 50px">

---

## 拨号上网

调制解调器: Modem(modulator-demodulator), 数字信号/电话线路模拟信号转换


<img src="images/modem.svg" width=700 style="margin: 20px 50px">

---

## ADSL宽带上网

ADSL, Asymmetric Digital Subscriber Line: 同时传输语音信号和数字信号,
为用户下载 (下行) 分配比上传 (上行) 更多的带宽

方法: 将低频频段( 300Hz-3300Hz ) 仍然留给话音信号, 高频频段用于传输数字信号


<img src="images/ADSL_frequency_plan.svg" width=700 style="margin: 20px 50px">

---

## ADSL宽带上网

<img src="images/adsl.svg" width=700 style="margin: 20px 50px">


---

## 移动通信技术


- 1G : 模拟信号, 大哥大

- 2G : 数字信号, GSM, 手机, SIM 卡, 漫游, WAP, 短消息, GPRS, 流量, CDMA

- 3G : 支持高速数据传输

- 4G : 集3G与WLAN技术于一体, 移动互联网, 智能手机, LTE

- 5G : 比4G更快, 质量更好

---

## 内容提要

### 1. 概述 

### 2. 电信网

### <font color="orangered">3. 互联网</font>


---

## 局域网设备及原理


<img src="images/Ethernet_LAN.svg" width=700 style="margin: 00px 00px">

---

## 网卡与网线

- 网卡 (Network Interface Card): 有线,  无线 

- 网线 (Network Cable): 10M, 100M, 1000M

<table id="switch">
<tr>
<td align="center" valign="middle">
<img src="images/network_cable.jpg" width=200 style="margin: 00px 00px">
</td>
<td align="center" valign="middle">
<img src="images/network_card.jpg" width=200 style="margin: 00px 20px">
</td>
<td align="center" valign="middle">
<img src="images/network_card_mobile.jpg" width=200 style="margin: 00px 20px">
</td>
</tr>
</table>

---

## 交换机 (switch)

用于连接局域网内的设备


<table id="switch">
<tr>
<td align="center" valign="bottom">
<img src="images/linksys-switch.jpg" width=200 style="margin: 00px 00px">
</td>
<td align="center" valign="bottom">
<img src="images/lan-switch.png" width=500 style="margin: 00px 20px">
</td>
</tr>
</table>

---

## 路由器 (router)

用于连接不同的网络

<table id="switch">
<tr>
<td align="center" valign="bottom">
<img src="images/linksys-router.jpg" width=200 style="margin: 00px 00px">
</td>
<td align="center" valign="bottom">
<img src="images/router_network.jpg" width=400 style="margin: 00px 50px">
</td>
</tr>
</table>

---

## 办公室组网


<img src="images/routerswitch.png" width=500 style="margin: 00px 50px">


---

## 家庭组网


<img src="images/router_network2.jpg" width=600 style="margin: 00px 50px">

---

## Internet协议: TCP/IP 协议栈

- IP 协议: 网络层协议, Internet 的核心, 不可靠

- TCP/UDP: 传输层协议

    - TCP: 可靠, 有序, 纠错
    
    - UDP: 不可靠


<img src="images/protocol.svg" width=700 style="margin: 20px 50px">

---

## 用户数据通过协议栈的示意


<img src="images/UDP_encapsulation.svg" width=700 style="margin: 00px 50px">

---

## 用户数据在网络上传输的示意


<img src="images/IP_stack_connections.svg" width=450 style="margin: 00px 50px">

---

## IP数据包的分组交换, packet-switch

IP数据包在网络上分组传输

- 数据被分成分组, 中间路由器完整接收并保存分组, 并在线路闲的时候转发出去

- 线路利用率高, 但是服务质量难以保证

<img src="images/storeforward.svg" width=700 style="margin: 00px 50px">

---

## IP分组交换示例

<img src="images/Packet_Switching.gif" width=700 style="margin: 00px 50px">

---

## TCP: 在不可靠的IP协议上可靠传输数据

TCP (Transmission Control Protocol) 协议：传输控制协议，提供了一种可靠的、面向连接的数据流服务

- 双方通信前需要预先建立一条连接(虚电路) 

- 如何建立连接？

### 两军问题

<img src="images/2-generals.svg" width=700 style="margin: 00px 50px">

---

## TCP建立连接的三次握手

握手(handshake): 通信的双方就建立连接的自动协商过程


<img src="images/Tcp-handshake.svg" width=450 style="margin: 20px 50px">


---

## TCP简化状态图

<img src="images/Tcp_state_diagram_fixed_new.svg" width=750 style="margin: -40px 00px">

---


## IP 地址

- 每个运行 TCP/IP 协议的设备都要有一个唯一的 IP 地址, 用于标识该设备

- IP 地址由 4 个字节(IPv4) 组成, 便于记忆写成 10 进制形式


<img src="images/ip.svg" width=700 style="margin: 50px 50px">

---

## IP 地址划分

- IP 地址实际包含两部分: 网络号, 主机号 

- IPv4 地址可分为 5 大类 

- 网络号的分配被严格控制


<img src="images/ipaddr.svg" width=700 style="margin: 10px 50px">

---

## 特殊 IP 地址

- 全 0: 当前网络或者当前主机

- 全 1: 广播地址

- 127.x.x.x: 本地回环地址, 用于本地回环测试

- 内部保留地址

    - A: 10.0.0.0 - 10.255.255.255
    
    - B: 172.16.0.0 - 172.31.255.255

    - C: 192.168.0.0 - 192.168.255.255

---

## 子网

A 或者 B 类网络作为一个单一网络太大了, 人们需要接入更 多的局域网 (子网)


<img src="images/subnetwork.svg" width=700 style="margin: 50px 50px">

---

## 子网掩码

为了解决单一网络内接入不同子网的需求, 将原来的主机号中拿出一部分, 构成子网号

- IP 地址 = 网络号 + 子网号 + 主机号 

- 用子网掩码 (subnet mask) 表示网络号


<img src="images/netmask.svg" width=750 style="margin: 20px 00px">


---

## IPv4 与 IPv6

IPv4 最大问题是网络地址资源有限

- 理论上有 1600 万个网络、40 亿台主机 

- 实际: 已于 2011 年 2 月 3 日分配完毕

    - 北美占有 3/4,约 30 亿个

    - 亚洲不到 4 亿
    
    - 中国截止 2010 年 6 月 IPv4 地址数量 2.5 亿

IPv6: 地址容量为 `\(2^{128}\)`, 是 IPv4 的约 8 × `\(10^{28}\)` 倍

---

## IP 地址的设置

** 手工设置 **

- 询问管理员: 获得主机 IP 地址, 网络掩码, 网关 

- 网关 (gateway): 转发发送到子网外的数据包的机器


** 自动获取方式, Dynamic Host Configuration Protocol ** 

- 从 DHCP 服务器处自动获得 IP 地址, 网络掩码, 网关, DNS服务器等

- 设置对用户透明, 推荐普通用户使用

---

## 网关与路由示意


<img src="images/Sample_network.svg" width=900 style="margin: -100px -80px">

---

## Internet 应用程序的地址

- Internet 应用程序地址: `<IP地址, 端口号>`

- 服务器程序有公开的固定地址


<img src="images/tcpport.svg" width=600 style="margin: 20px 50px">

---

## DNS, Domain Name System

域名: 解决数字的 IP 地址难以记忆的问题

- 域名由两个或两个以上的词构成，中间由点号分隔开。最右边的那个词称为顶级域名, 之前的为二级域名

- 国际顶级域名(.com, .net, .org等)由美国ICANN管理, 如 `www.wikipedia.org`

- 国家/地区顶级域名由各国分别管理, 如.cn由CNNIC管理, 如 `www.pku.edu.cn`

- 域名的所有者可以通过查询 WHOIS 数据库找到, 如 whois.icann.org

- 国家/地区顶级域名受到越来越多的重视, 比如 .cc(已开放为国际顶级域名), .io 等

- 域名是有价值的资源

---

## 层次化的域名空间


<img src="images/Domain_name_space.svg" width=700 style="margin: 00px 50px">

---

## 实际的 DNS 解析


<img src="images/DNS_in_the_real_world.svg" width=900 style="margin: 00px 00px">

---

## 解析本地域名服务器管理的域名


<img src="images/resolv.svg" width=700 style="margin: 50px 00px">

---

## 解析非本地域名服务器管理的域名

<img src="images/An_example_of_theoretical_DNS_recursion.svg" width=900 style="margin: 00px 00px">

---

## URL, Uniform Resource Locator

一个字符串, 用于标记WEB资源的访问地址

语法:

```txt
scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
```

示例:

<pre>
               hierarchical part
        ┌────────────┴───────────────┐
              authority        path
        ┌────────┴─────────┐┌───┴────┐
  abc://user:pass@git.io:123/path/data?key=value&k2=v2#fragid1
  └┬┘   └───┬───┘ └────┘ └┬┘           └──────┬──────┘ └──┬──┘
scheme  user infor  host  port              query      fragment

</pre>


---

## World Wide Web, WWW

基于超媒体, 方便用户在 Internet 上检索和浏览信息的一种工具. WWW 和 Internet 并不等价.

- 超媒体 (hypermedia): 超文本和多媒体 (multimedia) 的结合 

- 超文本(hypertext): 用于显示文档的一种用户接口技术.  超文本文档里包含若干个指向其他文档的超链接 

- 超链接 (hyperlink): 类似于科技文献中的引用

---

## WWW 分层的功能示意


<img src="images/Internet_Key_Layers.png" width=700 style="margin: 00px 50px">

---

## WWW 超链接的一个图形化示意片段


<img src="images/WorldWideWebAroundWikipedia.png" width=700 style="margin: 00px 00px">

---

## WWW, HTTP, HTML

** 一个WEB服务器: ** 
<pre> http://www.example.org/index.html </pre>

** 客户端浏览器打开该URL地址, 发送HTTP请求: **

```xml
GET /index.html HTTP/1.1
Host: www.example.org
```

** WEB服务器发送HTTP响应: **

```xml
HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
```

** 紧随其后是返回的HTML页面内容 **

---

## HTML, CSS, Javascript

** HTML 页面内容 **

``` xml
<!DOCTYPE html>
<html>
  <head>
    <title>This is a title</title>
  </head>
  <body>
    <p>Hello world!</p>
  </body>
</html>
```

HTML4, HTML5

CSS(Cascading Style Sheets): 样式、布局

Javascript: 提供交互行为

---

## 电子邮件 Email


<img src="images/message.svg" width=680 style="margin: 00px 50px">

---

## 邮件的重要信头

信头 |  含义
:---- | :----
To   |  主要的收件人邮件地址
CC   |  次要的收件人邮件地址 (Carbon Copy)
Bcc  |  隐藏的收件人邮件地址 (Blind Carbon Copy)
From |   邮件发送者或创建者的地址
Subject | 邮件内容的简短说明
Reply-To | 该邮件的回复地址

---

## 邮件礼仪

### 标题一目了然

### 称呼体现尊重

### 正文清晰美观

### 结尾致敬签名

### 回复及时有针对


---

## Email Spam 与 Junk mail

### Email Spam

将一封相同的邮件发送给很多 (成千上万, 甚至上百万) 接收者 

- Spam 邮件通常包含广告, 或者到商业网站的链接, 是垃圾邮件

- Spam 邮件浪费了网络资源, 被视为犯罪行为

### Junk mail

垃圾邮件, 不是自己愿意收到的邮件

---

## 常见邮件访问方式

#### POP3

古老, 客户端下载邮件到本地处理

#### IMAP

邮件的存储和处理在服务器端进行

#### Web Mail

仅用浏览器即可收发邮件

#### Push e-mail

服务器将邮件推送给客户端, 常见于手机

---

## 恶意软件, malware

被专门设计用来在计算机所有者不知情的情况下, 刺探或破坏宿主计算机的软件


<img
src="images/Malware_statics_2011-03-16-en.svg" width=450 style="margin: 00px 100px">

---

## 计算机病毒, Computer virus

一类寄生于其它可执行代码或文档上、可自我复制进行传播的程序

- 不能独立存在

- 具有传染性

<img src="images/virus.svg" width=700 style="margin: 10px 00px">


---

## 病毒的寄生宿主

- 二进制可执行文件, 如.com, .exe, .dll, .sys 等 

- 脚本文件, 如.bat, .vbs 等

- 包含宏 (macro)的文档, 如.doc, .xls 等 

- 磁盘的启动扇区

- ...

---

## 病毒 vs 杀毒程序

**老的方法**

-  保持文件被感染前后的修改日期一致

-  保持被感染文件的大小不变

-  杀死病毒检测进程

**新的方法**

- 避免感染系统文件及诱饵文件

- 隐匿

- 自我修改

---

## 蠕虫, Computer worm

.left-column[
跟病毒类似, 不同之处在于蠕虫不需要宿主 

- 蠕虫利用网络进行传播, 占用网络资源

- 世界上第一个蠕虫: Xerox PARK 于 1978 设计的一个软件, 寻找空闲 CPU 帮助工作

- Internet 上第一个广受关注的蠕虫: 1988 年的 Morris Worm 

- 蠕虫除了传播, 还可以干任何事情: 有益或有害

]

.right-column[

<img src="images/Morris_Worm.jpg" width=300 style="margin: 00px 50px">

]

---

## Conficker: 2003年以来的最大Worm 


<img src="images/Conficker.svg" width=750 style="margin: -20px 00px">


---

## 木马, Trojan horse

隐藏在合法软件外衣下的恶意软件

- 木马是正常的程序, 需要受害者主动运行 

**预防木马软件**

- 当心不明邮件, 不自动打开邮件附件

- 保证反病毒程序实时检测及自动更新 

- 经常打补丁

- 小心使用 IE 及 Outlook

---

## 间谍软件, Spyware

监视用户使用计算机, 并把收集的信息发送给第三方的软件. Spyware 不会自我复制

- 2000 年, 出现了最早的 Spyware 和 Anti-Spyware

- 约 90% 的连接到 Internet 的计算机感染了 Spyware 

- 感染途径

    - 欺骗用户安装 

    - 和共享软件等绑定(不要从非正规渠道下载安装软件) 

    - 利用浏览器 (IE) 漏洞

    - 智能手机应用市场

---

## 广告软件, Adware

自动显示、下载广告信息的软件. 常和合法程序绑定, 为用户所见.

- Adware 形式和 Spyware 类似, 但是 Adware 并不收集用户信息

- Adware 通常是资助个体程序员或小公司开发软件的重要途径

- 通常和共享软件绑定: 免费使用, 有广告; 注册交费, 无广告

---

## Botnet: 有组织的蠕虫、间谍软件网络

Botnet的主要构成: Command and Control, Zombie Computer

.left-column[
.center[客户-服务器结构]
<img src="images/Server-based-network.svg" height=350 style="margin: 00px 00px">
]

.right-column[
.center[P2P结构]
<img src="images/P2P-network.svg" height=350 style="margin: 00px 50px">
]

---

## Zombie 


.r-side[
(1) Spammer's web site 

(2) Spammer 

(3) Spamware 

(4) Infected computers

(5) Virus or trojan 

(6) Mail servers 

(7) Users 

(8) Web traffic

]

.l-side[

<img src="images/Circle_of_spam.svg" width=500 style="margin: -60px 00px">

]


---

## 恶意软件利用的漏洞

- 软件的相似性

- 软件缺陷

- 未经许可的软件运行

- 用户权限过大

- 可执行程序的权限过大

---

## 防范恶意软件

- 安装杀毒软件/安全防护软件, 及时打补丁

- 使用防火墙, 禁止外部计算机通过网络访问本机

- 不随便下载运行可执行程序 

- 不打开未知的邮件附件 

- U 盘 通常带毒, 打开前要先查毒 

- 不随便暴露自己的 email、生日、手机等重要信息 

- 不以 Administrator 权限操作计算机 

