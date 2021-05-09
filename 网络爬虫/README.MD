## 第1关：urllib
任务描述

本关任务：使用python内置库urllib发起请求并返回状态码。

相关知识

Get

urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
例如，对豆瓣的一个URL`https://api.douban.com/v2/book/2129650`
进行抓取，并返回响应：
```python
 from urllib import request
    with request.urlopen(‘http://www.gliet.edu.cn/') as f:
        data = f.read()
        print(‘Status:’, f.status, f.reason)
        for k, v in f.getheaders():
            print(‘%s: %s’ % (k, v))
    print(‘Data:’, data.decode(‘utf-8’))
```
   

可以看到HTTP响应的头和数据。

如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
```python
from urllib import request
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
```
urllib更详细的用法可以参考：
https://www.liaoxuefeng.com/wiki/1016959663602400/1019223241745024
#### 编程要求
根据提示，在右侧编辑器补充代码，对给定链接发送请求。请求成功时返回Status（状态码），失败时返回错误信息。
提示：使用以下格式可输出错误信息
```

    try:
        …
    except Exception as e:
        …
```
#### 测试说明
平台会对你编写的代码进行测试：

测试输入：http://www.gliet.edu.cn/

预期输出：
```
Status: 200 OK
```


测试输入：一个错误的url，不能请求成功

预期输出：
```
<urlopen error [Errno -2] Name or service not known>
```


开始你的任务吧，祝你成功！

[Requests: HTTP for Humans](https://docs.python-requests.org/en/master/)

## 第2关：requests
### 任务描述
本关任务：使用python第三方库requests发起请求并返回状态码。

### 相关知识
Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。
##### 安装requests
在命令行下通过pip安装：
```
$ pip install requests
```
如果遇到Permission denied安装失败，请加上sudo重试。
##### 使用requests
要通过GET访问一个页面，只需要几行代码：
```
    >>> import requests
    >>> r = requests.get(‘https://www.douban.com/') # 豆瓣首页
    >>> r.status_code
    200
    >>> r.text
    r.text
```
    ‘\n\n\n<meta name=”description” content=”提供图书、电影、音乐唱片的推荐、评论和…’
无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
```
>>> r.content
    b’\n\n\n\n…’
```
requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
```
    >>> r = requests.get(‘https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
    >>> r.json()
    {‘query’: {‘count’: 1, ‘created’: ‘2017-11-17T07:14:12Z’, …
    需要传入HTTP Header时，我们传入一个dict作为headers参数：
    >>> r = requests.get(‘https://www.douban.com/', headers={‘User-Agent’: ‘Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit’})
    >>> r.text
    ‘\n\n\n\n …’
```
要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
```
    >>> r = requests.post(‘https://accounts.douban.com/login', data={‘form_email’: ‘abc@example.com’, ‘form_password’: ‘123456’})
```
requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
```
params = {‘key’: ‘value’}
    r = requests.post(url, json=params) # 内部自动序列化为JSON
```    

更多的使用方法，可以参考：
https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448
#### 编程要求
根据提示，在右侧编辑器补充代码，对给定页面进行requests请求。请求成功时返回status_code（状态码），失败时返回错误信息。
提示：使用以下格式可输出错误信息
```
try:
    …
except Exception as e:
…
```
#### 测试说明
```
平台会对你编写的代码进行测试：
测试输入：http://www.gliet.edu.cn/
预期输出：
Status: 200
测试输入：一个错误的url，不能请求成功
预期输出：
url请求失败
```

[廖雪峰的官方网站-requests](https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448)

## 第3关：re
### 任务描述
本关任务：编写一个能匹配Email地址的正则小程序。

### 相关知识
##### 正则表达式是什么

正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

##### 为什么使用正则表达式
字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。比如判断一个字符串是否是合法的Email地址，虽然可以编程提取@前后的子串，再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用。
所以我们判断一个字符串是否是合法的Email的方法是：
创建一个匹配Email的正则表达式；
用该正则表达式去匹配用户的输入来判断是否合法。
因为正则表达式也是用字符串表示的，所以，我们要首先了解如何用字符来描述字符。
##### 正则表达式语法
在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：
    ‘00\d’可以匹配’007’，但无法匹配’00A’；
    ‘\d\d\d’可以匹配’010’；
    ‘\w\w\d’可以匹配’py3’；
.可以匹配任意字符，所以：
    ‘py.’可以匹配’pyc’、’pyo’、’py!’等等。
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符。
    来看一个复杂的例子：\d{3}\s+\d{3,8}。
我们来从左到右解读一下：
    \d{3}表示匹配3个数字，例如’010’；
    \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配’ ’，’    ‘等；
    \d{3,8}表示3-8个数字，例如’1234567’。
综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
    如果要匹配’010-12345’这样的号码呢？
    由于’-‘是特殊字符，在正则表达式中，要用’'转义，所以，上面的正则是\d{3}-\d{3,8}。
##### re模块
```
    >>> import re
    >>> re.match(‘\d{3}-\d{3,8}’, ‘010-12345’)
    <re.Match object; span=(0, 9), match=’010-12345’>

```
匹配变长的字符，.*匹配任意个字符。
下面我们匹配html页面中的链接试试：
.{5}匹配5个字符，但链接明显长于5个字符，所以匹配不到。
.{1,50}匹配1到50个字符就可以匹配到了：
    >>> re.match(‘‘, ‘‘)
    <re.Match object; span=(0, 48), match=’‘>
    >>> re.match(‘‘, ‘‘)
    >>> re.match(‘‘, ‘‘)
    <re.Match object; span=(0, 48), match=’‘>

### 分组
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
```
    >>> m = re.match(r’^(\d{3})-(\d{3,8})$’, ‘010-12345’)
    >>> m
    <_sre.SRE_Match object; span=(0, 9), match=’010-12345’>
    >>> m.group(0)
    ‘010-12345’
    >>> m.group(1)
    ‘010’
    >>> m.group(2)
    ‘12345’
```
我们用分组匹配链接试试：
```
>>> re.match(‘‘, ‘‘).groups()
    (‘//tvax4.sinaimg.cn/mw600/5ed2d’,)
```
 末尾为什么会有一个逗号呢？因为groups()返回的是一个分组列表（List）
##### 贪婪匹配
最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：
```
>>> re.match(r’^(\d+)(0*)$’, ‘102300’).groups()
    (‘102300’, ‘’)
```
由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0只能匹配空字符串了。
必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
```
>>> re.match(r’^(\d+?)(0)$’, ‘102300’).groups()
    (‘1023’, ‘00’)
```
我们用贪婪匹配，匹配链接试试：
```
>>> re.match(r’^(t.)’, ‘tvax4.sinaimg.cn/mw600/5ed2d.jpg’).groups()
    ‘tvax4.sinaimg.cn/mw600/5ed2d.jpg’
    >>> re.match(r’^(t.?)’, ‘tvax4.sinaimg.cn/mw600/5ed2d.jpg’).groups()
    ‘t’
```
想了解更多正则知识，可参考：https://www.liaoxuefeng.com/wiki/1016959663602400/1017639890281664
正则表达式非常强大，要在短短的一节里讲完是不可能的。要讲清楚正则的所有内容，可以写一本厚厚的书了。如果你经常遇到正则表达式的问题，你可能需要一本正则表达式的参考书。
####  编程要求
根据提示，在右侧编辑器补充代码，成功匹配给定的Email地址并输出，如果匹配不到，输出None。
#### 测试说明
平台会对你编写的代码进行测试：
测试输入：
```
10001@qq.com
```
预期输出：
```
<re.Match object; span=(0, 12), match='10001@qq.com'>
```
测试输入：
```
qq10001
```
预期输出：
```
None
```

## 第4关：BeautifulSoup 任务描述
### 本关任务：编写一个能爬取桂电就业信息的小程序。

### 相关知识
Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。

Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。

Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。

### 环境配置
```
pip install Beautifulsoup4
```
Beautiful Soup在解析时实际是依赖解析器的，它除了支持python标准库中的HTML解析器外还支持第三方解析器如lxml等,推荐使用lxml.

安装解析器:
 ```
pip install lxml
```
##### 基本使用
创建beautifulsoup对象
```python

 soup=BeautifulSoup(html,'lxml')
```   
html: 可以为 str, 也可以是 文件句柄fp

‘lxml’: 解析器, 需安装lxml包
##### 节点选择器
直接调用节点的名称就可以选择节点元素，节点可以嵌套选择, 返回的类型都是bs4.element.Tag对象
``` 
soup.head  #获取head标签
soup.p.b #获取p节点下的b节点
soup.p.string #获取p标签下的文本
```

当同级有多个相同节点时, 节点选择器默认只选择第一个
##### 使用find_all
```python
find_all(name,attrs,recursive,text,**kwargs)

```
查询所有符合条件的元素，其中的参数:

|参数|含义|
|---|---|
|name|表示可以查找所有名字为name的标签(tag)，也可以是过滤器，正则表达式，列表或者是True|
|attrs|表示传入的属性，可以通过attrs参数以字典的形式指定如常用属性id,attrs={‘id’:’123’}，由于class属性是python中的关键字，所有在查询时需要在class后面加上下划线即class_=’element’，返回的结果是tag类型的列表|
|text|用来匹配节点的文本，传入的形式可以是字符串也可以是正则表达式对象|
|recursive|如果只想搜索直接子节点可以将参数设为false：recursive=Flase|
|limit|可以用来限制返回结果的数量，与SQL中的limit关键字类似|

find_all(条件)：查询所有符合条件的元素
查找标签名为 div 的所有元素
``` python
soup.find_all(name='div')   # name代表标签名,不是name属性
soup.find_all('div')      # 标签查找
#查找标签名为 li 或 a 的所有元素
soup.find_all(name = ['li', 'a'])
#查找 id 为 world 的所有元素
soup.find_all(id = 'world')
#查找 class 为 active 的 所有元素
soup.find_all(class_='active')  # class为python关键字,需加下划线
#查找 a 标签中,title 属性为 hello 的所有元素
soup.find_all('a', title='hello')  # 标签 加属性过滤
soup.find_all('a', title='hello', limit=2) # 限制输出, limit属性代表取前2个
#查找 a 标签中包含属性 id=’box’, class=’active’ 的所有元素
soup.find_all('a',attrs={'id':'box','class':'active'})  # 多属性过滤
#查找文本中能匹配字符串 hello 的所有元素
soup.find_all(text=re.compile('Tillie')) # 使用正则过滤查找

```

其他方法:
``` 
find( name , attrs , recursive , text , **kwargs )
```
它返回的是单个元素，也就是第一个匹配的元素，类型依然是tag类型,参数同find_all()一样
更多示例可以查看：
https://www.cnblogs.com/Deaseyy/p/11266742.html

例子（爬取先知社区的标题）
```python
import requests
from bs4 import BeautifulSoup
import re    #Regular
url = 'https://xz.aliyun.com/'
r = requests.get(url=url)
soup = BeautifulSoup(r.content,'lxml')
bbs_news = soup.find_all(name ='a',attrs={'class':'topic-title'})
for new in bbs_news:
    print new.string.strip()
```

### 编程要求
爬取桂电招聘页面的招聘信息。
页面地址：https://www.guet.edu.cn/jy/zhaopin.jsp?a165823t=475&a165823p=1&a165823c=10&urltype=tree.TreeTempUrl&wbtreeid=1003
经过简单测试，可以发现，调整a165823p的数值可以改变页数，我们可以理解这个参数为page。调整a165823c的数值可以改变每一页显示的信息条数，我们可以理解这个参数为列。
由于页面会根据就业信息变化，为了方便设置题目，请同学们爬取给定日期的信息并显示出来。可能同学们做题的时候给定日期的信息已经不在第一页了，可以自己观察修改下。
提示：给定日期的信息不在一页怎么办？爬取两页就好了呀，用request请求2页并用BeautifulSoup爬取。

### 测试说明
平台会对你编写的代码进行测试：

测试输入：
```
2020-03-02；
```
预期输出：
``` 
教育部启动“24365校园联合招聘服务” 助力高校毕业生网上求职
步步高教育电子2020春季校园招聘
天津飞腾信息技术有限公司2020招聘简章
美国安费诺电子装配（厦门）有限公司招聘简章
实力央企——中国一冶  诚邀您共建美丽中国
中铁广州工程局集团第二工程有限公司2020年校园招聘公告
中国振华电子集团贵州振华风光半导体有限公司招聘简章
嘉瑞能源科技（深圳）有限公司招聘简章
北部湾财产保险股份有限公司信息技术岗位人员招聘启事
```


测试输入：
```
2020-02-28；
```
预期输出：
``` 
摩比集团2020届校园招聘简章
深圳市伊力科电源有限公司2020招聘简章
梦想即至 |科华恒盛2020届校园招聘简章
TP-LINK普联技术生产制造体系校园招聘
长安汽车2020春季校园招聘驭爱前行
广西翅冀钢铁有限公司招聘简章
广州朗国科技2020春季校招简章
上海特金信息科技招聘信息
光宝电源科技(东莞)有限公司招聘简章
深圳海云安网络安全技术有限公司招聘信息
德国M+P国际公司北京代表处2020年春季招聘
中国十五冶2020年校园招聘简章
中冶赛迪上海工程技术有限公司湛江分公司2020招聘简章
```

[Python爬虫教学](https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html)

##  第5关：requests+BeautifulSoup桂电毕业生就业网搜索结果提取
### 任务描述
本关任务：编写一个能爬取桂电毕业生就业网搜索结果的小程序。

### 相关知识
为了完成本关任务，你需要掌握：1.爬虫设置headers头伪装浏览器，2.使用多线程进行爬虫。

### 设置headers头伪装浏览器
为什么要设置headers头信息？ 在请求网页爬取的时候，输出的text信息中会出现抱歉，无法访问等字眼，这就是禁止爬取，需要通过反爬机制去解决这个问题。headers是解决requests请求反爬的方法之一，相当于我们进去这个网页的服务器本身，假装自己本身在爬取数据。
#### requests设置headers头实例
```python
import requests
headers={
"Host": "www.dianping.com"
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
res=requests.get("http://www.dianping.com/",headers=headers)
print(res.text)
```
### Python多线程爬虫
为什么需要多线程？ 凡事知其然也要知其所以然。在了解多线程的相关知识之前，我们先来看看为什么需要多线程。打个比方吧，你要搬家了，单线程就类似于请了一个搬家工人，他一个人负责打包、搬运、开车、卸货等一系列操作流程，这个工作效率可想而知是很慢的；而多线程就相当于请了四个搬家工人，甲打包完交给已搬运到车上，然后丙开车送往目的地，最后由丁来卸货。 由此可见多线程的好处就是高效、可以充分利用资源，坏处就是各个线程之间要相互协调，否则容易乱套（类似于一个和尚挑水喝、两个和尚抬水喝、三个和尚没水喝的窘境）。所以为了提高爬虫效率，我们在使用多线程时要格外注意多线程的管理问题。 我们可以使用队列（Queue）分页对目标进行爬取，这样目标有很多页的时候可以提高抓取数据效率。
#### Python使用实现多线程爬虫实例
```python
from threading import Thread
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)  
        #super(MyThread, self).__init__()
    def run(self):
        #write this thread task
        pass
if __name__ == '__main__':
    thread = MyThread()
    thread.start()
    thread.join()
```

### Python使用使用队列（Queue）实现多线程爬虫实例

```python

from threading import Thread
from Queue import Queue
global my_queue
my_queue = Queue()
class MyThread1(Thread):
    def __init__(self):
        Thread.__init__(self)  
        #super(MyThread1, self).__init__()
    def run(self):
        put_data = "you producer data"
        my_queue.put(put_data)
        #write this thread task
        pass
class MyThread2(Thread):
    def __init__(self):
        Thread.__init__(self)  
        #super(MyThread2, self).__init__()
    def run(self):
        get_data = my_queue.get()
        #write this thread task
        pass
if __name__ == '__main__':
    thread1 = MyThread1()
    thread2 = MyThread2()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
```

### 参考链接：
https://www.cnblogs.com/songzhenhua/p/11824483.html

https://blog.csdn.net/u013787595/article/details/49446291

### 编程要求
对桂电毕业生就业网的搜索结果进行爬取，得出详情链接以及企业名称
https://www.guet.edu.cn/jy/
上一关我们只爬取结果所在的页面，本关我们爬取所有页面。
#### 提示：
虽然网站使用POST方式发送请求，但我们将参数放入URL依然能正常访问需要的页面。同学们也可以使用requests的post方式请求，看个人喜好。
经过观察发现lucenenewssearchkeyword参数为搜索的关键字，currentnum参数决定页数。

### 测试说明
平台会对你编写的代码进行测试：
Evidence函数的keyword参数为关键字，测试集会有2个不同输入，输出2019年10月23日关键字搜索结果的详情链接以及企业名称。

### 测试输入：深圳
### 预期输出：
https://www.guet.edu.cn/jy/info/1031/10496.htm

深圳市雅信通光缆有限公司来校参加双选会

https://www.guet.edu.cn/jy/info/1031/10495.htm

深圳市飞博康光通讯技术有限公司来校参加双选会

https://www.guet.edu.cn/jy/info/1031/10488.htm

深圳市慧为智能科技股份有限公司来校参加双选会

https://www.guet.edu.cn/jy/info/1031/10494.htm

深圳市拓普泰克电子有限公司来校参加双选会

https://www.guet.edu.cn/jy/info/1031/10508.htm

深圳市汇博数码电子科技有限公司来校参加双选会

## reference:
[Python3 爬虫（七）：多线程爬虫](https://wangxin1248.github.io/python/2018/09/python3-spider-7.html)

[Python爬虫4.1 — threading(多线程)用法教程](https://blog.csdn.net/Zhihua_W/article/details/102516355)

[python采用 多进程/多线程/协程 写爬虫以及性能对比，牛逼的分分钟就将一个网站爬下来! - 地球守卫者 - 博客园](https://www.cnblogs.com/huangguifeng/p/7632799.html)

[【暂时Over】Python 从零开始爬虫（十）给爬虫加速：多线程，多进程 - SegmentFault 思否](https://segmentfault.com/a/1190000016216521)

## 第6关：scrapy框架简单使用

任务描述

本关任务：编写一个使用Scrapy框架爬取桂林电子科技大学计算机与信息安全学院网站就业信息的小程序。


相关知识

Scrapy介绍

Scrapy是一个适用爬取网站数据、提取结构性数据的应用程序框架，它可以应用在广泛领域：Scrapy 常应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。通常我们可以很简单的通过 Scrapy 框架实现一个爬虫，抓取指定网站的内容或图片。


| 模块                               | 作用                                                  |
| ---------------------------------- | ----------------------------------------------------- |
| Scrapy Engine(引擎)                | 总指挥:负责数据和信号的在不同模块间的传递             |
| Scheduler(调度器)                  | 一个队列，存放引擎发过来的request请求                 |
| Downloader (下载器)                | 下载把引擎发过来的requests请求，并返回给引擎          |
| Spider (爬虫)                      | 处理引擎发来来的response,提取数据，提取url,并交给引擎 |
| Item Pipeline(管道)                | 处理引擎传过来的数据，比如存储                        |
| DownloaderMiddlewares (下载中间件) | 可以自定义的下载扩展，比如设置代理                    |
| SpiderMiddlewaresSpider(中间件)    | 可以自定义requests请求和进行response过滤              |


##### pip安装

pip install Scrapy -i http://pypi.douban.com/simple –trusted-host=pypi.douban.com

使用豆瓣源下载，速度会快些

1.创建一个scrapy项目

scrapy startproject <项目名字>

2.生成一个爬虫

scrapy genspider <爬虫名字> <爬虫范围>

示例：

scrapy genspider itcast itcast.cn

3.提取数据

完善spider,使用xpath等方法

4.保存数据

pipeline中保存数据

5.启动爬虫

scrapy crawl <爬虫名字>


Scrapy目录结构
```python

.
├── mySpider
│   ├── init.py
│   ├── items.py    自己预计需要爬取的内容
│   ├── middlewares.py    自定义中间件的文
│   ├── pipelines.py    管道，保存数据
│   ├── pycache
│   │   ├── init.cpython-37.pyc
│   │   ├── pipelines.cpython-37.pyc
│   │   └── settings.cpython-37.pyc
│   ├── settings.py    设置文件， UA，启动管道
│   └── spiders    自己定义的spider的文件夹
│       ├── init.py
│       ├── itcast.py    定义spider的文件
│       └── pycache
│           ├── init.cpython-37.pyc
│           └── itcast.cpython-37.pyc
└── scrapy.cfg        项目的配置文件

```

##### itcast.py——完善spider，在例子中为itcast.py
```python
class ItcastSpider (scrapy. Spider): -> 自定义spider类， 继承自scrapy.spider
        name = ‘itcast’   # 爬虫名字<爬虫启动时候使用: scrapy crawl itcast>
        allowed_ domains = [‘itcast.cn’]      # 允许爬取的范围,防止爬虫爬到了别的网站
        start_ _urls = [‘http://www. itcast. cn/ channel/teacher . shtml ‘]        # 开始爬取的地址

    def parse(self, response):  # 数据提起方法，接收下载中间件传过来的response
        names = response . xpath("//div [@class='tea_ con']//li/div/h3/text()")
        print(names)     # 返回包含选择器的列表
```
    
从选择器中提取字符串:

    extract() 返回一个包含有字符串数据的列表
    
    extract_frst() 返回列表中的第一个字符串
    

注意:

    spider中的parse方法名不能修改
    
    需要爬取的ur|地址必须要属于allow_ domain下的连接
    
    respone.xpath()返回的是一 个含有selector对象的列表
    
##### itcast.py——spider的数据传到pipeline
```python
 def parse(self, response) :
        teachers = response . xpath(“//div [@class=’tea_ con’]//li”)        # xpath分组提取
    for t in teachers:
        name = t.xpath(“. /div/h3/text()”) .extract_ first()
        position = t.xpath(“./div/h4/text()”). extract_ first()
        profile = t. xpath(“ ./div/p/text()”) .extract_ first()
        item = dict(
        name= name ,
        position = position,
        profiel = profile
        )
        yield item     # yield 就可以了
```
   

为什么要使用yield?

让整个函数变成一个生成器，变成generator(生成器)有什么好处?

每次遍历的时候挨个读到内存中，不会导致内存的占用量瞬间变高

pipelines.py——使用pipeline

使用pipeline
```python
 import json
        class MyspiderPipeline (object):
            def process_ item(self, item， spider):     # 实现存储方法
                with open( ‘ temp.txt’ ,’a’) as f:
                json. dump(item,f ,ensure_ ascii=False, indent=2)
```
   
完成pipeline代码后，需要在setting中设置开启

从pipeline的字典形式可以看出来，pipeline可以有多个， 而且确实pipeline能够定义多个

为什么需要多个pipeline:

    可能会有多个spider,不同的pipeline处理不同的item的内容
    
    一个spider的内容可能要做不同的操作，比如存入不同的数据库中
    
注意:

    pipeline的权重越小优先级越高
    
    pipeline中process_ ltem方法名不能修改为其他的名称
    
##### settings.py——设置使用管道
    # Configure item pipelines
    # See http://scrapy。readthedocs。org/ en/latest/topics/i tem-pi peline . html
    ITEM_ PIPELINES = {
    ‘myspider . pipelines . MyspiderPipeline’: 300,     # ‘pipeline的位置’:权重
    }
##### setting.py——设置日志显示级别，设置日志文件

同学们自己使用scrapy框架的时候一定要在setting.py中加上LOG_LEVEL = “WARNING”，不然scrapy会输出很多默认信息。实训中的setting.py不用添加。

    添加LOG_LEVEL，只显示WARNING级别以上的日志信息
    LOG_LEVEL = “WARNING”
    添加LOG_FILE，终端不会显示信息，将记录在设置的日志文件中
    LOG_FILE = “./log.log”

想要更多了解scarpy框架，可参考：

https://www.cnblogs.com/zhaopanpan/articles/9339784.html
#### 编程要求
爬取桂电招聘页面的招聘信息。

页面地址：https://www.guet.edu.cn/jy/zhaopin.jsp?a165823t=475&a165823p=1&a165823c=10&urltype=tree.TreeTempUrl&wbtreeid=1003

#### 测试说明

平台会对你编写的代码进行测试：
```
测试输入：2020-03-02；
预期输出：
北部湾财产保险股份有限公司信息技术岗位人员招聘启事
步步高教育电子2020春季校园招聘
天津飞腾信息技术有限公司2020招聘简章
美国安费诺电子装配（厦门）有限公司招聘简章
实力央企——中国一冶  诚邀您共建美丽中国
中铁广州工程局集团第二工程有限公司2020年校园招聘公告
中国振华电子集团贵州振华风光半导体有限公司招聘简章
嘉瑞能源科技（深圳）有限公司招聘简章
教育部启动“24365校园联合招聘服务” 助力高校毕业生网上求职

测试输入：2020-02-28；
预期输出：
深圳海云安网络安全技术有限公司招聘信息
德国M+P国际公司北京代表处2020年春季招聘
中国十五冶2020年校园招聘简章
中冶赛迪上海工程技术有限公司湛江分公司2020招聘简章
摩比集团2020届校园招聘简章
深圳市伊力科电源有限公司2020招聘简章
梦想即至 |科华恒盛2020届校园招聘简章
TP-LINK普联技术生产制造体系校园招聘
长安汽车2020春季校园招聘驭爱前行
广西翅冀钢铁有限公司招聘简章
广州朗国科技2020春季校招简章
上海特金信息科技招聘信息
光宝电源科技(东莞)有限公司招聘简章
```
